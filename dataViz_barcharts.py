#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import file
rules = pd.read_csv('filename.csv')

#include graph in notebook
%matplotlib inline

#determine total number of antecedents
rules['antecedents'].count()

#determine number of individual antecedents and convert to percentage
rules['antecedents'].value_counts()/rules['antecedents'].count()*100

#create figure object
fig = plt.figure()

#add axes to the figure object
ax = fig.add_axes([0,0,1,1])

#define antecedents and data
antecedents = ['died548', 'MIin30', 'CIin30', 'RFin30', 'Bleed']
data = [50, 21, 14, 13, 2]

#create a bar chart
ax.bar(antecedents, data)

#give chart a title
ax.set_title('Frequency of complications in top 5% of generated association rules')

#label x and y axes
ax.set_xlabel('Complications')
ax.set_ylabel('Frequency (%)')

#save and export graph
fig.savefig(r'newfilename.png', bbox_inches='tight')

