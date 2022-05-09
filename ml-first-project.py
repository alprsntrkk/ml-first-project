import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import display



df = pd.read_excel(r'C:\Users\asenturk\Desktop\crop_dataset.xlsx',sheet_name='Sheet1')
display(df.head())
display(df.dtypes)

df=pd.get_dummies(df,drop_first=(True))
print(df)
X = df[['CROP', 'CONTRACT_COUNT', 'CATEGORY_IZMIR','CATEGORY_SAMSUN']]

print(X)

y = df['BOUGHT_BALES']

from sklearn import linear_model

regr = linear_model.LinearRegression()
regr.fit(X, y)

prediction=regr.predict([[2021,7097,0,1]])

print(prediction)
