### How to Create Docker Image (CPU) for Data Science

Using docker, you can create a snapshot of your working environment including the underlying version of OS. Altogether, docker enables you to separate your applications from your infrastructure so you can deliver your software quickly. Installing docker can be achieved by following [this instructions](https://www.docker.com/get-started).

#### Purge dangling images
  `docker system prune`

#### Build the image 
  `docker build --no-cache -t py3-jupyter .`
    
#### Run build
  `docker run -it -p 8888:8888 -v ${PWD}/:/home/jovyan py3-jupyter:latest`

  In the console of last docker run command above, it will show the link with a credential `http://127.0.0.1:8888/?token=....`.
  Just clicking on it will open the Jupyter endpoint in the default browser.
  Files saved under work directory will be visible on current directory.
