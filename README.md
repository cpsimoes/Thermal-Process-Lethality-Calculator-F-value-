# Thermal-Process-Lethality-Calculator-F-value-
This repository hosts a Python application designed to calculate the lethality (F-value) of a thermal process. The lethality of a thermal process describes the effectiveness of the process in reducing the number of harmful microorganisms. It is an essential concept in food processing and other industries that require precise temperature control.

The application includes implementations of two numerical integration methods:

Trapezoidal Rule: A straightforward method that approximates the area under the curve as a series of trapezoids. This method is relatively quick but can be less accurate for curves with significant curvature.

Simpson's Rule: A more complex method that approximates the area under the curve using parabolic segments. This method often provides a more accurate approximation but requires that the number of intervals (or data points minus 1) be even.

Features:

Accepts time vs. temperature data in CSV format.
Allows users to specify a reference temperature and time interval for calculations.
Supports both the Trapezoidal Rule and Simpson's Rule for numerical integration.
Can be compiled into a standalone executable.

Usage:
The calculator can be run via the command line, passing the necessary parameters such as the CSV file path, reference temperature, and time range.
