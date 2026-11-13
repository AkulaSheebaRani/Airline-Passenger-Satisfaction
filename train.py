import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings 
warnings.filterwarnings('ignore')
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

df=pd.read_csv('airline_passanger_satisfaction.csv')

print(df.head())

print(df.info())

print(df.isnull().sum())

df=df.drop(['Unnamed: 0','id'],axis=1)

x=df.iloc[:,:-1]
y=df.iloc[:,-1]
### Outlier detection
num_cols = ['Age', 'Flight Distance',
            'Departure Delay in Minutes',
            'Arrival Delay in Minutes']

for col in num_cols:
    Q1=x[col].quantile(0.25)
    Q3=x[col].quantile(0.75)
    IQR=Q3-Q1
    lower=Q1-1.5*IQR
    upper=Q3+1.5*IQR
    outliers=x[(x[col]<lower) | (x[col]>upper)]
    print(col)
    print("Outlier Count:",len(outliers))

y=y.map({'neutral or dissatisfied':0,
         'satisfied':1})

### Target Variable diatribution

print(y.value_counts())

sns.countplot(x='satisfaction',data=df)
plt.title("Passenger Satisfaction ")
plt.show()

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)

cat_cols=x.select_dtypes(include='object').columns
num_cols=x.select_dtypes(include=['int64','float64']).columns

cat_pipe=Pipeline(steps=[
    ('imputer',SimpleImputer(strategy='most_frequent')),
    ('encoder',OneHotEncoder(handle_unknown='ignore'))])
num_pipe=Pipeline(steps=[
    ('imputer',SimpleImputer(strategy='median'))])
preprocessor=ColumnTransformer(transformers=[
    ('cat',cat_pipe,cat_cols),
    ('num',num_pipe,num_cols)])
# ### Decision Tree
rf_pipeline=Pipeline(steps=[
    ('preprocessor',preprocessor),
    ('classifier',RandomForestClassifier(random_state=42))])
rf_pipeline.fit(x_train,y_train)

y_pred=rf_pipeline.predict(x_test)

acc=accuracy_score(y_test,y_pred)
cr=classification_report(y_test,y_pred)
cm=confusion_matrix(y_test,y_pred)
print("Accuracy :",acc*100)
print("Classification_report")
print(cr)
print("Confussion Matrix")
print(cm)

## Saving file
joblib.dump(rf_pipeline, "airline_passenger_satisfaction_pipeline.pkl")

print("Saved:airline_passenger_satisfaction_pipeline.pkl")
