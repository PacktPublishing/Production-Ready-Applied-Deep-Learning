### How to Create Docker Image (GPU) for Data Science

Note: The image is taken from Amazon Machine Image (AMI)

* For GPU you need to have `nvidia-docker2` on your host machine.


* To build do

```
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 763104351884.dkr.ecr.us-east-1.amazonaws.com 
```

```
docker build --no-cache -t aws-jupyter . 
```

```
docker run --gpus=all -it -p 8888:8888 aws-jupyter:latest
```

