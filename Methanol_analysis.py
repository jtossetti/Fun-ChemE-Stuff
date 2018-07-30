#This program processes and plots data from a methanol (MeOH) fuel cell \
#experiment. Currents and voltages were recorded from three separate cells.
#Each one contained a difference concentration of MeOH: 1, 2, and 3%. The goal \
#is to observe the effect of MeOH conc. on current and voltage.

#As of 9 July, the .m file has been downloaded. See GDriveAPI_Max.py \
#for code

#Step 1: Import libraries.
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns #Need to swarm plot 
import pandas as pd #Data Frames
import scipy.io #Need to import .mat (MATLAB) files 

#Step 2: Import .mat file UPDATE on 07/11 --> I saved var of interest \
# (currents and voltages for three experiments, each differing in MeOH\
# conc.) to a .mat file. Do this via save('filename.mat','var1',...,'varn') in Matlab

#BEWARE!!!! Using save('filename.mat', 'var1',..., 'varn') overwrites what was
#already there!!!!
mat = scipy.io.loadmat('INSERT PATH')#Abs. path 
#print(mat.keys()) #Peek at what's inside 

keys = ('jM1', 'jM2', 'jM3', 'vM1', 'vM2', 'vM3')
#Arrays the same len?
#No, these dict arrays have different lengths
dmat = {k: mat[k] for k in keys} #Creates new dictionary with keys in "keys" list.
#dmat was created using a Dictionary Comprehension. FYI. 
#print(dmat.keys()) --> Took a peek. Looks good.

dmat_unp = [y for x in dmat.values() for y in x] #This unpacks 
#dmat into a list of arrays
j= pd.DataFrame(dmat_unp[0:3]).T #".T" takes transpose of
#The data frame inserts Nan values to ensure uniform shape. Program does NOT
#try to plot Nan values. 
j_concat = pd.concat([j[0], j[1], j[2]])
#j_concat= Single col of current values.

v= pd.DataFrame(dmat_unp[3:]).T #Dataframe for voltages
v_concat= pd.concat([v[0], v[1], v[2]]) #Creates single
#col of voltages 

#Col for Methanol concentrations (1%, 2%, 3%) 
ones = np.ones(len(j[0:]))
twos = 2*ones
threes = 3*ones
c = pd.DataFrame([ones, twos, threes]).T #Each col is conc
c_concat= pd.concat([c[0], c[1], c[2]])


#Step 4: Visualization--> Try beeswarm, scatter, ECDF, box 
#Try concatenating each data set into ONE col. --> Tried and WORKS!
plt.subplot(1,2,1) #One row, 2 cols, first plot
_= sns.swarmplot(x= c_concat, y= j_concat)
_= plt.xlabel('[MeOH] (%)') #NOICE brackets around MeOH denote concentration!
#That is accepted practice. 
_= plt.ylabel('Current (mA)')
_= plt.grid()

plt.subplot(1,2,2)
_= sns.swarmplot(x= c_concat, y= v_concat)
_= plt.xlabel('[MeOH] (%)')
_= plt.ylabel('Voltage (V)')
_= plt.grid()

plt.suptitle('Effects of Methanol Concentration on Current & Voltage')
plt.show()

#Looks great. Very well done. 
