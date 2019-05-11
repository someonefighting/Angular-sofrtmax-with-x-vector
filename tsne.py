import numpy as np
import matplotlib
matplotlib.use('agg')
import pylab as plt
from sklearn import manifold, datasets

with open('feat', 'r') as f:
    Xl = [[float(num) for num in line.split(' ') if num.strip()] for line in f]
    #print(X)
with open('label', 'r') as f:
    yl = [[float(num) for num in line.split(' ') if num.strip()] for line in f]
    #print(y)
X = np.asarray(Xl)
y = np.asarray(yl)
tsne = manifold.TSNE(n_components=2, init='pca', random_state=501)
X_tsne = tsne.fit_transform(X)

print("Org data dimension is {}.Embedded data dimension is {}".format(X.shape[-1], X_tsne.shape[-1]))
x_min, x_max = X_tsne.min(0), X_tsne.max(0)
X_norm = (X_tsne - x_min) / (x_max - x_min)
fig2 = plt.figure(figsize=(8, 8))
for i in range(X_norm.shape[0]):
    plt.text(X_norm[i, 0], X_norm[i, 1],str(y[i][0]), color=plt.cm.Set1(int(y[i][0])),
                                             fontdict={'weight': 'bold', 'size': 9})
plt.xticks([])
plt.yticks([])
plt.show()
fig2.savefig('2.png')
