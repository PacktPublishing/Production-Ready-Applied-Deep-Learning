### Monitoring Deep Learning Endpoints in Production

[Notebook showing an example of metrics logging for CloudWatch](./cloudwatch_log_metrics.ipynb)

[TensorFlow Serving](https://github.com/aws/sagemaker-tensorflow-serving-container#getting-started)
    - Python `print` statements from TF serving output function `output_handler` will log it to CloudWatch.

[CloudWatch Alarm](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html)
  - Set up rules to detect changes in the metrics and alert. 