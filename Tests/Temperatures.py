maxtemp = 1
days = 1
negative = 0
maximum = []
total = 0
average = 0
averagedays = 0
while maxtemp != 999:
    maxtemp = int(input("Please enter the highest temperature of the day"))
    if maxtemp < 0:
        negative = negative + 1
    days = days + 1
    total = total + maxtemp
    maximum.append(maxtemp)
average = total / days
for i in range(len(maximum)):
    if maximum[i] > average:
        averagedays = averagedays + 1
print("The average maximum temperature was",average, "The number of times the maximum temperature was above average was",averagedays, "The number of times temperature reached negative values was",negative)