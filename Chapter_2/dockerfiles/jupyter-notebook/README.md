## How to Create Docker Image for Data Science 

##### Purge dangling images

	docker system prune

###### Build the image. 

    docker build --no-cache -t py3-jupyter .
    
###### Run Build
    docker run -it -p 8888:8888 -v ${PWD}/:/home/jovyan py3-jupyter:latest
    
    
  - In the console of last docker run command above, it will show the link 127.0.0.1:8888.
    Just clicking on it will open the Jupyter endpoint in the default browser.
    Files saved under work directory will be visiable on current directory

  - Open a new notebook and type below to verify pyspark, tensorflow, pytorch, pytorch_lightning, analytics-zoo, 
    and bigDL.

          import pyspark
          import tensorflow as tf
          from tensorflow import keras
          from tensorflow.keras import layers
          import torch
          import pytorch_lightning
          import matplotlib
          from elephas.utils.rdd_utils import to_simple_rdd
          from zoo.orca import init_orca_context, stop_orca_context
          from zoo.orca.learn.trigger import EveryEpoch
          from zoo.orca.learn.pytorch import Estimator
          from bigdl.util.common import *
          from bigdl.nn.layer import *
