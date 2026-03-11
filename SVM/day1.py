from sklearn.svm import SVC
import pandas as pd
data={
    "age":[45,50,38,60,48,55,35,62],
    "cholesterol":[230,250,180,300,240,270,190,310],
    "blood_pressure":[140,150,120,160,145,155,118,170],
    "heart_attack":[1,1,0,1,1,1,0,1]
}

df=pd.DataFrame(data)

x=df[["age","cholesterol","blood_pressure"]]
y=df["heart_attack"]


model=SVC(kernel="linear") #

model.fit(x,y) #

new_data=[[45,245,150]]

p=model.predict(new_data)

if p>=1:
    print("high risk of attack")
else:
    print("low risk of attack")    


     # model :-- fast, accuracy_score, large amount of data yr proper ,interpretion,performance
     svm
     knn
     byes
     xgboost
     etc..

     kaggle
     large dataset



     