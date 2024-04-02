from math import sqrt

def length_of_segment(x1, y1, x2, y2):
    distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))
segment_length = length_of_segment(x1, y1, x2, y2)
print("Длина отрезка равна:", segment_length)