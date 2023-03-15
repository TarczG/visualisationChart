from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


df1 = pd.read_csv('life_expectancy.csv') #source: https://data.worldbank.org/indicator/SP.DYN.LE00.IN?locations=1W&start=1984&view=chart
df2 = pd.read_csv('poverty.csv') #source:https://data.worldbank.org/indicator/SI.POV.DDAY?locations=1W&start=1984&view=chart


# filtered data by specific country
df1=df1[(df1['Country Name']=="Poland") | (df1['Country Name']=='Greece')]

# limit data by years
years=['1995','2000','2005','2010','2015','2020']
df1=pd.melt(frame=df1, id_vars=['Country Name'], value_vars=years,value_name='lifeExpectation',var_name='year')
PolandExpLife = df1[(df1['Country Name']=="Poland") ].lifeExpectation
GreeceExpLife = df1[(df1['Country Name']=='Greece')].lifeExpectation

#side by side bars
def create_x(t,w,n,d):
    return [t*x + w*n for x in range(d)]

PolandExpLife_x=create_x(2,0.8,1,6)
GreeceExpLife_x=create_x(2,0.8,2,6)

plt.figure(figsize=(10,8))
ax=plt.subplot()
plt.bar(PolandExpLife_x,PolandExpLife)
plt.bar(GreeceExpLife_x,GreeceExpLife)
middle_x=[(PolandExpLife_x[i]+GreeceExpLife_x[i])/2 for i in range(len(years))]
ax.set_xticks(middle_x)
ax.set_xticklabels(years)

plt.legend(['Poland','Greece'])
plt.title('Comparison in life length: Poland vs Greece')
plt.xlabel('Year')
plt.ylabel('Life Expectation')

plt.show()
plt.close()

#chart 2
df = pd.read_csv('students.csv')


school_subjects = ["History", "Chemistry", "Mathematics", "Art", "Physics"] 

As=[ len(df[df[i]==5.0]) for i in school_subjects]
Bs=[ len(df[df[i]==4.0]) for i in school_subjects]
Cs=[ len(df[df[i]==3.0]) for i in school_subjects]
Ds=[ len(df[df[i]==2.0]) for i in school_subjects]
Es=[ len(df[df[i]==1.0]) for i in school_subjects]
Fs=[ len(df[df[i].isnull()]) for i in school_subjects]


x = range(len(school_subjects))
c_bottom = np.add(As, Bs)
d_bottom = np.add(c_bottom, Cs)
e_bottom = np.add(d_bottom, Ds)
f_bottom = np.add(e_bottom, Es)

plt.figure(figsize=(10,8))
plt.bar(x, As)
plt.bar(x, Bs, bottom=As)
plt.bar(x, Cs, bottom=c_bottom)
plt.bar(x, Ds, bottom=d_bottom)
plt.bar(x, Es, bottom=e_bottom)
plt.bar(x, Fs, bottom=f_bottom)
ax=plt.subplot()
ax.set_xticks(range(len(school_subjects)))
ax.set_xticklabels(school_subjects)
plt.xlabel('Subject')
plt.ylabel('Number of students')
plt.title('Grade distribution')
plt.legend([5,4,3,2,1,"absent"])
plt.show()



#Two Histograms on a Plot
df3 = pd.read_csv('life_expectancy.csv') #source: https://data.worldbank.org/indicator/SP.DYN.LE00.IN?locations=1W&start=1984&view=chart

year2000 = df3[ ~(df3["2000"].isnull())]["2000"]
year2020 = df3[ ~(df3["2020"].isnull())]["2020"]


plt.figure(figsize=(10,8))
plt.hist(year2000 , bins=12, density=True, histtype = 'step', linewidth=2)
plt.hist(year2020 , bins=12, density=True, histtype = 'step', linewidth=2)
plt.legend(['2000','2020'])
plt.xlabel('Life Length')
plt.ylabel('Frequency')
plt.title('Life Average 2000 vs 2020')
plt.show()


df4=pd.read_csv('continents_country.csv')
continents = ['Africa','Asia','Europe','North America','Oceania','South America']
num_countries = [ len(df4[df4["continent"]==i]) for i in continents]

#pie chart

plt.figure(figsize=(10,8))

def autopct_format(values):
    def my_format(pct):
        tot = sum(values)
        vl = int(round(pct*tot/100.0))
        return '{v:d}'.format(v=vl)
    return my_format
plt.pie(num_countries, autopct = autopct_format(num_countries))
plt.axis('equal')
plt.title('Number of countries on continents - in world context')
plt.legend(continents)
plt.show()

x=input('exit')
