import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# create data
y1=[120,120,120,120,120,120]
x = [0,1,2,3,4,5]
y = np.arange(0,140,20)#[120, 120,120, 120,120]
labels = ['1', '2', '3', '4', '5']
men_means = [20, 10, 30, 10, 50]
women_means = [80, 55, 40, 10, 0]
cm=['#008080','#054907','#F0E68C','#FF81C0','#90EE90']
cw=['#9A0EEA','#40E0D0','#6E750E','#069AF3','#90EE90']
#men_std = [2, 3, 4, 1, 2]
#women_std = [3, 5, 2, 3, 3]
width = 0.7      # the width of the bars: can also be len(x) sequence
fig, ax = plt.subplots()
plt.plot(x, y1,c='g', label="line 1", linestyle="-")
ax.bar(labels, men_means, width,color=cw, label='Men')
ax.bar(labels, women_means, width,color=cm,  bottom=men_means,label='Women')
ax.set_title('Tytuł')
plt.show()
plt.savefig('line_plot.jpg', dpi=300)
#zZad2

data = pd.read_excel('mieszkania1.xlsx', sheet_name='DANE')
df = pd.DataFrame(data)
kolor=['r','y','b']

wartosci=data['Rok']
wysokosć=data['Wartość']
mieszkania=data['Formy budownictwa']
ind=data.loc[data['Formy budownictwa'] == 'indywidualne'].count()[0]
spl=data.loc[data['Formy budownictwa'] == 'spółdzielcze'].count()[0]
kom=data.loc[data['Formy budownictwa'] == 'komunalne'].count()[0]
#seria = df.groupby('Formy budownictwa')['Formy budownictwa'].size()
plt.text(-1.2, 1.1, 'NrIndeksu', fontsize=10, color='green')
plt.bar(data.Rok,data.Wartość,color=kolor)
plt.bar(data.Rok,ind,color='b')
plt.bar(data.Rok,spl,color='y')
plt.bar(data.Rok,kom,color='g')
plt.show()
#zad3
data1 = pd.read_excel('turystyka1.xlsx', sheet_name='TABLICA')
df1 = pd.DataFrame(data1)
print(df1)
