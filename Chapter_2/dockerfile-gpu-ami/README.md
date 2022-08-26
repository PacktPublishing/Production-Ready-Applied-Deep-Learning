### How to Create Docker Image (GPU) for Data Science

Note: The image is taken from Amazon Machine Image (AMI)

* First of all, ensure that your GPU environment is correctly set up. You need to have appropriate [nvidia drivers](https://www.nvidia.com/download/index.aspx) and [cuda with version greater than 11.2](https://developer.nvidia.com/cuda-11.2.0-download-archive)

* For GPU environment, you need to install [nvidia-docker2](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html)

* Please note that you will need [aws cli version 2](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

* To install and start docker image, please run the following commands

```
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 763104351884.dkr.ecr.us-east-1.amazonaws.com
docker build --no-cache -t aws-jupyter-gpu . 
docker run --gpus=all -it -p 8888:8888 -v ${PWD}/:${PWD} aws-jupyter-gpu:latest
```
