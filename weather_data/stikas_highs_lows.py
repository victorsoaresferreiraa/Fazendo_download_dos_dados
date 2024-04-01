from pathlib import Path
import csv 
from datetime import datetime

import matplotlib.pyplot as plt 

path = Path('death_valley_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

#Extrai datas, temperaturas maximas e minimas 
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    low = row[5]
    dates.append(current_date)
    highs.append(high)
    lows.append(low)


#Plota as temperaturas maximas e minimas 
plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#formata o grafico
ax.set_title("Daily high and low temperatures, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (f)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
