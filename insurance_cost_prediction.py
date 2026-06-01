import pandas as pd
import seaborn as sb

df=pd.read_csv("insurance.csv")
df

sb.scatterplot(x=df["bmi"],y=df["charges"],hue=df["smoker"])

X=df.drop(columns=["charges","region"])
Y=df["charges"]

X["sex"]=X["sex"].map({"female":1,"male":0})
X["smoker"]=X["smoker"].map({"yes":1,"no":0})

X.head()

#Train Test Split

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.20,random_state=42)

x_train

x_test

from sklearn.linear_model import LinearRegression

model=LinearRegression()
model.fit(x_train,y_train)

y_pred=model.predict(x_test)

y_pred

from sklearn.metrics import r2_score

r2_score(y_test,y_pred)
