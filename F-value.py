# -*- coding: latin-1 -*-
import numpy as np
import csv
import sys

def calculate_integral(time, temperature, min_temp, start_time, end_time):
    # Filter values based on time and then subtract min_temp from temperatures
    time_filtered = [t for t, temp in zip(time, temperature) if start_time <= t <= end_time]
    temp_filtered = [temp - min_temp if temp > min_temp else 0 for t, temp in zip(time, temperature) if start_time <= t <= end_time]

    # Calculate integral
    integral_value = np.trapz(temp_filtered, time_filtered)
    return integral_value

def main():
    # Get parameters from command line arguments
    filename = sys.argv[1]
    min_temp = float(sys.argv[2])
    start_time = int(sys.argv[3])
    end_time = int(sys.argv[4])

    # Read data from file
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header
        data = list(reader)

    # Convert data to lists of floats
    time = [float(i[0]) for i in data]
    temperature = [float(i[1]) for i in data]

    integral_value = calculate_integral(time, temperature, min_temp, start_time, end_time)
    print("The integral value is:", integral_value)
    print("Calculator for determining the lethality (F value) of a thermal process using the Trapezoidal rule - Carlos Paula, 2023")

if __name__ == "__main__":
    main()
