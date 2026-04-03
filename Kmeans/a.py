import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.cluster  import KMeans
# 🔵 Low customers
low_income = np.random.randint(10000, 40000, 300) #values [10000,23000,3200000]
low_spending = np.random.randint(1, 40, 300) # 1-40 


# 🟢 Medium customers
mid_income = np.random.randint(40000, 70000, 400)
mid_spending = np.random.randint(40, 70, 400) #40-70


# 🔴 High customers
high_income = np.random.randint(70000, 100000, 300)
high_spending = np.random.randint(70, 100, 300) #70-100

income=np.concatenate([low_income,mid_income,high_income])
spending=np.concatenate([low_spending,mid_spending,high_spending])


df=pd.DataFrame(
    {
        "Income":income,
        "Spending":spending
    }
)

x=df[["Income","Spending"]]

# k:-- no of clusters 
# means :-- avg

ins=[]

for i in range(1,7):
    model=KMeans(n_clusters=i)
    model.fit(x)
    ins.append(model.inertia_)


print(ins,"ins")
print(df.head(5))

plt.plot(range(1,7),ins,marker="o")
plt.xlabel("no of k")
plt.ylabel("inertia")
plt.title("elbow point finder")
plt.show()


model=KMeans(n_clusters=3) # nc=3

df["target"]=model.fit_predict(x)


cen = model.cluster_centers_


plt.figure()

for i in range(3): #i=0
    cluster_data=df[df["target"] == i] #  0 == 0 
    plt.scatter(cluster_data["Income"],cluster_data["Spending"],label=f"Cluster {i}")

plt.scatter(cen[:,0],cen[:,1],marker="X")

plt.xlabel("Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation")
plt.legend()
plt.show()

