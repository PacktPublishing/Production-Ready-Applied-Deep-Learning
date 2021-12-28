import plotly.express as px
from sklearn.decomposition import PCA
# Download iris dataset
df = px.data.iris()
# Features
features = ["sepal_width", "sepal_length", "petal_width", "petal_length"]
# create PCA instances
pca = PCA()
comp = pca.fit_transform(df[features])
labels = {
    str(i): f"PC {i+1} ({var:.1f}%)"
    for i, var in enumerate(pca.explained_variance_ratio_ * 100)
}
# Scatter plot
fgr = px.scatter_matrix(
    comp,  # components
    labels=labels,
    dimensions=range(2),  # number of principal components
    color=df["species"]
)

fgr.update_traces(diagonal_visible=False)
fgr.show()
