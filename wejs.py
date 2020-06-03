import json
import urllib.request
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import locale
import datetime
import csv

sns.set(style="darkgrid")
x = datetime.datetime.now()
x = x.strftime("%d%m%y")
urlx = "http://api.openweathermap.org/data/2.5/weather?q=Berlin,de&units=metric&lang=de&appid=d404a1a7718889ba83338da115728976"

with urllib.request.urlopen(urlx) as url:
	data = json.loads(url.read().decode())
	
	
xx = (data["main"])
# print (xx["temp"])
aktu_temp =  data["main"]["temp"]
aktu_wind = data["wind"]["speed"]
aktu_beschr = data["weather"][0]["description"]

print ("Aktuelle Temperatur: " + str(aktu_temp) + "°C")
print("Aktuelle Windgeschwindigkeit: " +  str(aktu_wind))
print("Beschreibung: " + aktu_beschr)

ff = open("./Wetterdaten/" + x + "wetterdaten.txt","w")
ff.writelines("Aktuelle Temperatur: " + str(aktu_temp) + "°C" + "\n")
ff.writelines("Aktuelle Windgeschwindigkeit: " +  str(aktu_wind) + "\n")
ff.writelines("Beschreibung: " + aktu_beschr + "\n")
ff.writelines("\n")

	
urly = "http://api.openweathermap.org/data/2.5/forecast?q=Berlin,de&units=metric&lang=de&appid=d404a1a7718889ba83338da115728976"

with urllib.request.urlopen(urly) as url:
	data2 = json.loads(url.read().decode())
	
i= 0
ii= 0
"""
temp_morgen = (data2["list"][39]["main"]["temp"])
print (temp_morgen)
"""
print()
for i in range(0,39):
	if data2["list"][i]["dt_txt"][11:13] == "15" and i > 5:
		#print (data2["list"][i]["main"]["temp"])
		ii +=1
		if ii == 1:
			temp_1tag = data2["list"][i]["main"]["temp"]
			wind_1tag = data2["list"][i]["wind"]["speed"]
			beschr_1tag = data2["list"][i]["weather"][0]["description"]
		elif ii == 2:
			temp_2tag = data2["list"][i]["main"]["temp"]
			wind_2tag = data2["list"][i]["wind"]["speed"]
			beschr_2tag = data2["list"][i]["weather"][0]["description"]
		elif ii == 3:
			temp_3tag = data2["list"][i]["main"]["temp"]
			wind_3tag = data2["list"][i]["wind"]["speed"]
			beschr_3tag = data2["list"][i]["weather"][0]["description"]
		elif ii == 4:
			temp_4tag = data2["list"][i]["main"]["temp"]
			wind_4tag = data2["list"][i]["wind"]["speed"]
			beschr_4tag = data2["list"][i]["weather"][0]["description"]
			
#print(data2["list"][8]["dt_txt"][11:13])
#print(ii)

print ("Temperatur Morgen: " + str(temp_1tag) + "°C")
print("Windgeschwindigkeit Morgen: " +  str(wind_1tag))
print("Beschreibung für Morgen: " + beschr_1tag)
print()
print ("Temperatur Übermorgen: " + str(temp_2tag) + "°C")
print("Windgeschwindigkeit Übermorgen: " +  str(wind_2tag))
print("Beschreibung für Übermorgen: " + beschr_2tag)
print()
print ("Temperatur in 3 Tagen: " + str(temp_3tag) + "°C")
print("Windgeschwindigkeit in 3 Tagen: " +  str(wind_3tag))
print("Beschreibung für in 3 Tagen: " + beschr_3tag)
print()
print ("Temperatur in 4 Tagen: " + str(temp_4tag) + "°C")
print("Windgeschwindigkeit in 4 Tagen: " +  str(wind_4tag))
print("Beschreibung für in 4 Tagen: " + beschr_4tag)


ff.writelines("Temperatur Morgen: " + str(temp_1tag) + "°C" + "\n")
ff.writelines("Windgeschwindigkeit Morgen: " +  str(wind_1tag) + "\n")
ff.writelines("Beschreibung für Morgen: " + beschr_1tag + "\n")
ff.writelines("\n")
ff.writelines("Temperatur Übermorgen: " + str(temp_2tag) + "°C" + "\n")
ff.writelines("Windgeschwindigkeit Übermorgen: " +  str(wind_2tag) + "\n")
ff.writelines("Beschreibung für Übermorgen: " + beschr_2tag  + "\n")
ff.writelines("\n")
ff.writelines("Temperatur in 3 Tagen: " + str(temp_3tag) + "°C" + "\n")
ff.writelines("Windgeschwindigkeit in 3 Tagen: " +  str(wind_3tag) + "\n")
ff.writelines("Beschreibung für in 3 Tagen: " + beschr_3tag + "\n")
ff.writelines("\n")
ff.writelines("Temperatur in 4 Tagen: " + str(temp_4tag) + "°C" + "\n")
ff.writelines("Windgeschwindigkeit in 4 Tagen: " +  str(wind_4tag) + "\n")
ff.writelines("Beschreibung für in 4 Tagen: " + beschr_4tag + "\n")
ff.close()

N = 5
tempss = (aktu_temp, temp_1tag, temp_2tag, temp_3tag, temp_4tag)
#womenMeans = (100 -bla1,100-bla2, 100-bla3, 100-bla4, 100-bla5)
menStd = (1, 1,1,1,1)
#womenStd = (1, 1,1,1,1)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence
"""
fig, ax = plt.subplots()
rects1 = ax.bar(ind, tempss, width, color='b', yerr=menStd)
"""
p1 = plt.bar(ind, tempss, width, yerr=menStd)
#p2 = plt.bar(ind, womenMeans, width,
           #  bottom=menMeans, yerr=womenStd)
"""
ax.set_ylabel('Temperatur in °C')
ax.set_title('Temperaturen für die nächsten 5 Tage')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('Heute', 'Morgen', 'Übermorgen', '3 Tage', '4 Tage'))
"""
plt.ylabel('Temperatur in °C')
plt.title('Temperaturen für die nächsten 5 Tage')
plt.xticks(ind, ('Heute', 'Morgen', 'Übermorgen', '3 Tage', '4 Tage'))
plt.yticks(np.arange(0, 40, 3))

"""
def autolabel(rects):
   
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)
"""
for index,data in enumerate(tempss):
    plt.text(x=index , y =data+1 , s=f"{data}" , fontdict=dict(fontsize=10))
#plt.legend((p1[0], p2[0]), ('free', 'used'))

plt.savefig("./Wetterdaten/" + x+ "temperaturen.png", dpi=300)
plt.show()
xx = datetime.datetime.now()
xx = xx.strftime("%d.%m.%y")	
xx1 = datetime.datetime.now() + datetime.timedelta(days=1)
xx1 = xx1.strftime("%d.%m.%y")	
xx2 = datetime.datetime.now() + datetime.timedelta(days=2)
xx2 = xx2.strftime("%d.%m.%y")	
xx3 = datetime.datetime.now() + datetime.timedelta(days=3)
xx3 = xx3.strftime("%d.%m.%y")	
xx4 = datetime.datetime.now() + datetime.timedelta(days=4)
xx4 = xx4.strftime("%d.%m.%y")	

	
csvData = [['Datum', 'Temperatur', 'Windgeschwindigkeit', 'Beschreibung'], [xx,aktu_temp,aktu_wind,aktu_beschr],[xx1,temp_1tag,wind_1tag,beschr_1tag],[xx2,temp_2tag,wind_2tag,beschr_2tag],[xx3,temp_3tag,wind_3tag,beschr_3tag],[xx4,temp_4tag,wind_4tag,beschr_4tag]]

with open('./Wetterdaten/' + x + ' wetterdaten.csv','w') as csvFile:
	writer = csv.writer(csvFile)
	writer.writerows(csvData)
	
csvFile.close()
	
"""{'coord': {'lon': 13.39, 'lat': 52.52}, 'weather': [{'id': 801, 'main': 'Clouds', 
	'description': 'Ein paar Wolken', 'icon': '02d'}], 'base': 'stations', 'main': 
	{'temp': 28.93, 'pressure': 1021, 'humidity': 51, 'temp_min': 27.78, 'temp_max': 30.56}, 'visibility': 10000, 
	'wind': {'speed': 4.6, 'deg': 290}, 'clouds': {'all': 20}, 'dt': 1563883050,
	'sys': {'type': 1, 'id': 1275, 'message': 0.0075, 'country': 'DE', 'sunrise': 1563851507, 
	'sunset': 1563909222}, 'timezone': 7200, 'id': 2950159, 'name': 'Berlin', 'cod': 200}
"""