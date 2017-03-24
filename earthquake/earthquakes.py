
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import seaborn as sns
from mpl_toolkits.basemap import Basemap
import warnings

earth_quake = pd.read_csv("./database.csv")
# print earth_quake.head()
# print earth_quake.columns

earth = earth_quake[["Date", "Latitude","Longitude","Magnitude","Depth","Type"]]
#print earth.head()
#print earth.tail()

earth["Date"] = pd.to_datetime(earth["Date"])
# print earth.shape

earth.pivot_table(index = "Type", values = "Magnitude", aggfunc=len)

m = Basemap(projection='mill',llcrnrlat=-80,urcrnrlat=80, llcrnrlon=-180,urcrnrlon=180,lat_ts=20,resolution='c')

longitudes = earth["Longitude"].tolist()
latitudes = earth["Latitude"].tolist()
#m = Basemap(width=12000000,height=9000000,projection='lcc',
            #resolution=None,lat_1=80.,lat_2=55,lat_0=80,lon_0=-107.)
x,y = m(longitudes,latitudes)

fig = plt.figure(figsize=(12,10))
plt.title("All affected areas")
m.plot(x, y, "o", markersize = 3, color = 'blue')
m.drawcoastlines()
m.fillcontinents(color='coral',lake_color='aqua')
m.drawmapboundary()
m.drawcountries()
plt.show()

minimum = earth["Magnitude"].min()
maximum = earth["Magnitude"].max()
average = earth["Magnitude"].mean()

(n,bins, patches) = plt.hist(earth["Magnitude"], range=(0,10), bins=10)
plt.xlabel("Earthquake Magnitudes")
plt.ylabel("Number of Occurences")
plt.title("Overview of earthquake magnitudes")
plt.show()

print "Magnitude" +"   "+ "Number of Occurence"
for i in range(5, len(n)):
    print(str(i)+ "-"+str(i+1)+"         " +str(n[i]))

plt.boxplot(earth["Magnitude"])
plt.show()

highly_affected = earth[earth["Magnitude"]>=8]

longitudes = highly_affected["Longitude"].tolist()
latitudes = highly_affected["Latitude"].tolist()
n = Basemap(projection='mill',llcrnrlat=-80,urcrnrlat=80, llcrnrlon=-180,urcrnrlon=180,lat_ts=20,resolution='c')
x,y = n(longitudes,latitudes)
fig3 = plt.figure(3,figsize=(12,10))
plt.title("Highly affected areas")
n.plot(x, y, "o", markersize = 10, color = 'blue')
n.drawcoastlines()
n.fillcontinents(color='coral',lake_color='aqua')
n.drawmapboundary()
n.drawcountries()
plt.show()

earth["Month"] = earth['Date'].dt.month

#month_occurrence = earth.pivot_table(index = "Month", values = ["Magnitude"] , aggfunc = )

month_occurrence = earth.groupby("Month").groups
print(len(month_occurrence[1]))

month = [i for i in range(1,13)]
occurrence = []

for i in range(len(month)):
    val = month_occurrence[month[i]]
    occurrence.append(len(val))

print(occurrence)
print(sum(occurrence))


fig, ax = plt.subplots(figsize = (10,8))
bar_positions = np.arange(12) + 0.5

months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
num_cols = months
bar_heights = occurrence

ax.bar(bar_positions, bar_heights)
tick_positions = np.arange(1,13)
ax.set_xticks(tick_positions)
ax.set_xticklabels(num_cols, rotation = 90)
plt.title("Frequency by Month")
plt.xlabel("Months")
plt.ylabel("Frequency")
plt.show()

earth["Year"] = earth['Date'].dt.year
year_occurrence = earth.groupby("Year").groups

year = [i for i in range(1965,2017)]
occurrence = []

for i in range(len(year)):
    val = year_occurrence[year[i]]
    occurrence.append(len(val))

maximum = max(occurrence)
minimum = min(occurrence)
print("Maximum",maximum)
print("Minimum",minimum)

#print("Year :" + "     " +"Occurrence")

#for k,v in year_occurrence.items():
    #print(str(k) +"      "+ str(len(v)))

fig = plt.figure(figsize=(10,6))
plt.plot(year,occurrence)
plt.xticks(rotation = 90)
plt.xlabel("Year")
plt.ylabel("Number of Occurrence")
plt.title("Frequency of Earthquakes by Year")
plt.xlim(1965,2017)
plt.show()


supermoon_date = ["2016-11-14","2016-11-16","2016-11-15"]  #( one day before and after)
supermoon = earth[earth['Date'].isin(supermoon_date)]

m = Basemap(llcrnrlon=165, llcrnrlat=-50, 
    urcrnrlon=179, urcrnrlat=-34, resolution='i',
    lat_0=-41, lon_0=172, 
    area_thresh=100.,projection='lcc')


longitudes = supermoon["Longitude"].tolist()
latitudes = supermoon["Latitude"].tolist()
x,y = m(longitudes,latitudes)
fig2 = plt.figure(3,figsize=(12,10))
plt.title("Can Supermoon trigger Earthquake?")
m.plot(x, y, "o", markersize = 10, color = 'blue')
m.drawcoastlines()

m.shadedrelief()
plt.show()




