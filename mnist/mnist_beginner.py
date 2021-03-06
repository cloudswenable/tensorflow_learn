#!/usr/bin/env python


import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data


if __name__ == "__main__":
    mnist = input_data.read_data_sets("mnist_data/", one_hot=True)

    x = tf.placeholder(tf.float32, [None, 784])

    W = tf.Variable(tf.zeros([784, 10]))
    b = tf.Variable(tf.zeros([10]))

    y = tf.nn.softmax(tf.matmul(x,W)+b)

    y_ = tf.placeholder(tf.float32, [None, 10])
    cost = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
    train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cost)

    init = tf.initialize_all_variables()

    sess = tf.Session()
    sess.run(init)

    for i in range(1000000):
        batch_xs, batch_ys = mnist.train.next_batch(100)
        sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})


