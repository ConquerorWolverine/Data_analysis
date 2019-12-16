import matplotlib.pyplot as plt
import numpy as np
input_values = np.linspace(0,5,100)
squares = input_values*input_values
plt.plot(input_values,squares,linewidth = 5)
plt.title("Squares",fontsize = 26)
plt.xlabel("Values",fontsize = 12)
plt.ylabel("Squares",fontsize = 12)
plt.tick_params(axis='both',labelsize=12)
plt.show()