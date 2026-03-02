# from data import data
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle
import pandas as pd
# from sklearn.metrics import r2_score

data = pd.DataFrame({
    "Size(sqft)": [1200, 1500, 800, 2000, 1100, 1800, 950, 1600, 2200, 1400],
    "Bedrooms": [3, 4, 2, 5, 3, 4, 2, 3, 5, 3],
    "Age": [5, 2, 10, 1, 8, 3, 12, 4, 1, 6],
    "LocationScore": [8, 9, 6, 10, 7, 9, 5, 8, 10, 7],
    "Price": [50000, 70000, 30000, 100000, 45000, 75000, 28000, 68000, 120000, 60000]
})

# 
x=data[["Size(sqft)"]] #features
y=data["Price"]

# import matplotlib.pyplot as pt 

# pt.scatter(x,y)
# pt.xlabel("sizeSqrfreet")
# pt.ylabel("Price")
# pt.title("srft vs price")
# pt.show()

x_train,x_test,y_train,y_test=train_test_split(
    x,y,test_size=0.25
)


model=LinearRegression()
model.fit(x_train,y_train)
print(model.score(x_train,y_train))
print(model.score(x_test,y_test))

with open("lr.pkl","wb") as f:
    pickle.dump(model,f)

