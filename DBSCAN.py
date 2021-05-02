import pandas as pd
from sklearn.cluster import DBSCAN
from collections import Counter
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Read CSV File with GPS data
data = pd.read_csv('TestRouteSvg.csv', sep=',')
print(data.head())

# Show info about dataframe
print(data.info())

# Plot the geographical points (just for testing if it worked)
'''_ = plt.plot(data['long'], data['lat'], marker='.', linewidth=0, color='#128128')
_ = plt.grid(which='major', color='#cccccc', alpha=0.45)
_ = plt.title('Clustering GPS data into hotspots', family='Arial', fontsize=12)
_ = plt.xlabel('Longitude')
_ = plt.ylabel('Latitude')
_ = plt.show()'''

# Prepare data for model
dbscan_data = data[['long', 'lat']]
dbscan_data = dbscan_data.values.astype('float32', copy=False)
print(dbscan_data)

# Normalize data
dbscan_data_scaler = StandardScaler().fit(dbscan_data)
print(dbscan_data_scaler)
dbscan_data = dbscan_data_scaler.transform(dbscan_data)
print(dbscan_data)

# Construct model
'''
-- min_samples :: requires a minimum 20 data points in a neighborhood
-- eps :: in radius 0.02
'''
model = DBSCAN(eps=0.05, min_samples=20, metric='euclidean').fit(dbscan_data)
print(model)

# Seperate outliers from clustered data
outliers_df = data[model.labels_ == -1]
clusters_df = data[model.labels_ != -1]

colors = model.labels_
colors_clusters = colors[colors != -1]
color_outliers = 'black'

# Get info about the clusters
clusters = Counter(model.labels_)
print(clusters)
print(data[model.labels_ == - 1].head())
print('Number of clusters = {}'.format((len(clusters)-1)))

# Plot clusters an outliers
imData = plt.imread('map.png')
# fig = plt.figure()
# ax = fig.add_axes([.1, .1, 1, 1])
fig, ax = plt.subplots()
ax.scatter(outliers_df['long'], outliers_df['lat'], c=color_outliers, edgecolors='black', s=30, alpha=0.5)
ax.scatter(clusters_df['long'], clusters_df['lat'], c=colors_clusters, s=50)

ax.set_xlabel('Longitude', family='Arial', fontsize=9)
ax.set_ylabel('Latitude', family='Arial', fontsize=9)
ax.imshow(imData, extent=[12.25800, 12.47678, 51.27130, 51.40799])
ax.set_aspect(1.0/ax.get_data_ratio(), adjustable='box')
plt.title('Clustering GPS data into hotspots', family='Arial', fontsize=12)
#plt.grid(which='major', color='#cccccc', alpha=0.45)


plt.show()
