import csv
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import style
#kinda useless but fun
with open ('cereal.csv') as fi:
    sugars = []
    rating = []
    fat = []
    cereal_reader = csv.reader(fi)
    next(cereal_reader) # skip header
    for row in cereal_reader:
        print(row)
        rounded_rating = row[-1]
        rating.append(int(rounded_rating[0:2]))
        fat.append(int(row[5]))
        sugars.append(int(row[9]))
style.use('ggplot')

fig = plt.figure(facecolor="b")

ax1 = fig.add_subplot(111, projection='3d')
ax1.scatter(fat, sugars, rating, c='g', marker='o')
ax1.set_xlabel('fat (g)')
ax1.set_ylabel('sugars (g)')
ax1.set_zlabel('rating (%)')

plt.show()
