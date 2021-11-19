from matplotlib import pyplot as plt 
import numpy as np
x_axis_value=np.arange(10,20,1) #1 intervall b/w two elements
y_axis_value=np.arange(100,200,10) # 10 interval b/w two elements

print("x value:",x_axis_value)
print("y value:",y_axis_value)
plt.scatter(x_axis_value,y_axis_value)
plt.show()
