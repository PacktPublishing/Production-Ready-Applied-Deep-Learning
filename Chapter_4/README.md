# Experiments tracking, model management, and dataset versioning

*	Weights & Biases [https://wandb.ai/site/experiment-tracking]
*	MLflow [https://mlflow.org/docs/latest/tracking.html]                                                       
*	SageMaker Studio [https://aws.amazon.com/sagemaker/studio/]
*	Kubeflow [https://www.kubeflow.org/]
*	Neptune [https://neptune.ai/product]
*	Comet [https://www.comet.ml/site/data-scientists/]
*	Polyaxon [https://polyaxon.com/]
*	Valohai [https://valohai.com/product/]

# Setting up W&B
```
pip install wandb
wandb login
```

# Examples 

[W&B.ipynb](W&B.ipynb)

# Setting up MLflow
```
pip install mlflow
```
To start UI locally simply type:
```
mlflow ui
```
and in your webbrowser type http address that is displayed in the row "Listening at: " 
```
[INFO] Listening at: http://127.0.0.1:5000
```
if you are doing this for a first time, you will see UI with default page without any experiments. 
<p align="center">
  <img src="mlflow_ui.png" width="80%">
</p>
A few examples of basics of experiment tracking with MLflow are presented [here](mlflow.ipynb) 

# Setting up DVC
```
pip install dvc
```
Example of how to set DVC and use it with MLflow can be found [here](dvc_mlflow.ipynb)
