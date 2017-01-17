"""
"""
from __future__ import print_function, division

import sys
import timeit

import numpy
import theano
import theano.tensor as T
from theano.sandbox.rng_mrg import MRG_RandomStreams

from logistic_sgd import LogisticRegression
from mlp import HiddenLayer
from rbm import RBM
from utils import load_traindata, load_testdata


# start-snippet-1


class DBN(object):
    """Deep Belief Network

    A deep belief network is obtained by stacking several RBMs on top of each
    other. The hidden layer of the RBM at layer `i` becomes the input of the
    RBM at layer `i+1`. The first layer RBM gets as input the input of the
    network, and the hidden layer of the last RBM represents the output. When
    used for classification, the DBN is treated as a MLP, by adding a logistic
    regression layer on top.
    """

    def __init__(self, numpy_rng, theano_rng=None, n_ins=3,
                 hidden_layers_sizes=[6, 12], n_outs=5):
        """This class is made to support a variable number of layers.

        :type numpy_rng: numpy.random.RandomState
        :param numpy_rng: numpy random number generator used to draw initial
                    weights

        :type theano_rng: theano.tensor.shared_randomstreams.RandomStreams
        :param theano_rng: Theano random generator; if None is given one is
                           generated based on a seed drawn from `rng`

        :type n_ins: int
        :param n_ins: dimension of the input to the DBN

        :type hidden_layers_sizes: list of ints
        :param hidden_layers_sizes: intermediate layers size, must contain
                               at least one value

        :type n_outs: int
        :param n_outs: dimension of the output of the network
        """

        self.sigmoid_layers = []
        self.rbm_layers = []
        self.params = []
        self.n_layers = len(hidden_layers_sizes)

        assert self.n_layers > 0

        if not theano_rng:
            theano_rng = MRG_RandomStreams(numpy_rng.randint(2 ** 10))

        # allocate symbolic variables for the data

        # the data is presented as rasterized images
        self.x = T.matrix('x')

        # the labels are presented as 1D vector of [int] labels
        self.y = T.ivector('y')
        # end-snippet-1
        # The DBN is an MLP, for which all weights of intermediate
        # layers are shared with a different RBM.  We will first
        # construct the DBN as a deep multilayer perceptron, and when
        # constructing each sigmoidal layer we also construct an RBM
        # that shares weights with that layer. During pretraining we
        # will train these RBMs (which will lead to chainging the
        # weights of the MLP as well) During finetuning we will finish
        # training the DBN by doing stochastic gradient descent on the
        # MLP.

        for i in range(self.n_layers):
            # construct the sigmoidal layer

            # the size of the input is either the number of hidden
            # units of the layer below or the input size if we are on
            # the first layer
            if i == 0:
                input_size = n_ins
            else:
                input_size = hidden_layers_sizes[i - 1]

            # the input to this layer is either the activation of the
            # hidden layer below or the input of the DBN if you are on
            # the first layer
            if i == 0:
                layer_input = self.x
            else:
                layer_input = self.sigmoid_layers[-1].output

            sigmoid_layer = HiddenLayer(rng=numpy_rng,
                                        input=layer_input,
                                        n_in=input_size,
                                        n_out=hidden_layers_sizes[i],
                                        activation=T.nnet.sigmoid)

            # add the layer to our list of layers
            self.sigmoid_layers.append(sigmoid_layer)

            # its arguably a philosophical question...  but we are
            # going to only declare that the parameters of the
            # sigmoid_layers are parameters of the DBN. The visible
            # biases in the RBM are parameters of those RBMs, but not
            # of the DBN.
            self.params.extend(sigmoid_layer.params)

            # Construct an RBM that shared weights with this layer
            rbm_layer = RBM(numpy_rng=numpy_rng,
                            theano_rng=theano_rng,
                            input=layer_input,
                            n_visible=input_size,
                            n_hidden=hidden_layers_sizes[i],
                            W=sigmoid_layer.W,
                            hbias=sigmoid_layer.b)
            self.rbm_layers.append(rbm_layer)

        # We now need to add a logistic layer on top of the MLP
        self.logLayer = LogisticRegression(
            input=self.sigmoid_layers[-1].output,
            n_in=hidden_layers_sizes[-1],
            n_out=n_outs)
        self.params.extend(self.logLayer.params)

        # compute the cost for second phase of training, defined as the
        # negative log likelihood of the logistic regression (output) layer
        self.finetune_cost = self.logLayer.negative_log_likelihood(self.y)

        # compute the gradients with respect to the model parameters
        # symbolic variable that points to the number of errors made on the
        # minibatch given by self.x and self.y
        self.errors = self.logLayer.errors(self.y)
        self.predict = self.logLayer.y_pred

    def pretraining_functions(self, train_set_x, batch_size, k):
        '''
        Generates a list of functions, for performing one step of
        gradient descent at a given layer. The function will require
        as input the minibatch index, and to train an RBM you just
        need to iterate, calling the corresponding function on all
        minibatch indexes.

        :type train_set_x: theano.tensor.TensorType
        :param train_set_x: Shared var. that contains all datapoints used
                            for training the RBM
        :type batch_size: int
        :param batch_size: size of a [mini]batch
        :param k: number of Gibbs steps to do in CD-k / PCD-k
        '''

        # index to a [mini]batch
        index = T.lscalar('index')  # index to a minibatch
        learning_rate = T.scalar('lr')  # learning rate to use

        # begining of a batch, given `index`
        batch_begin = index * batch_size
        # ending of a batch given `index`
        batch_end = batch_begin + batch_size

        pretrain_fns = []
        for rbm in self.rbm_layers:
            # get the cost and the updates list
            # using CD-k here (persisent=None) for training each RBM.
            # TODO: change cost function to reconstruction error
            cost, updates = rbm.get_cost_updates(learning_rate,
                                                 persistent=None, k=k)

            # compile the theano function
            fn = theano.function(
                inputs=[index, theano.In(learning_rate, value=0.1)],
                outputs=cost,
                updates=updates,
                givens={
                    self.x: train_set_x[batch_begin:batch_end]
                }
            )
            # append `fn` to the list of functions
            pretrain_fns.append(fn)

        return pretrain_fns

    def build_finetune_functions(self, datasets, batch_size, learning_rate):
        '''Generates a function `train` that implements one step of
        finetuning, a function `validate` that computes the error on a
        batch from the validation set, and a function `test` that
        computes the error on a batch from the testing set

        :type datasets: list of pairs of theano.tensor.TensorType
        :param datasets: It is a list that contain all the datasets;
                        the has to contain three pairs, `train`,
                        `valid`, `test` in this order, where each pair
                        is formed of two Theano variables, one for the
                        datapoints, the other for the labels
        :type batch_size: int
        :param batch_size: size of a minibatch
        :type learning_rate: float
        :param learning_rate: learning rate used during finetune stage
        '''

        (train_set_x, train_set_y) = datasets[0]
        (test_set_x, test_set_y) = datasets[1]

        # compute number of minibatches for training, validation and testing
        n_test_batches = test_set_x.get_value(borrow=True).shape[0]
        n_test_batches //= batch_size

        index = T.lscalar('index')  # index to a [mini]batch

        # compute the gradients with respect to the model parameters
        gparams = T.grad(self.finetune_cost, self.params)

        # compute list of fine-tuning updates
        updates = []
        for param, gparam in zip(self.params, gparams):
            updates.append((param, param - gparam * learning_rate))

        train_fn = theano.function(
            inputs=[index],
            outputs=self.finetune_cost,
            updates=updates,
            givens={
                self.x: train_set_x[
                        index * batch_size: (index + 1) * batch_size
                        ],
                self.y: train_set_y[
                        index * batch_size: (index + 1) * batch_size
                        ]
            }
        )

        test_score_i = theano.function(
            [index],
            self.errors,
            givens={
                self.x: test_set_x[
                        index * batch_size: (index + 1) * batch_size
                        ],
                self.y: test_set_y[
                        index * batch_size: (index + 1) * batch_size
                        ]
            }
        )

        test_label_i = theano.function(
            [index],
            self.predict,
            givens={
                self.x: test_set_x[
                        index * batch_size: (index + 1) * batch_size
                        ],
            }
        )

        # Create a function that scans the entire validation set
        # def valid_score():
        #   return [valid_score_i(i) for i in range(n_valid_batches)]

        # Create a function that scans the entire test set
        def test_score():
            return [test_score_i(i) for i in range(n_test_batches)]

        def test_label():
            return [test_label_i(i) for i in range(n_test_batches)]

        return train_fn, test_score, test_label


class runDBN():
    def __init__(self):
        self.dbn = []
        self.datasets = []
        self.rawdata = []
        self.n_train_batches = []
        self.totalscore = 0
        self.totalresult = ''
        self.score = []
        self.indexname = []
        self.rootindex = ''
        self.trained = []
        self.tested = []
        self.scoretable = {
            0: 95,
            1: 85,
            2: 75,
            3: 65,
            4: 55,
        }

        self.translate_result = {
            0: '优秀',
            1: '良好',
            2: '中等',
            3: '合格',
            4: '不合格'
        }

    def resetTest(self):
        self.totalresult = ''
        self.totalscore = 0
        self.score = []
        self.tested = [False for _ in self.indexname]
        self.datasets = [[data[0]] for data in self.datasets]

    def setIndexname(self, index):
        self.indexname = index
        self.trained = [False for _ in index]
        self.tested = [False for _ in index]
        self.n_train_batches = [0 for _ in index]
        self.dbn = [DBN(numpy_rng=numpy.random.RandomState(123)) for _ in index]

    def setRootIndex(self, index):
        self.rootindex = index

    def calc_totalscore(self, MainWindow):
        lv = MainWindow.level - 1
        score = self.score
        while lv != 1:  # not in the root level
            lv -= 1
            tmpscore = []
            fatherwidget = MainWindow.get_all_level_k_widget(lv)
            for node in fatherwidget:
                tmp = 0.0
                sum_weight = 0
                childNum = node.childCount()
                for val in range(childNum):
                    childnode = node.child(val)
                    tmp += score[val] * int(childnode.text(1))
                    sum_weight += int(childnode.text(1))
                tmpscore.append(tmp / sum_weight)
                result = self.calc_result(tmpscore[-1])
                self.print_result(MainWindow, node.text(0), result, node.text(1))
            score = tmpscore

    def print_result(self, MainWindow, index, result, weight):
        MainWindow.outui.textEdit.append('指标名称 : {}'.format(index))
        MainWindow.outui.textEdit.append('评估结果 : {}'.format(result))
        MainWindow.outui.textEdit.append('指标权重 ：{}\n'.format(weight))

    def calc_result(self, score):
        result = {
            (90, 100): '优秀',
            (80, 90): '良好',
            (70, 80): '中等',
            (60, 70): '合格',
            (0, 60): '不合格'
        }
        key = result.keys()
        key = [i for i in key]
        key.sort(key=lambda x: x[0], reverse=True)
        for score_range in key:
            if score in range(score_range[0], score_range[1]):
                return result[score_range]

    def pretrain_DBN(self, MainWindow):
        trainFilePath = MainWindow.dialog_selectTrain.getPath()
        trainIndex = MainWindow.comboBox_indexName.currentIndex()
        pretraining_epochs = int(MainWindow.lineEdit_epoch.text())
        pretrain_lr = float(MainWindow.lineEdit_lr.text())
        batch_size = int(MainWindow.lineEdit_batch.text())
        train_set_x, train_set_y, feaNum, rawdata = load_traindata(trainFilePath)
        # when we haven't trained this index, we trained it, otherwise refresh the datasets.
        if self.trained[trainIndex]:
            self.datasets[trainIndex] = [(train_set_x, train_set_y)]
            self.rawdata[trainIndex] = rawdata
        else:
            self.datasets.append([(train_set_x, train_set_y)])
            self.rawdata.append(rawdata)
            name = MainWindow.comboBox_indexName.currentText()
            MainWindow.comboBox_indexName.setItemText(trainIndex, name + ' (*)')

        self.trained[trainIndex] = True
        self.n_train_batches[trainIndex] = train_set_x.get_value(borrow=True).shape[0] // batch_size
        hidden_layer_sizes = []
        if MainWindow.checkBox_lv1.isChecked():
            hidden_layer_sizes.append(int(MainWindow.lineEdit_lv1.text()))

        if MainWindow.checkBox_lv2.isChecked():
            hidden_layer_sizes.append(int(MainWindow.lineEdit_lv2.text()))

        if MainWindow.checkBox_lv3.isChecked():
            hidden_layer_sizes.append(int(MainWindow.lineEdit_lv3.text()))

        # numpy random generator
        numpy_rng = numpy.random.RandomState(123)
        # construct the Deep Belief Network
        self.dbn[trainIndex] = DBN(numpy_rng=numpy_rng, n_ins=feaNum,
                                   hidden_layers_sizes=hidden_layer_sizes,
                                   n_outs=5)
        # n_out=5, for we only have A+ A B C D.

        # start-snippet-2
        #########################
        # PRETRAINING THE MODEL #
        #########################
        k = 1
        print('... getting the pretraining functions')
        pretraining_fns = self.dbn[trainIndex].pretraining_functions(train_set_x=train_set_x,
                                                                     batch_size=batch_size,
                                                                     k=k)
        print('... pre-training the model')
        start_time = timeit.default_timer()
        # Pre-train layer-wise
        for i in range(self.dbn[trainIndex].n_layers):
            for epoch in range(pretraining_epochs):
                c = []
                for batch_index in range(self.n_train_batches[trainIndex]):
                    c.append(pretraining_fns[i](index=batch_index,
                                                lr=pretrain_lr))
                print('Pre-training layer %i, epoch %d, cost ' % (i, epoch), end=' ')
                print(numpy.mean(c))

        end_time = timeit.default_timer()
        print('The pretraining code for file ' +
              'ran for %.2fm' % ((end_time - start_time) / 60.), file=sys.stderr)
        # end-snippet-2

    def test_DBN(self, MainWindow):
        batch_size = 4
        finetune_lr = 0.1
        training_epochs = 1000
        testIndex = MainWindow.comboBox_testIndex.currentIndex()
        testFilePath = MainWindow.dialog_selectTest.getPath()
        if not self.tested[testIndex]:
            self.tested[testIndex] = True
        test_set_x, test_set_y = load_testdata(testFilePath, self.rawdata[testIndex], batch_size)
        self.datasets[testIndex].append((test_set_x, test_set_y))
        # get the training, validation and testing function for the model
        print('... getting the finetuning functions')
        train_fn, test_model, predict_model = self.dbn[testIndex].build_finetune_functions(
            datasets=self.datasets[testIndex],
            batch_size=batch_size,
            learning_rate=finetune_lr
        )

        print('... finetuning the model')
        # early-stopping parameters
        # look as this many examples regardless
        start_time = timeit.default_timer()
        epoch = 0
        while (epoch < training_epochs):
            epoch = epoch + 1
            for minibatch_index in range(self.n_train_batches[testIndex]):
                train_fn(minibatch_index)

        end_time = timeit.default_timer()
        print('The fine tuning code for file ' +
              'ran for %.2fm' % ((end_time - start_time) / 60.), file=sys.stderr)

        predict_label = predict_model()
        last_label = []
        for eachbatch in predict_label:
            last_label.extend(eachbatch.tolist())

        MainWindow.lineEdit_result.setText(str(self.translate_result[last_label[-1]]))
        # MainWindow.outui.textEdit.append('指标名称 : {}'.format(MainWindow.comboBox_testIndex.currentText()))
        # MainWindow.outui.textEdit.append('评估结果 : {}'.format(MainWindow.lineEdit_result.text()))
        # MainWindow.outui.textEdit.append('指标权重 ：{}\n'.format(MainWindow.indexweight[testIndex]))
        self.print_result(MainWindow, MainWindow.comboBox_testIndex.currentText(), MainWindow.lineEdit_result.text(),
                          MainWindow.indexweight[testIndex])
        name = MainWindow.comboBox_testIndex.currentText()
        MainWindow.comboBox_testIndex.setItemText(testIndex, name + ' (*)')
        self.score.append(self.scoretable[last_label[0]])
        if not (False in self.tested):
            self.calc_totalscore(MainWindow)
