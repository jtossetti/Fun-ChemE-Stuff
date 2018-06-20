#This program explores the relationship between the hot and cold water stream
# temperatures that flow through a plate heat exchanger.
#The flow rates of the water streams are not equal.

#Step 1: import packages

import scipy.io #Need to access matlab file
import matplotlib.pyplot as plt #For plotting
plt.ion() #Interactive mode to display plots
import numpy as np
import os 

#Step 2: import temperature data --> Consider using absolute path.   
                      
mat = scipy.io.loadmat('unequal_batch.mat') 

#print(type(mat))
#print(np.shape(mat))
#print(mat.keys()) #Get acquainted with data inside by \
#viewing the dictionary keys

#Step 3: Create numpy arrays using mat's dictionary keys.

time = mat['time'] / 60 #Convert seconds to minutes
THin = mat['THin'] #Temps are in F 
THout = mat['THout']
TCin = mat['TCin']
TCout = mat['TCout']

#Step 4: Plot time vs. temp. Want to easily see how hot and cold streams \
#change relative to each other, so best to plot all 4 on same axes. 

fig = plt.figure()
plt.plot(time, THin,'r-', label = 'Incoming Hot')
plt.plot(time, THout, color = 'orange', label = 'Outgoing Hot')
plt.plot(time, TCin, 'b-', label = 'Incoming Cold')
plt.plot(time, TCout, 'm-', label = 'Outgoing Cold')

plt.xlim(0,14)
plt.ylim(35,65)
plt.title('Temperatures of Incoming and Outgoing\nHot and Cold Streams \
in a Heat Exchanger')
plt.xlabel('Time (Min)')
plt.ylabel('Temperature (F)')
plt.grid()
fig.legend(bbox_to_anchor= (0.75, 0.4), shadow= True) #Manually position \
#the legend inside. Adding a shadow makes the legend easier to see. 








    

            



