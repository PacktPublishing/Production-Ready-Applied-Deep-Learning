## Inferencing using Elastic Kubernetes Service

This first section of this chapter describes EKS-based approach. 
We introduce how to create inference endpoints for TensorFlow (TF) and PyTorch models and deploy them using EKS. We will also introduce Elastic Inference (EI) accelerator which can increase the throughput while reducing the cost. EKS clusters have pods that host the inference endpoints as webservers. As the last topic for EKS-based deployment, 
we will introduce how the pods can be scaled horizontally for the dynamic incoming traffic.

[Inference endpoint for TensorFlow](https://docs.aws.amazon.com/deep-learning-containers/latest/devguide/deep-learning-containers-eks-tutorials-gpu-inference.html#deep-learning-containers-eks-tutorials-gpu-inference-tf)

[Inference endpoint for PyTorch](https://docs.aws.amazon.com/deep-learning-containers/latest/devguide/deep-learning-containers-eks-tutorials-gpu-inference.html#deep-learning-containers-eks-tutorials-gpu-inference-pytorch)

[Elastic Inference (EI) accelerator](https://github.com/aws-samples/amazon-elastic-inference-eks)

#### Related links

[Creating an EKS cluster](https://docs.aws.amazon.com/eks/latest/userguide/create-cluster.html)

[TF model serving with Kubernetes and Amazon Elastic Inference](https://aws.amazon.com/blogs/machine-learning/optimizing-tensorflow-model-serving-with-kubernetes-and-amazon-elastic-inference/)

[PyTorch model archive](https://github.com/pytorch/serve/blob/master/model-archiver) - Package all models into a single package and create PyTorch serving similar to [TensorFlow serving](https://www.tensorflow.org/tfx/guide/serving).
