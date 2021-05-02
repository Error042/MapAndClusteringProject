import math
import matplotlib.pyplot as plt

database = 'TestRouteSVG.csv'

xg = 12.35427
yg = 51.33031

x_draw = [xg]
y_draw = [yg]

x_draw2 = []
y_draw2 = []

comparison = None

def result(x_value, y_value):
    return math.sqrt((71.5 * (xg - x_value)) * (71.5 * (xg - x_value)) + (111.3 * (yg - y_value)) * (111.3 * (yg - y_value)))

with open(database, 'r') as file:
    for counter, line in enumerate(file):
        data = line.strip().split(',')

        if data[0] == 'time':
            continue

        ys = float(data[1])
        xs = float(data[2])

        x_draw2.append(float(data[2]))
        y_draw2.append(float(data[1]))

        nearest_point = result(xs, ys)
        print(counter, nearest_point)

        if comparison == None or comparison > nearest_point:
            comparison = nearest_point
            y_result = ys
            x_result = xs
            at_place = counter

x_draw.append(x_result)
y_draw.append(y_result)

imData = plt.imread('map.png')
fig, ax = plt.subplots()
ax.imshow(imData, extent=[12.25800, 12.47678, 51.27130, 51.40799])
ax.set_aspect(1.0/ax.get_data_ratio(), adjustable='box')

#plt.plot(x_draw2, y_draw2, marker='o')
#plt.plot(x_draw, y_draw, color='red', marker='o')
plt.plot(x_draw, y_draw)
plt.xlabel('Latitude')
plt.ylabel('Longitude')

print('The point LON:' + str(x_result) + ' LAT:' + str(y_result) + ' is the closest, with ' + str(comparison) +
      'km. It is the element with the index: ' + str(at_place))
plt.show()
