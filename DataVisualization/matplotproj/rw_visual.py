import matplotlib.pyplot as plt
from random_walk import RandomWalk


rw = RandomWalk()
rw.fill_walk()
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(15,9), dpi=128)
point_numbers = range(rw.num_points)


cmap = plt.colormaps['Blues']
#ax.plot(rw.x_values,rw.y_values,linewidth=3)
ax.scatter(rw.x_values,rw.y_values, c=point_numbers ,s=3,cmap=cmap, edgecolor='none')
ax.scatter(0,0, c='green',edgecolor='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100)

ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()

#keep_running = input('Make Another Walk? (y/n) ').lower()
#if keep_running == 'n':
    #break
