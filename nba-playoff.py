
import pandas as pd
import  matplotlib.pyplot as plt
import  seaborn as sns
import numpy as np 


data=pd.read_csv(r"C:\Users\buğra\Desktop\NBA Stats 202324 All Stats  NBA Player Props Tool (4).csv")
print(data.columns)





"""  
sns.countplot(x='TEAM', data=data)
plt.show()


sns.countplot(x='POS', data=data)
plt.show()

sns.barplot(x='NAME' , y='3P%' ,   data=data)
plt.xticks(rotation=90)
plt.grid(True)
plt.show()


sns.barplot(x='NAME' ,y='2P%'  , data=data)
plt.grid(True)
plt.xticks(rotation=90)
plt.show()

sns.barplot(x='NAME', y='FT%', data=data)
plt.xticks(rotation=90)
plt.grid(True)
plt.show()



sns.scatterplot(x='2P%', y='3P%' , hue='POS', size='AGE' , data=data)
plt.xticks(rotation=90)
plt.legend()
plt.show()


print(
o=data.nlargest(1, 'GP' ),
a=data.nlargest(1,'MPG'  ),
b=data.nlargest(1,'FTA'  ),
c=data.nlargest(1,'2PA'  ),
d=data.nlargest(1, '3PA'  ),
)
"""

plt.pie(data['POS'].value_counts(), labels=data['POS'].unique(), autopct='%1.1f%%', startangle=90)
plt.show()

c=data.nlargest(30,'2PA'  )
d=data.nlargest(30, '3PA'  )

sns.scatterplot(x='3PA', y='2PA', hue='POS' , data=c)
plt.legend()
plt.show()


