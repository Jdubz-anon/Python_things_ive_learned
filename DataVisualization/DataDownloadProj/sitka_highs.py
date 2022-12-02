import csv
import matplotlib.pyplot as plt
import datetime as dt
filename = r'/home/jdubzanon/Documents/PythonCrashCourseData/data/sitka_weather_2018_simple.csv'

#open file and read it
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

#indexing column numbers for refrence
#for index, col_header in enumerate(header_row):
    #print(index,col_header)

#get high temps
    dates, highs, lows = [], [], []

    for row in reader:
        current_date = dt.datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        #high = int(row[5])
        highs.append(int(row[5]))
        lows.append(int(row[6]))

#plot high temps
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

#actual plots on graph use ax.plot()
ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='blue')
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.5)
#format plot
ax.set_title('Daily High and Low Temps, 2018', fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temp (F)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()

