# --------------------------------
# Plotting a Simple Line Graph
# --------------------------------
import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]

#plt.style.use('dark_background')
#plt.style.use('Solarize_Light2')
#plt.style.use('bmh')
#plt.style.use('ggplot')

fig, ax = plt.subplots()
ax.plot(input_values,squares)

plt.show()

# -------------------------------------------
# Changing the Label Type and Line Thickness
# -------------------------------------------
fig, ax2 = plt.subplots()
ax2.plot(input_values,squares,linewidth = 3)

# Set chart title and label axes.
ax2.set_title("Square Numbers",fontsize=24)
ax2.set_xlabel("Value",fontsize=14)
ax2.set_ylabel("Squre of Value",fontsize = 14)

# Set size of tick labels.
ax2.tick_params(axis='both',labelsize=14)

plt.show()

# ---------------------------------------
# Using Built-in Styles
# ---------------------------------------
# to see the suportted styels on your system 
# enter a python terminal sesh and...
# >>> import matplotlib.pyplot as plt
# >>> plt.style.available
# enter line at top 'plt.style.use('chosen style')
# ['seaborn-deep', 'seaborn-muted', 'Solarize_Light2', 'dark_background', 'fast', 'seaborn-pastel', 'seaborn-notebook', 'classic', 'seaborn-ticks', 'seaborn-paper', 'grayscale', 'seaborn-dark-palette', 'seaborn-talk', 'ggplot', 'seaborn', 'seaborn-dark', '_classic_test', 'seaborn-white', 'seaborn-whitegrid', 'bmh', 'fivethirtyeight', 'seaborn-bright', 'tableau-colorblind10', 'seaborn-colorblind', 'seaborn-darkgrid', 'seaborn-poster']


# ---------------------------------------
# Plotting and Styling Individual Points with scatter()
# ---------------------------------------
x_values = range(1, 10001)
y_values = [x**2 for x in x_values] # list comp to calc squares in range

fix, ax3 = plt.subplots()
ax3.scatter(x_values,y_values,c=(0,0.8,0),s=10)  # 's' sets size of dots
                                                 # 'c' sets RGB color

# Set chart title and label axes
ax3.set_title("Square Numbers", fontsize=24)
ax3.set_xlabel("Value", fontsize=14)
ax3.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax3.tick_params(axis='both',which='major',labelsize=14)

# Set the range for each axis.
ax3.axis([0,1100,0,1100000])

plt.show()

# ---------------------------------------
# Using a Colormap
# ---------------------------------------
x_values = range(1, 10001)
y_values = [x**2 for x in x_values] # list comp to calc squares in range

fix, ax4 = plt.subplots()
ax4.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,s=10)

# Set chart title and label axes
ax4.set_title("Square Numbers", fontsize=24)
ax4.set_xlabel("Value", fontsize=14)
ax4.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax4.tick_params(axis='both',which='major',labelsize=14)

# Set the range for each axis.
ax4.axis([0,1100,0,1100000])

plt.show()

# ---------------------------------------
# Saving Plots Automatically
# ---------------------------------------
# plt.savefig('squares_plot.png',bbox_inches='tight')

# ---------------------------------------
# Random Walk Visual
# ---------------------------------------
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Make a random walk.
rw = RandomWalk()
rw.fill_walk()

# Plot the points in the walk.
fig, ax5 = plt.subplots()
ax5.scatter(rw.x_values,rw.y_values,s=15)
plt.show()

# ---------------------------------------
# Generating multiple Random Walks
# ---------------------------------------
#while True:
#    # Make a random walk.
#    rw = RandomWalk(50_000)
#    rw.fill_walk()
#
#    # Plot the points in the walk.
#    plt.style.use('classic')
#    fig, ax6 = plt.subplots(figsize=(15,9))
#    point_numbers = range(rw.num_points)
#    ax6.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',s=15)
#
#    # Remove the axes.
#    ax6.get_xaxis().set_visible(False)
#    ax6.get_yaxis().set_visible(False)
#    plt.show()
#
#    keep_running = input("Make another walk? (y/n): ")
#    if keep_running == 'n':
#        break

# ---------------------------------------
# Rolling Dice with Plotly
# ---------------------------------------
from die import Die

# Create a D6. - six sided die
die = Die()

# make some rolls, and store results in a list.
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

print(results)