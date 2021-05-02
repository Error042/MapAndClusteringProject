import math

database = 'TestRoute.csv'

x_point_C = 12.35427
y_point_C = 51.33031

dist_b = None

list_format = []


def distance_two_points(x_value_point1, y_value_point1, x_value_point2, y_value_point2):
    return math.sqrt((71.5 * (x_value_point1 - x_value_point2)) * (71.5 * (x_value_point1 - x_value_point2)) + (
                111.3 * (y_value_point1 - y_value_point2)) * (111.3 * (y_value_point1 - y_value_point2)))


with open(database, 'r') as file:
    for counter, line in enumerate(file):
        data = line.strip().split(',')
        list_format.append(data)

        if data[0] == 'time':
            continue

        ys = float(data[1])
        xs = float(data[2])

        nearest_point = distance_two_points(xs, ys, x_point_C, y_point_C)
        print(counter, nearest_point)

        if dist_b is None or dist_b > nearest_point:
            dist_b = nearest_point
            y_point_A = ys
            x_point_A = xs
            at_place = counter


if distance_two_points(float(list_format[at_place - 1][2]), float(list_format[at_place - 1][1]), x_point_C, y_point_C) \
        < distance_two_points(float(list_format[at_place + 1][2]), float(list_format[at_place + 1][1]), x_point_C,
                              y_point_C):

    dist_a = distance_two_points(float(list_format[at_place - 1][2]), float(list_format[at_place - 1][1]), x_point_C,
                                 y_point_C)
    y_point_B = float(list_format[at_place - 1][1])
    x_point_B = float(list_format[at_place - 1][2])
    print('option befor')

else:
    dist_a = distance_two_points(float(list_format[at_place + 1][2]), float(list_format[at_place + 1][1]), x_point_C,
                                 y_point_C)
    y_point_B = float(list_format[at_place + 1][1])
    x_point_B = float(list_format[at_place + 1][2])
    print('option after')


dist_c = distance_two_points(x_point_A, y_point_A, x_point_B, y_point_B)

print(dist_b, y_point_A, x_point_A, at_place)
print(dist_a, y_point_B, x_point_B)
print(dist_c)

if dist_a ** 2 < (dist_b ** 2 + dist_c ** 2):
    print(dist_a)
else:
    print(math.degrees(math.acos((dist_b ** 2 + dist_c ** 2 - dist_a ** 2) / (2 * dist_b * dist_c))))

print(dist_a ** 2)
print(dist_b ** 2 + dist_c ** 2)
