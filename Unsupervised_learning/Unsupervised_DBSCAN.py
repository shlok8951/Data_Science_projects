import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons
from sklearn.cluster import DBSCAN,KMeans
X,y_true  = make_moons(n_samples=500,noise=0.05,random_state=42)
df = pd.DataFrame(X,columns=["f1","f2"])

scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

kmeans = KMeans(n_clusters=2,random_state=42)
kmeans_labels = kmeans.fit_predict(X_scaled)
df["kMean_label"]=kmeans_labels

sns.scatterplot(x=df["f1"],y = df["f2"],hue=df["kMean_label"],palette="tab10")
plt.show()

dbscan = DBSCAN(eps=0.3,min_samples=5)
dbscan_label = dbscan.fit_predict(X_scaled)
df["dbscale_label"]=dbscan_label

sns.scatterplot(x=df["f1"],y = df["f2"],hue=df["dbscale_label"],palette="tab10")
plt.show()
