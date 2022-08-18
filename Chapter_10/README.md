# Improving Inference Efficiency

This chapter introduces techniques for improving the inference latency while maintaining the original performance as much as possible.

In this repository, we provide solid examples for the following techniques:

#TODO: sample code to be filled
* Network quantization: reducing the number of bits used for model parameters
  * [Network quantization using TensorFlow](link or notebook)
  * [Network quantization using PyTorch](./network_quantization_pytorch.ipynb)
* Weight sharing: reducing the number of distinct weight values
  * [Weight sharing using TensorFlow](link or notebook)
  * [Weight sharing using PyTorch](./weight_sharing_pytorch.ipynb)
* Network pruning: eliminating unnecessary connections within the network
  * [Network pruning using TensorFlow](link or notebook)
  * [Network pruning using PyTorch](./network_pruning_pytorch.ipynb)
