import pandas as pd
import statsmodels.formula.api as smf
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('https://raw.githubusercontent.com/jdeeke/data/main/water_potability.csv', on_bad_lines = 'skip')
df.head()
#create model
model = smf.logit('Potability ~ Solids', data = df).fit()
model.summary()
#create the plot, choose axis
sns.lmplot(x = 'Solids', y = 'Potability', data = df)
#plt.show()

df['phat'] = model.predict(df)
df['yhat'] = 1 * (df['phat'] > 0.5)
df.head()

pd.crosstab(df['Potability'], df['yhat'])
#Mean potability, min potability, etc.
print(df['phat'].describe())