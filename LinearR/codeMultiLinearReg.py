from data import data
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle

# 
x=data[["Size(sqft)","Bedrooms","Age","LocationScore"]] #features
y=data["Price"]

x_train,x_test,y_train,t_test=train_test_split(
    x,y,test_size=0.25
)

model=LinearRegression()
model.fit(x_train,y_train)


with open("lr2.pkl","wb") as f:
    pickle.dump(model,f)

