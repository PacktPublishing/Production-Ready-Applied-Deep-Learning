# Revealing the secret of DL models

The first topic of this chapter is on obtaining the best performing model using hyperparameter tuning.

As hyperparameter tuning plays an important role in ML projects, there exist many libraries that are designed to simplify the process. The popular ones are as follows:
*	[Scikit-Optimize](https://scikit-optimize.github.io/stable/index.html)
*	[Optuna](https://optuna.org)
*	[HyperOpt](http://hyperopt.github.io/hyperopt)
*	[Ray Tune](https://docs.ray.io/en/latest/tune/index.html)
*	[BayesianOptimization](https://github.com/fmfn/BayesianOptimization)
*	[Metric Optimization Engine (MOE)](https://github.com/Yelp/MOE)
*	[Spearmint](https://github.com/HIPS/Spearmint)
*	[GPyOpt](https://github.com/SheffieldML/GPyOpt)
*	[SigOpt](https://sigopt.com/)
*	[FLAML](https://github.com/microsoft/FLAML)
*	[Dragonfly](https://github.com/dragonfly/dragonfly)
*	[HpBandSter](https://github.com/automl/HpBandSter)
*	[Nevergrad](https://github.com/facebookresearch/nevergrad)
*	[ZOOpt](https://github.com/polixir/ZOOpt)
*	[HEBO](https://github.com/huawei-noah/HEBO/tree/master/HEBO)
*	[Sagemaker](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-how-it-works.html)

Among the various tools, Scikit-Optimize would be a good starting
point if you are not familiar with hyperparameter tuning. If your
pipeline is built with SageMaker, SageMaker Hyperparameter Tuning
would be a sensible choice.

The next topic is on understanding the behavior of the model with Explainable AI. The key techniques we introduce are Permutation Importance, SHAP, and LIME. The details can be found in the book as well as in [this notebook](./Secret_of_DL_models.ipynb)
