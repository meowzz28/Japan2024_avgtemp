from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt


path = Path('weather_data/3751685.csv')
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)


dates, highs, lows, avgs = [], [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        avg = int(row[3])
        '''high = int(row[4])
        low = int(row[5])'''
    except ValueError:
        print("Missing_Data")
    else:
        dates.append(current_date)
        #highs.append(high)
        #lows.append(low)
        avgs.append(avg)


plt.style.use('bmh')
fig, ax = plt.subplots()
#ax.plot(dates, highs, color='red', alpha=0.5)
#ax.plot(dates, lows, color='blue', alpha=0.5)
ax.plot(dates, avgs, color='black', alpha=0.5)
#ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

ax.set_title("Daily Avg Temperatures of Japan, 2024", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()