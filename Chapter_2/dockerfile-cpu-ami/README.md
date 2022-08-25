### How to Create Docker Image (CPU) for Data Science

Note. The image is taken from Amazon Machine Image (AMI)

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

