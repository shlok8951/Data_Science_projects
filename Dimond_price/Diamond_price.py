
#------------------------------------ Dimond Price prediction------------------------

import pandas as pd
import seaborn as sns
import pickle as pkl
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score,accuracy_score
from sklearn.ensemble import RandomForestRegressor



df = pd.read_csv("Diamonds Prices2022.csv")  #read csv file


#EDA

print(df.shape)
print(df.head()) 
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.duplicated().sum())

df.drop("serial_no",axis=1,inplace=True)

numeric_col = ["carat","depth","table", "price","x","y","z"]
category_col = ["cut","color","clarity"]

for col in numeric_col:
    sns.histplot(x=df[col],kde=True,bins=20)
    plt.show()

for col in category_col:
    sns.countplot(x=df[col])
    plt.show()

print(df["cut"].value_counts())
print(df["color"].value_counts())
print(df['clarity'].value_counts())

#LABEL ENCODING
le = LabelEncoder()
df["cut"] = le.fit_transform(df["cut"])
df["color"] = le.fit_transform(df["color"])
df["clarity"] = le.fit_transform(df["clarity"])

#ONEHOTENCODING
# df = pd.get_dummies(df,columns=["color","clarity","cut"])
# df = df.astype(int)
# print(df.head())

sns.heatmap(df.corr(numeric_only=True),annot=True)   #Graphihcal reparsentation of Corelation
plt.show()   

corelation  = df.corr(numeric_only=True)["price"].sort_values(ascending=False)
print(corelation)

x = df[["clarity",'carat' ,"depth", 'x','y','z',"table","color"]]
y = df['price']


x_train ,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

#RandomForest Regression 
model = RandomForestRegressor(random_state=42)
model.fit(x_train,y_train)

predictions =  model.predict(x_test)

mae = mean_absolute_error(y_test,predictions)
print("Mean absulat error : ",mae)

mse = mean_squared_error(y_test,predictions)
print("Mean Square error : ",mse)

r2 = r2_score(y_test,predictions)
print("R2 Score : ",r2)
n = x_test.shape[0]
p=x_test.shape[1]
adj_r2 = 1 - ((1-r2)*(n-1))/(n-p-1)
print("Adjusted_r2 : ", adj_r2)

error  = abs(y_test-predictions)

sns.scatterplot(x=y_test, y=predictions,hue=error,palette="rainbow")

plt.plot([y_test.min(), y_test.max()],
         [y_test.min(), y_test.max()],
         color="red", linewidth=2)

plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted (Diamond Price)")
plt.show()

# user Prediction
caret_ = float(input("Enter the caret : "))
table_ = float(input("Enter the table Value : "))
x_ = float(input("Enter the x Value : "))
y_ = float(input("Enter the y Value : "))
z_ = float(input("Enter the z Value : "))
clarity_ = input("Enter the clarity : ")
color_ = input("Enter the color : ")
depth_ = float(input("Enter the depth : "))

data = pd.DataFrame({
    "clarity":[clarity_],
    'carat':[caret_],
    'depth':[depth_],
    'x':[x_],
    'y':[y_],
    'z':[z_],
    'table':[table_],
    "color":[color_]    
})

data["color"] = le.fit_transform(data["color"])
data["clarity"] = le.fit_transform(data["clarity"])

# data = pd.get_dummies(data,columns=["color,clarity"])

predicts = model.predict(data)
print(predicts)
