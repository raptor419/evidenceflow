#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
from tensorflow.contrib.tensorboard.plugins import projector
import numpy as np

PATH = os.getcwd()

LOG_DIR = PATH + '/embeddings/log/'
metadata = os.path.join(LOG_DIR, 'metadata.tsv')

import pandas as pd
A=pd.read_csv("embeddings/vector.tsv",sep="\t",header=None)


# In[2]:


images=tf.Variable(A)


# In[3]:


with tf.Session() as sess:
    saver = tf.train.Saver([images])

    sess.run(images.initializer)
    saver.save(sess, os.path.join(LOG_DIR, 'images.ckpt'))

    config = projector.ProjectorConfig()
    # One can add multiple embeddings.
    embedding = config.embeddings.add()
    embedding.tensor_name = images.name
    # Link this tensor to its metadata file (e.g. labels).
    embedding.metadata_path = metadata
    # Saves a config file that TensorBoard will read during startup.
    projector.visualize_embeddings(tf.summary.FileWriter(LOG_DIR), config)


# In[ ]:




