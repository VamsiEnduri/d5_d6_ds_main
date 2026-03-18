import pandas as pd 
import numpy as np   
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier

n=1000
age=np.random.randint(22,60,n)
bp=np.random.randint(120,200,n)
ch=np.random.randint(170,300,n)
excersise_level=np.random.randint(0,7,n)


risk=(bp>150).astype(int) + (ch>200).astype(int) - (excersise_level>3).astype(int)
print(risk,"risk")

risk=(risk>=1).astype(int)

print(risk,"16")

df=pd.DataFrame(
   { "age":age,
    "bp":bp,
    "ch":ch,
    "excersise_level":excersise_level,
    "risk":risk}
)

x=df.drop("risk",axis=1) #f
y=df["risk"] #t

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)


model=GradientBoostingClassifier(n_estimators=200,max_depth=2,learning_rate=0.1,subsample=0.8)

model.fit(x_train,y_train)

print(model.score(x_train,y_train))
print(model.score(x_test,y_test))


new_data=[[35,120,160,6]]

p=model.predict(new_data)

print(p[0],"result")







# - xgboost





import numpy as np
import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

np.random.seed(42)

n = 1000

# Features
age = np.random.randint(20, 80, n)
bp = np.random.randint(80, 180, n)
cholesterol = np.random.randint(150, 300, n)
exercise = np.random.randint(0, 5, n)

# Target (simple logic)
risk = ((age > 50) & (bp > 140) | (cholesterol > 240)).astype(int)

# DataFrame
df = pd.DataFrame({
    "age": age,
    "bp": bp,
    "cholesterol": cholesterol,
    "exercise": exercise,
    "risk": risk
})

# Split
X = df.drop("risk", axis=1)
y = df["risk"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model
model = XGBClassifier(
    n_estimators=300,
    learning_rate=0.05,
    max_depth=3,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))