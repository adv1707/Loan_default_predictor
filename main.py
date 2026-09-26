import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression,SGDClassifier
from sklearn.metrics import confusion_matrix,accuracy_score,precision_score,f1_score,recall_score


#Importing data and removing useless column
data = pd.read_csv(r"loan.csv")
data = data.drop(columns=["LoanID"])


#Creating train test split
X=data.drop(columns=["Default"])
Y = data["Default"]
x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.2,random_state=17)


#Creating functions and model
scaler = StandardScaler()
onehotencoder = OneHotEncoder(sparse_output=False,drop="first")
model = LogisticRegression(l1_ratio=1,solver="liblinear",class_weight="balanced",C=0.0001)


#Creating Columntransformer
arr = [i for i in range(24)]
c1 = ColumnTransformer(transformers=[
    ("Onehotencoding",onehotencoder,[9,10,11,12,13,14,15])
],remainder='passthrough')

c2 = ColumnTransformer(transformers=[
    ("scaling",scaler,arr)
],remainder="passthrough")


#Making pipeline
mainpipe = Pipeline([
    ("Onehotencoding",c1),
    ("standard_scaling",c2),
    ("model",model)
])


#Fitting data and calculating different metrics
mainpipe.fit(x_train,y_train)
y_pred = mainpipe.predict(x_test)

accuracy = accuracy_score(y_test,y_pred)
precision = precision_score(y_test,y_pred)
recall = recall_score(y_test,y_pred)
f1 = f1_score(y_test,y_pred)
confusion = confusion_matrix(y_test,y_pred)



