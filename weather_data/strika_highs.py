from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('death_valley_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

#Extrai datas e temperaturas maximas 
dates, highs = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    dates.append(current_date)
    highs.append(high)


#Extrai as temaperaturas maximas 
hights = []
for row in reader:
    high = int(row[4])
    hights.append(high)

#print(hights)

#Plota as temperaturas maximas
plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(hights, color='red')
ax.plot(dates, highs, color='red')


#Formata o grafico
ax.set_title("Daily high temperatures, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (f)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
print(plt.style.available)

#for index, colum_header in enumerate(header_row):
    #print(index, colum_header)

#print(header_row)