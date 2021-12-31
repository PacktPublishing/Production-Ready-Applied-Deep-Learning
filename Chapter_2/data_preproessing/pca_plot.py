import plotly.express as px
from sklearn.decomposition import PCA
# Set number of principal components to plot.
# Maximum can be length of variable "features" (i.e., 4)
NUM_OF_PRINCIPAL_COMPONENTS = 4
# Download iris dataset
df = px.data.iris()
# Features
features = ["sepal_width", "sepal_length", "petal_width", "petal_length"]
# create PCA instances
pca = PCA()
# fit features to get
principal_comp = pca.fit_transform(df[features])
# label for x and y axis
labels = {
    str(i): f"PC {i+1} ({exp_var_ratio:.2f}%)"
    for i, exp_var_ratio in enumerate(100 * pca.explained_variance_ratio_)
}
# Scatter plot
figure = px.scatter_matrix(
    principal_comp,  # components
    labels=labels,  # contains labels for x and y axis
    dimensions=range(NUM_OF_PRINCIPAL_COMPONENTS),  # number of principal components
    color=df["species"]  # target feature
)
# make the diagonal invisible
figure.update_traces(diagonal_visible=False)
figure.show()
