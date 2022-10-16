from random import randrange
from statistics import mean
import time

def calcHist(array):
    array_2 = [0] * 10
    for i in array:
        if i <= 99:
            array_2[0] += 1
        elif 100 <= i and i <= 199:
            array_2[1] += 1
        elif 200 <= i and i <= 299:
            array_2[2] += 1
        elif 300 <= i and i <= 399:
            array_2[3] += 1
        elif 400 <= i and i <= 499:
            array_2[4] += 1
        elif 500 <= i and i <= 599:
            array_2[5] += 1
        elif 600 <= i and i <= 699:
            array_2[6] += 1
        elif 700 <= i and i <= 799:
            array_2[7] += 1
        elif 800 <= i and i <= 899:
            array_2[8] += 1
        elif 900 <= i and i <= 999:
            array_2[9] += 1
    array_3 = [i / 1000000 for i in array_2]

def make_list():
    array_4 = []
    for i in range(1000000):
        array_4.append(999)
    return array_4

time_array = []
for i in range(100):
    array_1 = make_list()
    t0 = time.time()
    calcHist(array_1)
    temp_time = time.time() - t0
    time_array.append(temp_time)
print("Минимальное время: ", min(time_array))
print("Максимальное время: ", max(time_array))
print("Среднее время: ", mean(time_array))