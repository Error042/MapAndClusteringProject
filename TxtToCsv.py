# this file creates a usable .csv for the map and the clustering for a txt file. I create the .txt file from a .svg file
import csv

with open('map.txt', 'r') as file:
    for line in file:
        data = line.strip().split(' ')

liste = []

for element in data:
    liste.append(element.split(','))

x = 0
y = 0
as_a_list = []
counter = 0

# converting the y axis upside down and the converting form px into lat long
for i in liste:
    counter += 1
    y += float(i[1])
    y_zw = (((2000 - y) / 20) * 0.0013669) + 51.27130
    x += float(i[0])
    x_zw = ((x / 20) * 0.0021878) + 12.25800

    as_a_list.append(str(counter) + ',' +str(round(y_zw, 5)) + ',' + str(round(x_zw, 5)))

final = [['time','lat','long']]
for elemente in as_a_list:
    final.append(elemente.split(','))

with open('new_csv.csv', 'w', newline='') as f:

    thewriter = csv.writer(f)

    for e in final:
        thewriter.writerow(e)
