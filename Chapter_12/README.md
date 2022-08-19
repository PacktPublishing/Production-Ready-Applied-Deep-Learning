<<<<<<< HEAD
### Monitoring Deep Learning Endpoints in Production


 
=======
# Monitoring Deep Learning Endpoints in Production

In this chapter, we discuss popular tools for monitoring DL models and alerting. 

Common tools for monitoring are

* [Prometheus](https://prometheus.io/)
* [CloudWatch](https://aws.amazon.com/cloudwatch/)
* [Grafana](https://grafana.com/)
* [DataDog](https://www.datadoghq.com/)
* [SageMaker Clarify](https://aws.amazon.com/sagemaker/clarify/)

Popular tools for alerting include

* [PagerDuty](https://www.pagerduty.com/)
* [DynaTrace](https://www.dynatrace.com/)

Out of the various tools we introduce, we will get our hands dirty with CloudWatch metrics logging.
* [Notebook showing logging metrics into CloudWatch](./cloudwatch_log_metrics.ipynb)

Other useful resources
* [CloudWatch concepts](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html)
* [Monitoring a SageMaker endpoint using CloudWatch](https://docs.aws.amazon.com/sagemaker/latest/dg/monitoring-cloudwatch.html)
* [Monitoring a SageMaker training jobs using CloudWatch Metrics](https://docs.aws.amazon.com/sagemaker/latest/dg/training-metrics.html)
* [Enabling EKS control plane logging metrics to CloudWatch](https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html)
* [Monitoring EKS API metrics](https://aws.github.io/aws-eks-best-practices/reliability/docs/controlplane/)
* [TensorFlow Serving](https://github.com/aws/sagemaker-tensorflow-serving-container#getting-started)
    - Python `print` statements from TF serving output function `output_handler` will log it to CloudWatch
      as shown in the [README](https://github.com/aws/sagemaker-tensorflow-serving-container#prepost-processing).
* [CloudWatch Alarm for setting up rules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html)
  
