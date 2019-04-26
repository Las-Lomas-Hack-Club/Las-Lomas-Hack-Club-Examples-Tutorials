'''
Visualizing data can be very useful.  Matplotlib is an easy efficient way of doing this.
'''
#importing modules needed
#note, you may need to pip install this.  Come ask for help if you can't figure it out! :)
import matplotlib.pyplot as plt 

#can assign object if you want to
#makes basic graph
plt.plot([1,2],[2,3])

#showing graph
plt.show()
#here you assign x and y a variable
x = []
xval = input("type in x variable")
graphable_x = int(xval)
x.append(graphable_x)
 
y = []
yval = input("type in y variable")
graphable_y = int(yval)
y.append(graphable_y)
#label makes a legend
plt.plot(x,y, label = "a point... not gonna lie, kinda lame")

#x and y axis labels
plt.xlabel("My x values")
plt.ylabel("My y values")

#shows legend
plt.legend()

#shows plot
plt.show()
#programming on a chromebook is a nightmare :(


