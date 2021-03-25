import math

database = 'TestRoute.csv'

xg = 12.35427
yg = 51.33031

comparison = None

with open(database, 'r') as file:
    for line in file:
        data = line.strip().split(',')

        if data[0] == 'time':
            continue

        ys = float(data[1])
        xs = float(data[2])

        result = math.sqrt((71.5 * (xg - xs)) * (71.5 * (xg - xs)) + (111.3 * (yg - ys)) * (111.3 * (yg - ys)))

        if comparison == None or comparison > result:
            comparison = result
            y_result = ys
            x_result = xs

print('Der Punkt LON:' + str(x_result) + ' LAT:' + str(y_result) + ' is the closest, with ' + str(comparison) + 'km.')