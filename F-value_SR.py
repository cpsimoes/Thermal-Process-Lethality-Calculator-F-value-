# -*- coding: latin-1 -*-
import numpy as np
import sys
import csv

def simpsons_rule(y, h):
    return h / 3 * (y[0] + y[-1] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]))

def main():

    data_file = sys.argv[1]
    min_temp = float(sys.argv[2])
    start_time = int(sys.argv[3])
    end_time = int(sys.argv[4])

    time = []
    temperature = []

    with open(data_file, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)
        for row in reader:
            time.append(float(row[0]))
            temperature.append(float(row[1]))

    # slice arrays to include only desired range
    time = time[start_time-1:end_time]
    temperature = temperature[start_time-1:end_time]

    # update temperature values to 0 if they are below the minimum temperature
    temperature = [temp - min_temp if temp >= min_temp else 0 for temp in temperature]

    h = (time[-1] - time[0]) / (len(time) - 1)
    integral_value = simpsons_rule(temperature, h)

    print("The integral value is:", integral_value)
    print("Calculator for determining the lethality (F value) of a thermal process using the Simpson's rule - Carlos Paula, 2023")

if __name__ == "__main__":
    main()

