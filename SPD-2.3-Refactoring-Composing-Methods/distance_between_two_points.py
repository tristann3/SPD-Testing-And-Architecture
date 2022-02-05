# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.

import math


def calculate_distance(xc1, yc1, xc2, yc2):
  # Calculate the distance between the two circle
    distance = math.sqrt((xc1-xc2)**2 + (yc1 - yc2)**2)
    print('distance', distance)

calculate_distance(4, 4.25, 53, -5.35)


def calculate_length(xa, ya, xb, yb):
  # calcualte the length of vector AB vector which is a vector between A and B points.
    length = math.sqrt((xa-xb)*(xa-xb) + (ya-yb)*(ya-yb))
    print('length', length)

calculate_length(-36, 97, .34, .91)