import matplotlib.pyplot as plt

#input_values = [1,2,3,4,5]
#squares = [1,4,9,16,25]

#creating large amount of plot values

x_values = range(1,1000)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8-dark')
fig, ax  = plt.subplots()
#for colormaps https://matplotlib.org/stable/tutorials/colors/colormaps.html#sphx-glr-tutorials-colors-colormaps-py
#https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.colormaps
cmap =  plt.colormaps['PiYG'] #colormap

ax.scatter(x_values,y_values, s=10, c=y_values, cmap=cmap) #scatter plot



#set chart title and label axes
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

#set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

ax.axis([0,1100,0,1100000])
#autosave
plt.savefig('squares_plot.png', bbox_inches='tight')
plt.show()