#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import file
rules = pd.read_csv('filename.csv')

#select required data and save as new dataframe
condition_1 = rules['antecedents'].apply(lambda x: 'CIin30' in x)
rules2 = rules.loc[condition_1]
rules2

#customize runtime configuration of plots
plt.rcParams['figure.figsize'] = (20,10)
plt.style.use('fivethirtyeight')

#create line-chart
plt.plot(rules2['consequents'], rules2['lift'], color = 'm', marker = 'o')

#label ticks on x axis and rotate labels 90°
plt.xticks(rules2['consequents'], rotation=90)

#give chart a title
plt.title('Association rules where antecedent is CIin30. Lift versus consequents.', fontsize=20)

#label y axis
plt.ylabel('Lift', fontsize=20)

#label x axis
plt.xlabel('Consequents', fontsize=20)

#save and export file
plt.savefig(r'newfilename.png', bbox_inches='tight')



