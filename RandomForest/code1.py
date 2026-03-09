import pandas as pd 
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
data = [
# Age, Income, Education, CreditScore, PropertyArea, LoanAmount, LoanApproved
[25,30000,"Graduate",620,"Urban",15000,0],
[45,85000,"Postgraduate",720,"Urban",20000,1],
[35,65000,"Graduate",690,"Semiurban",18000,1],
[28,40000,"Graduate",640,"Rural",12000,0],
[50,90000,"Postgraduate",750,"Urban",25000,1],
[23,28000,"Undergraduate",610,"Rural",10000,0],
[40,70000,"Graduate",710,"Semiurban",20000,1],
[30,50000,"Graduate",660,"Urban",15000,0],
[32,55000,"Undergraduate",670,"Semiurban",16000,1],
[27,38000,"Graduate",630,"Rural",11000,0]
]

df=pd.DataFrame(data,columns=["Age", "Income", "Education", "CreditScore", "PropertyArea", "LoanAmount", "LoanApproved"])

le=LabelEncoder()

df["Education"]=le.fit_transform(df["Education"])
df["PropertyArea"]=le.fit_transform(df["PropertyArea"])

x=df.drop("LoanApproved",axis=1)
y = df["LoanApproved"]


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=42)

model=RandomForestClassifier(
    n_estimators=10,
    max_depth=5,
    min_samples_split=6,
    random_state=42
)
model.fit(x_train,y_train)

print("tra",model.score(x_train,y_train))
print("tes",model.score(x_test,y_test))


print(model.predict([[25,65000,1,720,1,40000]]))

