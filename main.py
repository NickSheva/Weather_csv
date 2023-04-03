'''График погоды в городе Ситке 2018 год'''
import csv
import sys
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

print(plt.style.available)

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename, encoding='utf-8') as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for index, column in enumerate(header_row):
        print(index, column)

    highs, lows, dates = [], [], []
    for row in reader:
        try:
            dates.append(datetime.strptime(row[2], '%Y-%m-%d'))
        except FileNotFoundError as error:
            print(f"{error} Ошибка.", file=sys.stderr)
        else:
            highs.append(int(row[5]))
            lows.append(int(row[6]))

# переводим градусы из Фаренгейтф в Цельсия
h = np.array(highs) # преобразуем список с помощью numpy
high = np.int_((h - 32) / 1.8) # преобразуем float в int

l = np.array(lows)
low = np.int_((l - 32) / 1.8)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots(figsize=(10, 8))

#plt.style.use('seaborn-v0_8')
plt.plot(dates, high, 'r', alpha=0.4)
plt.plot(dates, low, 'b', alpha=0.3)

# заголовок таблицы
plt.title('Daily weather in Sitka 2018', fontsize=18, weight='bold')
# заголовок по оси Y
plt.ylabel('Temperature(C)', fontsize=16)
plt.xlabel('',  fontsize=14)
# закрашиваем область между температурами
plt.fill_between(dates, high, low, facecolor='blue', alpha=0.07)
# pазворачиваем даты для лучшей читаемости
fig.autofmt_xdate()
plt.tick_params(axis='both', which='major')
plt.ylim((-9, 30))

#plt.show()
# сохранение графика
plt.savefig('weather_sitka', bbox_inches='tight' )

