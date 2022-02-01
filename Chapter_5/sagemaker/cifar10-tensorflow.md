```python
# This code has been taken from AWS sample link below, and made some corrections to run successfully
# https://aws.amazon.com/getting-started/hands-on/train-tune-deep-learning-model-amazon-sagemaker/
```


```python

# (1) under root folder /, create a new file named "generate_cifar10_tfrecords.py". first you have to choose text file which will create untitled.txt, 
# which has to be renamed as "generate_cifar10_tfrecords.py"

# (2) Copy the code from below file path and put inside the newly created file "generate_cifar10_tfrecords.py" and save it.
# https://github.com/aws/amazon-sagemaker-examples/blob/master/advanced_functionality/tensorflow_bring_your_own/utils/generate_cifar10_tfrecords.py
```


```python
# install ipywidgets library
!pip install ipywidgets
```


```python
# helps to setup data directory for cifar10 dataset (tar.gz file from  https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz)
!python generate_cifar10_tfrecords.py --data-dir cifar10
```


```python
import time, os, sys
import sagemaker, boto3
import numpy as np
import pandas as pd

sess = boto3.Session()
sm   = sess.client('sagemaker')
role = sagemaker.get_execution_role()
sagemaker_session = sagemaker.Session(boto_session=sess)

datasets = sagemaker_session.upload_data(path='cifar10', key_prefix='datasets/cifar10-dataset')
datasets 
```


```python
from smexperiments.experiment import Experiment
from smexperiments.trial import Trial
from smexperiments.trial_component import TrialComponent
# change the experiment_name if needed. Experiment name has to be unique within and AWS account and AWS region
training_experiment = Experiment.create(
                                experiment_name = "sagemaker-experiments-v1", 
                                description     = "Experiment to track cifar10 training trials", 
                                sagemaker_boto_client=sm)
########### set up trial

l_experiment_name = training_experiment.experiment_name
print(l_experiment_name)
# Trial name should be unique
single_gpu_trial = Trial.create(
    trial_name = 'sagemaker-single-gpu-training-v1', 
    experiment_name = training_experiment.experiment_name,
    sagemaker_boto_client = sm,
)

trial_comp_name = 'single-gpu-training-job'
experiment_config = {"ExperimentName": training_experiment.experiment_name, 
                       "TrialName": single_gpu_trial.trial_name,
                       "TrialComponentDisplayName": trial_comp_name}
```


```python
%tb
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.layers import Input, Dense, Flatten
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.optimizers import Adam, SGD
import argparse
import os
import re
import time

HEIGHT = 32
WIDTH = 32
DEPTH = 3
NUM_CLASSES = 10

def single_example_parser(serialized_example):
    """Parses a single tf.Example into image and label tensors."""
    # Dimensions of the images in the CIFAR-10 dataset.
    # See http://www.cs.toronto.edu/~kriz/cifar.html for a description of the
    # input format.
    features = tf.io.parse_single_example(
        serialized_example,
        features={
            'image': tf.io.FixedLenFeature([], tf.string),
            'label': tf.io.FixedLenFeature([], tf.int64),
        })
    image = tf.decode_raw(features['image'], tf.uint8)
    image.set_shape([DEPTH * HEIGHT * WIDTH])

    # Reshape from [depth * height * width] to [depth, height, width].
    image = tf.cast(
        tf.transpose(tf.reshape(image, [DEPTH, HEIGHT, WIDTH]), [1, 2, 0]),
        tf.float32)
    label = tf.cast(features['label'], tf.int32)
    
    image = train_preprocess_fn(image)
    label = tf.one_hot(label, NUM_CLASSES)
    
    return image, label

def train_preprocess_fn(image):

    # Resize the image to add four extra pixels on each side.
    image = tf.image.resize_with_crop_or_pad(image, HEIGHT + 8, WIDTH + 8)

    # Randomly crop a [HEIGHT, WIDTH] section of the image.
    image = tf.image.random_crop(image, [HEIGHT, WIDTH, DEPTH])

    # Randomly flip the image horizontally.
    image = tf.image.random_flip_left_right(image)
    return image

def get_dataset(filenames, batch_size):
    """Read the images and labels from 'filenames'."""
    # Repeat infinitely.
    dataset = tf.data.TFRecordDataset(filenames).repeat().shuffle(10000)

    # Parse records.
    dataset = dataset.map(single_example_parser, num_parallel_calls=tf.data.experimental.AUTOTUNE)

    # Batch it up.
    dataset = dataset.batch(batch_size, drop_remainder=True)
    return dataset

def get_model(input_shape, learning_rate, weight_decay, optimizer, momentum):
    input_tensor = Input(shape=input_shape)
    base_model = keras.applications.resnet50.ResNet50(include_top=False,
                                                          weights='imagenet',
                                                          input_tensor=input_tensor,
                                                          input_shape=input_shape,
                                                          classes=None)
    x = Flatten()(base_model.output)
    predictions = Dense(NUM_CLASSES, activation='softmax')(x)
    model = Model(inputs=base_model.input, outputs=predictions)
    return model

def main():
    # Hyper-parameters
    epochs       = 10
    lr           = .01
    batch_size   = 128
    momentum     = 2e-4
    weight_decay = 0.9
    optimizer    = 'sgd'
    model_dir = 's3://sagemaker-us-east-2-058199717680/models/cifar10/'

    # SageMaker options
    training_dir   = 's3://sagemaker-us-east-2-058199717680/datasets/cifar10-dataset'
    validation_dir = 's3://sagemaker-us-east-2-058199717680/datasets/cifar10-dataset'
    eval_dir       = 's3://sagemaker-us-east-2-058199717680/datasets/cifar10-dataset'
    
    
    print(f"training: {training_dir} | valid: {validation_dir} | eval: {eval_dir}")
    print(f"optimizer: {optimizer}")

    train_dataset = get_dataset(training_dir+'/train.tfrecords',  batch_size)
    val_dataset   = get_dataset(validation_dir+'/validation.tfrecords', batch_size)
    eval_dataset  = get_dataset(eval_dir+'/eval.tfrecords', batch_size)
    
    input_shape = (HEIGHT, WIDTH, DEPTH)
    model = get_model(input_shape, lr, weight_decay, optimizer, momentum)
    
    # Optimizer
    if optimizer.lower() == 'sgd':
        opt = SGD(lr=lr, decay=weight_decay, momentum=momentum)
    else:
        opt = Adam(lr=lr, decay=weight_decay)

    # Compile model
    model.compile(optimizer=opt,
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    
    # Train model
    history = model.fit(train_dataset, steps_per_epoch=40000 // batch_size,
                        validation_data=val_dataset, 
                        validation_steps=10000 // batch_size,
                        epochs=epochs)
                        
    
    # Evaluate model performance
    score = model.evaluate(eval_dataset, steps=10000 // batch_size, verbose=1)
    print('Test loss    :', score[0])
    print('Test accuracy:', score[1])
    
    # Save model to model directory
    model.save(f'{model_dir}/{time.strftime("%m%d%H%M%S", time.gmtime())}', save_format='tf')


#%%
if __name__ == "__main__":
     
    main()


```


```python
# TUNE HYPERPARMETERS
###################


from sagemaker.tensorflow import TensorFlow

hyperparams={'epochs'       : 30,
             'learning-rate': 0.01,
             'batch-size'   : 256,
             'weight-decay' : 2e-4,
             'momentum'     : 0.9,
             'optimizer'    : 'adam'}

bucket_name = sagemaker_session.default_bucket()
output_path = f's3://{bucket_name}/jobs'
metric_definitions = [{'Name': 'val_acc', 'Regex': 'val_acc: ([0-9\\.]+)'}]

tf_estimator = TensorFlow(entry_point          = 'cifar10-training-sagemaker.py', 
                          output_path          = f'{output_path}/',
                          code_location        = output_path,
                          role                 = role,
                          train_instance_count = 1, 
                          train_instance_type  = 'ml.g4dn.xlarge',
                          framework_version    = '1.15.2', 
                          py_version           = 'py3',
                          script_mode          = True,
                          metric_definitions   = metric_definitions,
                          sagemaker_session    = sagemaker_session,
                          hyperparameters      = hyperparams)

job_name=f'tensorflow-single-gpu-{time.strftime("%Y-%m-%d-%H-%M-%S", time.gmtime())}'
tf_estimator.fit({'training'  : datasets,
                  'validation': datasets,
                  'eval'      : datasets},
                 job_name = job_name,
                 experiment_config=experiment_config)
```


```python
# visualize training job
from sagemaker.tensorflow import TensorFlow

hyperparams={'epochs'       : 30,
             'learning-rate': 0.01,
             'batch-size'   : 256,
             'weight-decay' : 2e-4,
             'momentum'     : 0.9,
             'optimizer'    : 'adam'}

bucket_name = sagemaker_session.default_bucket()
output_path = f's3://{bucket_name}/jobs'
metric_definitions = [{'Name': 'val_acc', 'Regex': 'val_acc: ([0-9\\.]+)'}]

tf_estimator = TensorFlow(entry_point          = 'cifar10-training-sagemaker-v2.py', 
                          output_path          = f'{output_path}/',
                          code_location        = output_path,
                          role                 = role,
                          train_instance_count = 1, 
                          train_instance_type  = 'ml.g4dn.xlarge',
                          framework_version    = '1.15.2', 
                          py_version           = 'py3',
                          script_mode          = True,
                          metric_definitions   = metric_definitions,
                          sagemaker_session    = sagemaker_session,
                          hyperparameters      = hyperparams)

job_name=f'tensorflow-single-gpu-{time.strftime("%Y-%m-%d-%H-%M-%S", time.gmtime())}'
tf_estimator.fit({'training'  : datasets,
                  'validation': datasets,
                  'eval'      : datasets},
                 job_name = job_name,
                 experiment_config=experiment_config)
```


```python
# PARAMETER TUNING
###################
# NOTE: Running this requires account level resources to allow running certain number of a node type. Otherwise throws below error.
########
# ERROR:
########
#  The account-level service limit 'ml.g4dn.xlarge for training job usage' is 2 Instances, with current utilization of 2 Instances 
# and a request delta of 8 Instances. Please contact AWS support to request an increase for this limit.

from sagemaker.tuner import IntegerParameter, CategoricalParameter, ContinuousParameter, HyperparameterTuner

hyperparameter_ranges = {
    'epochs'        : IntegerParameter(5, 30),
    'learning-rate' : ContinuousParameter(0.001, 0.1, scaling_type='Logarithmic'), 
    'batch-size'    : CategoricalParameter(['128', '256', '512']),
    'momentum'      : ContinuousParameter(0.9, 0.99),
    'optimizer'     : CategoricalParameter(['sgd', 'adam'])
}

objective_metric_name = 'val_acc'
objective_type = 'Maximize'
metric_definitions = [{'Name': 'val_acc', 'Regex': 'val_acc: ([0-9\\.]+)'}]

tf_estimator = TensorFlow(entry_point          = 'cifar10-training-sagemaker-v2.py', 
                          output_path          = f'{output_path}/',
                          code_location        = output_path,
                          role                 = role,
                          train_instance_count = 1, 
                          train_instance_type  = 'ml.g4dn.xlarge',
                          framework_version    = '1.15', 
                          py_version           = 'py3',
                          script_mode          = True,
                          metric_definitions   = metric_definitions,
                          sagemaker_session    = sagemaker_session)

tuner = HyperparameterTuner(estimator             = tf_estimator,
                            objective_metric_name = objective_metric_name,
                            hyperparameter_ranges = hyperparameter_ranges,
                            metric_definitions    = metric_definitions,
                            max_jobs              = 16,
                            max_parallel_jobs     = 8,
                            objective_type        = objective_type)

job_name=f'tf-hpo-{time.strftime("%Y-%m-%d-%H-%M-%S", time.gmtime())}'
tuner.fit({'training'  : datasets,
           'validation': datasets,
           'eval'      : datasets},
            job_name = job_name)
```


```python

```
