from cProfile import label
import numpy as np
import pylab as plt

year = ["2014-15", "2015-16", "2016-17", "2017-18", "2018-19", "2019-20", "2020-21", "2021-22", "2022-23"] # nba season
z = [] # 3 fgr
fig = plt.figure(figsize=(12, 18), facecolor='white')
plt.title('Top 5 NBA Players In Each Regular Season')
colors = ['red', 'blue', 'orange', 'pink', 'grey', 'orange', 'white', 'purple', 'black']

rank = 1

while rank <= 5:
  path = "data" + str(rank) + ".txt"
  with open(path, 'r') as f:
    y = []
    names = {}
    for line in f:
      data = line.split(',')
      y.append(float(data[5]))
      names[float(data[5])] = data[2]
    plt.plot(year, y, 'r', markersize = 4, color=colors[rank - 1])
    for a, b in zip(year, y):
      plt.text(a, b, names[b], ha = 'right', va = 'top', fontsize = 8, alpha = 0.8)
  rank = rank + 1

plt.legend(['Rank1', 'Rank2', 'Rank3', 'Rank4', 'Rank5'])
plt.xlabel('NBA Seasons')
plt.ylabel('Game Impact: Offensive Rating + Defensive Rating')

plt.show()

f.close()