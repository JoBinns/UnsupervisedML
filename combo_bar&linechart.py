#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import file
rules = pd.read_csv('filename.csv')

#include graph in notebook
%matplotlib inline

#customize runtime configuration of plots
plt.rcParams['figure.figsize'] = (20,10)
plt.style.use('fivethirtyeight')

#create figure and add axes
fig, ax1 = plt.subplots()

#create a twin axis sharing the x axis
ax2 = plt.twinx(ax = ax1)

#define consequents, support and data
consequents = ['AF', 'Age_80-89', 'CIHD', 'COPD', 'Male', 'Age_over89', 'HT', 'NIDDM', 'HC', 'DU', 'Female', 'HCVA', 'HCD']
support = [5.08, 13.24, 6.46, 3.12, 40.52, 0.71, 40.00, 8.06, 5.87, 0.24, 59.47, 5.17, 5.01]
data = [46,41,38,32,16,14,9,9,9,7,7,4,4]

#create a barchart
ax1.bar(consequents, data)

#create a linechart on the same figure sharing the x axis
ax2.plot(support, color = 'm')

#give the graph a title
ax1.set_title('Frequency of comorbidities/demographics in top 5% of generated association rules versus support', fontsize=20)

#label the x axis and the 2 y axes
ax1.set_ylabel('Frequency (%)', fontsize=20)
ax1.set_xlabel('Comorbidities/Demographics')
ax2.set_ylabel('Support (%)', color = 'm')

#save and export graph
fig.savefig(r'newfilename.png', bbox_inches='tight')

