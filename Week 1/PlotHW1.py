#import numpy and matlibplots module


#generate array of x values from 0 to 6pi

#calculate y values for sin wave

#calculate y values for cosine wave

#plot x and y values for both functions 

#set dashed line for sine wave and solide line for cosine wave

#add legend

import matplotlib.pyplot as plt
import numpy as np
plt.rcdefaults()
from numpy import sin, cos, pi

a = np.linspace(0,6*pi,100)
ysin_=sin(a)
ycos_=cos(a)

plt.gca().set_color_cycle(['blue','red'])
plt.plot(a,ysin_)
plt.plot(a,ycos_)
plt.ylabel("y")
plt.xlabel("x")
plt.legend(('sin(x)','cos(x)'))
plt.title('Plot of sinx and cosx for 0 to 6pi')

plt.show()

#leave comment here with your information
#Name:Adaugo Anyamele
#Date:1/21/2016

