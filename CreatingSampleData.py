import random
import csv
import matplotlib.pyplot as plt

x = []
y = []
counter = 0
zwischen = []
final = [['count', 'x', 'y']]

while counter <= 4999:
    x.append(float(random.randint(0, 5000)))
    y.append(float(random.randint(0, 5000)))
    counter += 1

print(x, y)

for c, element in enumerate(x):
    zwischen.append(str(c))
    zwischen.append(str(x[c]))
    zwischen.append(str(y[c]))
    final.append(zwischen)
    zwischen = []

print(final)
with open('ExampleData.csv', 'w', newline='') as f:

    thewriter = csv.writer(f)

    for e in final:
        thewriter.writerow(e)
#plt.plot(x, y, 'o')
#plt.show()