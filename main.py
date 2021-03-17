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

# creating the CS with the specifications
plt.plot(xs, ys, 'r-o')
plt.xlabel('Latitude')
plt.ylabel('Longitude')
imData = plt.imread('map.png')
plt.imshow(imData, extent=[12.32117, 12.41747, 51.30025, 51.36042])

# showing the final result
plt.show()