import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_excel("turystyka1.xlsx", header=None)
df_t = df.rename(columns={0:"Kategoria",1:"Rok",2:"Liczba"})
df.to_excel("turystykapo.xlsx", index=False)
#to zamienia wiersze na kolumny
df_t=df.T
df_t.to_excel("turystykpoT.xlsx", index=False)
print(df_t)
df_t.rename(columns={'0':'Kategoria'},inplace=True)
df_t.head()
#od tego momentu musisz kombinowac
#fig=plt.figure()
#ax = fig.add_axes([0,0,1,1])
#ax.axis('equal')
#wb=pd.read_excel('turystykapoT.xlsx')
#a = wb.groupby(2).Status.count()
#b = wb.Status.unique()
#ax.pie(a, labels=b, autopct='%1.1f%%')
#plt.show()
