import numpy as np 
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier
rows=1000
data={
    "age":np.random.randint(21,60,rows),
    "income":np.random.randint(20000,150000,rows),
    "credit_score":np.random.randint(500,850,rows),
    "loan_amount":np.random.randint(300000,1500000,rows),
    "work_experience":np.random.randint(2,15,rows),
    "tenure":np.random.choice([5,7,9,11,13],rows),
    "existing_loans":np.random.randint(0,4,rows)
}

df=pd.DataFrame(data)

df["loan_approved"]=( (df["income"] >45000)  & df["credit_score"]>650) & (df["existing_loans"]<3) & (df["work_experience"]>2).astype(int)

# print(df["loan_approved"])

x=df.drop("loan_approved",axis=1) #features 
y=df["loan_approved"] #target

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=42)


model=RandomForestClassifier(n_estimators=200,max_depth=5,min_samples_split=5)


model.fit(x_train,y_train)

print("train",model.score(x_train,y_train))
print("test",model.score(x_test,y_test))

f_importance=model.feature_importances_

df1=pd.DataFrame({
    "Feature":x.columns,
    "importance":f_importance
})

f_i_table=df1.sort_values(by="importance",ascending=False)
print(f_i_table)

new_data=[[22,55000,650,500000,1,7,0]]
p=model.predict(new_data)
print(p)


