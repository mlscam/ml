import pandas as pd
import numpy as np



data = [[2, 4,"neg"], [4,6,"neg"], [4,4,"pos"],[4,2,"neg"],[6,4,"neg"],[6,2,"pos"]]
  
# Create the pandas DataFrame
dataset = pd.DataFrame(data, columns = ['x', 'y','class'])

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
