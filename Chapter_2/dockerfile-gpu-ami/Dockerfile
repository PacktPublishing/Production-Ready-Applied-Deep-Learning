# This docker file is to build GPU based machine with necessary Data Science Library (TensorFlow, PyTorch etc)
FROM 763104351884.dkr.ecr.us-east-1.amazonaws.com/tensorflow-training:2.9.1-gpu-py39-cu112-ubuntu20.04-ec2

RUN python -m pip install --upgrade pip
RUN pip install --upgrade protobuf

#
RUN pip install numpy scipy pandas

RUN pip install matplotlib seaborn

# Install required packages to enable the SageMaker Python SDK and the smdebug library
RUN pip install sagemaker sagemaker-training
RUN pip install smdebug
RUN pip install tensorflow-gpu
RUN pip install torch torchvision torchaudio pytorch-lightning
#
RUN pip install tensorflow_model_optimization
RUN pip install mlflow dvc wandb

RUN pip install tqdm pandasql
#
RUN pip install notebook jupyterhub jupyterlab

#
RUN pip install ipywidgets widgetsnbextension pandas-profiling

CMD ["jupyter nbextension enable --py widgetsnbextension"]

#
RUN pip install ipykernel
RUN python -m ipykernel install --user

#
RUN pip install pyarrow

#
RUN pip install scikit-learn --upgrade

#
RUN pip install ray

#
RUN pip install onnx onnxruntime tf2onnx

#
RUN pip install shap eli5 lime

#
RUN pip install jupyterlab-nvdashboard

# java, spark, hadoop
ARG spark_version="3.1.2"
ARG hadoop_version="3.2"
ARG spark_checksum="2385CB772F21B014CE2ABD6B8F5E815721580D6E8BC42A26D70BBCDDA8D303D886A6F12B36D40F6971B5547B70FAE62B5A96146F0421CB93D4E51491308EF5D5"
ARG openjdk_version="11"

ENV APACHE_SPARK_VERSION="${spark_version}" \
    HADOOP_VERSION="${hadoop_version}"

RUN apt-get update --yes && \
    apt-get install --yes --no-install-recommends \
    "openjdk-${openjdk_version}-jre-headless" \
    ca-certificates-java && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Spark installation
WORKDIR /tmp
RUN wget -q "https://archive.apache.org/dist/spark/spark-${APACHE_SPARK_VERSION}/spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" && \
    echo "${spark_checksum} *spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" | sha512sum -c - && \
    tar xzf "spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" -C /usr/local --owner root --group root --no-same-owner && \
    rm "spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz"

WORKDIR /usr/local

# Configure Spark
ENV SPARK_HOME=/usr/local/spark
ENV SPARK_OPTS="--driver-java-options=-Xms1024M --driver-java-options=-Xmx4096M --driver-java-options=-Dlog4j.logLevel=info" \
    PATH="${PATH}:${SPARK_HOME}/bin"

RUN ln -s "spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}" spark && \
    # Add a link in the before_notebook hook in order to source automatically PYTHONPATH
    mkdir -p /usr/local/bin/before-notebook.d && \
    ln -s "${SPARK_HOME}/sbin/spark-config.sh" /usr/local/bin/before-notebook.d/spark-config.sh

# Fix Spark installation for Java 11 and Apache Arrow library
# see: https://github.com/apache/spark/pull/27356, https://spark.apache.org/docs/latest/#downloading
RUN cp -p "${SPARK_HOME}/conf/spark-defaults.conf.template" "${SPARK_HOME}/conf/spark-defaults.conf" && \
    echo 'spark.driver.extraJavaOptions -Dio.netty.tryReflectionSetAccessible=true' >> "${SPARK_HOME}/conf/spark-defaults.conf" && \
    echo 'spark.executor.extraJavaOptions -Dio.netty.tryReflectionSetAccessible=true' >> "${SPARK_HOME}/conf/spark-defaults.conf"


# pyspark
RUN pip install --upgrade findspark
# pyspark
RUN pip install --upgrade pyspark==3.1.2

#
ENV PYTHONUNBUFFERED=TRUE

# Define entrypoint
CMD ["jupyter", "notebook", "--ip='*'", "--port=8888", "--no-browser", "--allow-root"]
EXPOSE 8888
