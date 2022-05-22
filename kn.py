import pandas as pd
import numpy as np

dataset= pd.read_csv('3.kdata.csv')

x=dataset.iloc[:,:-1]
y=dataset.iloc[:,2].values
x,y

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
x=x.apply(le.fit_transform)

#genral knn
from sklearn.neighbors import KNeighborsClassifier
classifier=KNeighborsClassifier(n_neighbors=3)
classifier.fit(x,y)

x_test=np.array([1,0])
y_pred=classifier.predict([x_test])
print("General KNN", y_pred)

#dist weighted knn
classifier=KNeighborsClassifier(n_neighbors=3,weights='distance')
classifier.fit(x,y)
x_test=np.array([1,0])
y_pred=classifier.predict([x_test])

print("Distance weighted KNN", y_pred)
