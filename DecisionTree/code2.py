# import pandas as pd 
# from sklearn.preprocessing import LabelEncoder
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import train_test_split
# data = [
# # Age, Income, Education, CreditScore, PropertyArea, LoanAmount, LoanApproved
# [25,30000,"Graduate",620,"Urban",15000,0],
# [45,85000,"Postgraduate",720,"Urban",20000,1],
# [35,65000,"Graduate",690,"Semiurban",18000,1],
# [28,40000,"Graduate",640,"Rural",12000,0],
# [50,90000,"Postgraduate",750,"Urban",25000,1],
# [23,28000,"Undergraduate",610,"Rural",10000,0],
# [40,70000,"Graduate",710,"Semiurban",20000,1],
# [30,50000,"Graduate",660,"Urban",15000,0],
# [32,55000,"Undergraduate",670,"Semiurban",16000,1],
# [27,38000,"Graduate",630,"Rural",11000,0]
# ]

# df=pd.DataFrame(data,columns=["Age","Income","Graduation","CibilScore","Area","LoanAmount","Approval"])

# # print(df,"dataframe")

# LE=LabelEncoder()
# df["Graduation"]=LE.fit_transform(df["Graduation"])
# df["Area"]=LE.fit_transform(df["Area"])


# x=df.drop("Approval",axis=1) # features
# y=df["Approval"] # target

# x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=42)

# model=DecisionTreeClassifier(max_depth=5,min_samples_split=5)
# model.fit(x_train,y_train)

# trScore=model.score(x_train,y_train)
# teScore=model.score(x_test,y_test)

# print(df,"dataframe")

# print(trScore,"trScore") # 1
# print(teScore,"teScore") # 0.88 overfitting

# pred=model.predict([[27,85000,0,710,0,100000]])
# print(pred)

# #  tree depth control






import pandas as pd 
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeRegressor
from  sklearn.metrics  import r2_score
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

df=pd.DataFrame(data,columns=["Age","Income","Graduation","CibilScore","Area","LoanAmount","Approval"])

# print(df,"dataframe")

LE=LabelEncoder()
df["Graduation"]=LE.fit_transform(df["Graduation"])
df["Area"]=LE.fit_transform(df["Area"])


x=df.drop("Approval",axis=1) # features
y=df["Approval"] # target

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=42)

model=DecisionTreeRegressor()
model.fit(x_train,y_train)

trScore=model.score(x_train,y_train)
teScore=model.score(x_test,y_test)

print(df,"dataframe")

print(trScore,"trScore") # 1
print(teScore,"teScore") # 0.88 overfitting

pred=model.predict(x)

r2__=r2_score(y,pred)
print(pred,"pred value")
print(r2__,"r2score value")


