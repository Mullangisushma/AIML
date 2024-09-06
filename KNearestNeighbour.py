from sklearn.datasets import load_iris



iris=load_iris()
x=iris.data
y=iris.target
print(x[:5],y[:5])

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)
print(iris.data.shape)
print(len(x_train))
print(len(y_test))

from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=1)
knn.fit(x_train,y_train)
y_pred=knn.predict(x_test)

from sklearn import metrics
print("Accuracy:",metrics.accuracy_score(y_test,y_pred))
ytest=[iris.target_names[i] for i in y_test]
ypred=[iris.target_names[i] for i in y_pred]
print("sno    predicted    actual")
for i in range(len(ypred)):
    print(i,"    ",ytest[i],"    ",ypred[i])
