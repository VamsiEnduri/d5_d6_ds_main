# import pandas as pd 
# from sklearn.preprocessing import LabelEncoder
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.metrics import accuracy_score
# data = {
#     "Outlook": ["Sunny","Sunny","Overcast","Rain","Rain",
#                 "Rain","Overcast","Sunny","Sunny","Rain"],
    
#     "Temperature": ["Hot","Hot","Hot","Mild","Cool",
#                     "Cool","Cool","Mild","Cool","Mild"],
    
#     "Humidity": ["High","High","High","High","Normal",
#                  "Normal","Normal","High","Normal","Normal"],
    
#     "Wind": ["Weak","Strong","Weak","Weak","Weak",
#              "Strong","Strong","Weak","Weak","Weak"],
    
#     "Play": ["No","No","Yes","Yes","Yes",
#              "No","Yes","No","Yes","Yes"]
# }

# df=pd.DataFrame(data)

# print(df,"before")

# le=LabelEncoder()

# for i in df.columns:
#     df[i]=le.fit_transform(df[i])

# print(df,"after")    


# x=df.drop("Play",axis=1)
# print(x)
# y=df["Play"]


# model=DecisionTreeClassifier(criterion="gini")
# model.fit(x,y)

# predicted_output=model.predict(x)


# print(accuracy_score(y,predicted_output),"ac_score")

# for i,j in zip(df.columns,model.feature_importances_):
#     print(f"{i} :-- {j}")




# # features = ["Outlook", "Humidity", "Wind"]
# # importance = [0.58, 0.32, 0.10]

# # for f, i in zip(features, importance):
# #     print(f"{f} : {i}")



import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Your dataset
data = {
    "Outlook": ["Sunny","Sunny","Overcast","Rain","Rain",
                "Rain","Overcast","Sunny","Sunny","Rain"],
    
    "Temperature": ["Hot","Hot","Hot","Mild","Cool",
                    "Cool","Cool","Mild","Cool","Mild"],
    
    "Humidity": ["High","High","High","High","Normal",
                 "Normal","Normal","High","Normal","Normal"],
    
    "Wind": ["Weak","Strong","Weak","Weak","Weak",
             "Strong","Strong","Weak","Weak","Weak"],
    
    "Play": ["No","No","Yes","Yes","Yes",
             "No","Yes","No","Yes","Yes"]
}

df = pd.DataFrame(data)
print(df, "\nBefore encoding\n")

# Encode categorical variables
le = LabelEncoder()
for col in df.columns:
    df[col] = le.fit_transform(df[col])

print(df, "\nAfter encoding\n")

# Features and target
X = df.drop("Play", axis=1)
y = df["Play"]

# Train Decision Tree
model = DecisionTreeClassifier(criterion="entropy", random_state=42)
model.fit(X, y)

# Predictions
pred = model.predict(X)
print("Accuracy:", accuracy_score(y, pred))

# Feature importances
for feature, importance in zip(X.columns, model.feature_importances_):
    print(f"{feature} : {importance:.4f}")

# Plot the tree
plt.figure(figsize=(12,8))
plot_tree(model, 
          feature_names=X.columns, 
          class_names=["No", "Yes"], 
          filled=True, 
          rounded=True,
          fontsize=12)
plt.show()