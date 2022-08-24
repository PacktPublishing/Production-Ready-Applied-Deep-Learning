# Improving Inference Efficiency

This chapter introduces techniques for improving the inference latency while maintaining the original performance as much as possible.

In this repository, we provide solid examples for the following techniques:

* Network quantization: reducing the number of bits used for model parameters
  * [Network quantization using TensorFlow](./network_quantization_tf.ipynb)
  * [Network quantization using PyTorch](./network_quantization_pytorch.ipynb)
* Weight sharing: reducing the number of distinct weight values
  * [Weight sharing using TensorFlow](./weight_sharing_tf.ipynb)
  * [Weight sharing using PyTorch](./weight_sharing_pytorch.ipynb)
* Network pruning: eliminating unnecessary connections within the network
  * [Network pruning using TensorFlow](./network_pruning_tf.ipynb)
  * [Network pruning using PyTorch](./network_pruning_pytorch.ipynb)
