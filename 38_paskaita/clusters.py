import numpy as np
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt

masyvas = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(masyvas.shape)
print(masyvas)

masyvas2 = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
print(masyvas2.shape)
print(masyvas2)

masyvas3 = np.array([[[5, 2], [3, 4]],[[6, 5], [5, 8]]])
print(masyvas3)
print(masyvas3.shape)


X = np.array([[5, 3],
              [10, 15],
              [15, 12],
              [24, 10],
              [30, 30],
              [85, 70],
              [71, 80],
              [60, 78],
              [70, 55],
              [80, 91],])

# model = AgglomerativeClustering(n_clusters=2, linkage='ward')

# model.fit(X)

# labels = model.labels_
# plt.scatter(X[:,0], X[:,1], c=labels, cmap='rainbow')
# plt.title("Pirmasis clustering grafikas")
# plt.grid()
# plt.show()

X = np.random.rand(150,2) * 50
agg_cluster = AgglomerativeClustering(n_clusters=4, linkage= 'complete')
agg_cluster.fit(X)
labels = agg_cluster.labels_
plt.scatter(X[:,0], X[:,1], c=labels, cmap='rainbow')
plt.title("4 klasteriai complete jungimo metodas")
plt.show()