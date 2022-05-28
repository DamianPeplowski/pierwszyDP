import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#from io import BytesIO
#import matplotlib.pyplot as plt
#from PIL import Image
#buf = BytesIO()
#plt.plot(...)  # Plot something here
#plt.savefig(buf)
#Image.open(buf).convert("RGB").save("testplot.jpg", quality=5)

#zad1
x = np.linspace(-6, 2*np.pi)
y = np.cos(x)
y1 = 30*np.sin(x)
y2 = (2*x/5)-2
y3 = 7-x
fig = plt.figure()
ax  = fig.add_subplot(111)
ax.plot(x, y1, c='r',linestyle='dashed', label='y=20*sin(x)')
ax.plot(x, y2, c='y',linestyle='dashed', label='y=(2x/5)-2')
ax.plot(x, y3, c='g', label='y=7-x',linewidth=2.0)
plt.legend(loc='lower left')
plt.show()
plt.savefig('line_plot.jpg', dpi=300)

#zad 2 zestaw 2 nie do konca z wykresem kołowym
#tylko z 2015 rokiem
data = pd.read_excel('mieszkania2.xlsx', sheet_name='DANE')
df = pd.DataFrame(data)
seria = df.groupby('Formy budownictwa')['Formy budownictwa'].size()
plt.text(-1.2, 1.1, 'NrIndeksu', fontsize=10, color='green')
#explode = np.random.randint(0, 5, seria.size) / 10#explode=explode
plt.pie(x=seria,labels = seria.keys(), shadow=True, autopct=lambda pct: "{:2f}%".format(pct))
plt.show()
plt.savefig("PDF.pdf")
plt.show()
#zad3
