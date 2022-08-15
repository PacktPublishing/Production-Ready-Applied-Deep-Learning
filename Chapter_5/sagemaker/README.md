## Utilizing SageMaker for ETL

[SageMaker](https://aws.amazon.com/sagemaker/) is an end-to-end service for machine learning. You can configure SageMaker to handle data processing, model development with notebooks, model training, as well as deployment of models to a production setting.

In this repository,
* we explain [how to set up a SageMaker Studio](./sagemaker_studio.md), a web-based development environment for SageMaker.
* [A sample model training implementation on SageMaker](./cifar10-tensorflow.ipynb). The model is [ResNet](https://arxiv.org/abs/1512.03385) trained with [CIFAR 10](https://www.cs.toronto.edu/~kriz/cifar.html) for image classification.
