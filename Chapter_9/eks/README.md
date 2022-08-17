## Inferencing using Elastic Kubernetes Service

This first section of this chapter describes EKS-based approach. We introduce how to create inference endpoints for TensorFlow (TF) and PyTorch models and deploy them using EKS. We will also introduce Elastic Inference (EI) accelerator which can increase the throughput while reducing the cost. EKS clusters have pods that host the inference endpoints as webservers. As the last topic for EKS-based deployment, we will introduce how the pods can be scaled horizontally for the dynamic incoming traffic.

# TODO: please add notebooks
* [Inference endpoint for TensorFlow](./tf-inference.ipynb)
* [Inference endpoint for PyTorch](./pytorch-inference.ipynb)
* [Elastic Inference (EI) accelerator](./ei-inference.ipynb)
