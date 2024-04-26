times = [['flamengo', 3, 0], ['vasco', 2, 5], ['gremio', 3, 3]]

#print(times[1][2] + times[2][2])

for time in times:
    if(time[0] != 'vasco'):
        print(time[2])