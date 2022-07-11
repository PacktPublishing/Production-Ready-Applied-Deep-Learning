# Chapter 7

In this chapter we cover the following main topics:
*	Obtaining the best performing model using hyperparameter tuning
*	Understanding the behavior of the model with Explainable AI

As hyperparameter tuning plays an important role in ML projects, there exist many libraries that are designed to simplify the process. The popular ones are as follows:
*	Scikit-Optimize - https://scikit-optimize.github.io/stable/index.html
*	Optuna - https://optuna.org
*	HyperOpt - http://hyperopt.github.io/hyperopt
*	Ray Tune - https://docs.ray.io/en/latest/tune/index.html
*	BayesianOptimization - https://github.com/fmfn/BayesianOptimization
*	Metric Optimization Engine (MOE) - https://github.com/Yelp/MOE
*	Spearmint - https://github.com/HIPS/Spearmint
*	GPyOpt - https://github.com/SheffieldML/GPyOpt
*	SigOpt - https://sigopt.com/
*	FLAML - https://github.com/microsoft/FLAML
*	Dragonfly - https://github.com/dragonfly/dragonfly
*	HpBandSter - https://github.com/automl/HpBandSter
*	Nevergrad - https://github.com/facebookresearch/nevergrad
*	ZOOpt - https://github.com/polixir/ZOOpt
*	HEBO - https://github.com/huawei-noah/HEBO/tree/master/HEBO
*	Sagemaker - https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-how-it-works.html

As part of Ray, a framework developed for scaling python workloads across machines, Ray Tune is designed for experiment execution and hyperparameter tuning at scale.

First, we will look at the basics of Ray Tune.
```python
from ray import tune
def tr_function(conf):
    num_iterations = conf["num_it"]
    for i in range(num_iterations):
        … // training logic
        tune.report(mean_accuracy=acc)

tune.run(
    run_or_experiment = tr_function
    conf={ “num_it”: tune.grid_search([10, 20, 30, 40])})
```
want to find more? don't forget to buy our book. 

Next, part is focused on understanding the behavior of the model with Explainable AI.

[Permutation Importance, SHAP, LIME](Secret_of_DL_models.ipynb)
