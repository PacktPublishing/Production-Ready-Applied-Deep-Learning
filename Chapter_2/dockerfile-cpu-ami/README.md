### How to Create Docker Image (CPU) for Data Science

Note. The image is taken from Amazon Machine Image (AMI)

* Please note that you will need [aws cli version 2](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

* To install and start docker image, please run the following commands

```
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 763104351884.dkr.ecr.us-east-1.amazonaws.com
docker build --no-cache -t aws-jupyter . 
docker run -it -p 8888:8888 -v ${PWD}:${PWD} aws-jupyter:latest
```
