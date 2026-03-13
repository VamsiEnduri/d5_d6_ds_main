import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt



data = {
    "area":[800,900,1000,1100,1200,1300,1400,1500],
    "bedrooms":[1,2,2,3,3,3,4,4],
    "price":[150000,180000,200000,230000,260000,280000,300000,320000]
}

df = pd.DataFrame(data)

x = df[["area","bedrooms"]]
y = df["price"]

# data = {
#     "age":[22,25,30,35,40,45,50,55],
#     "salary":[20000,25000,30000,35000,60000,65000,70000,75000],
#     "loan":[0,0,0,0,1,1,1,1]
# }

# df=pd.DataFrame(data)

# x=df[["age","salary"]]
# y=df["loan"]


x_train,x_test,y_train,y_test=train_test_split(
    x,y,test_size=0.25,random_state=42
)


f_scaler=StandardScaler()

x_train_f_scaler=f_scaler.fit_transform(x_train)

model=KNeighborsRegressor(n_neighbors=4)
model.fit(x_train_f_scaler,y_train)


new_data=[[1250,3]]

new_data_f_scaler=f_scaler.transform(new_data)

p=model.predict(new_data_f_scaler)

plt.scatter(df["area"],df["price"],c=y)

plt.scatter(new_data[0][0],p[0],color="yellow",marker="*",s=250)

plt.xlabel("area")
plt.ylabel("price")

plt.title("area vs price knn")

plt.show()

print(p)






