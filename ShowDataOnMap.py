import matplotlib.pyplot as plt

# creating variables to put in the coordinate system (CS)
xs = []
ys = []

# filling the variables with the points from the .csv file
with open('TestRoute.csv', 'r') as file:
    for line in file:
        data = line.strip().split(",")

# skipping the first line to get the data
        if data[0] == 'time':
            continue
# needs to be a float instead of a string so it is correctly shown in the CS
        ys.append(float(data[1]))
        xs.append(float(data[2]))

# creating the CS with the map.png in the background
imData = plt.imread('map.png')
fig, ax = plt.subplots()
ax.imshow(imData, extent=[12.25800, 12.47678, 51.27130, 51.40799])
ax.set_aspect(1.0/ax.get_data_ratio(), adjustable='box')

# placing the coordinates in the CS and labeling the axes
plt.plot(xs, ys, color='red', marker='o')
plt.xlabel('Latitude')
plt.ylabel('Longitude')

# show the final result
plt.show()
