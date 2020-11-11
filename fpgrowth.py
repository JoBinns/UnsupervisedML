#install mlxtend machine learning library
pip install mlxtend 

#import required data manipulation and data analysis libraries
import pandas as pd
import numpy as np

#load the required file and describe data
HES = pd.read_csv('filename.csv')
HES.info()

#import required libraries from mlxtend
from mlxtend.frequent_patterns import fpgrowth
from mlxtend.frequent_patterns import association_rules

#generate frequent itemsets using fpgrowth algorithm
frequent_itemsets = fpgrowth(HES, min_support = 0.0001, use_colnames = True)
frequent_itemsets

#generate association rules
rules = association_rules(frequent_itemsets, metric = 'lift', min_threshold = 1.1)
rules

#add columns to rules which describe the width of the antecedents and consequents
rules['antecedent_len'] = rules['antecedents'].apply(lambda x: len(x))
rules['consequent_len'] = rules['consequents'].apply(lambda x: len(x))
rules.info()

#condition_1 to contain data whereby antecedents are complications
condition_1 = rules['antecedents'].apply(lambda x:'died548' in x or 'PEin90' in x
                                        or 'DVTin90' in x or 'MIin30' in x or 'CVAin30' in x or 'TIain30' in x
                                        or 'RFin30' in x or 'CIin30' in x or 'read18m' in x or 'CDiff' in x
                                        or 'Bleed' in x or 'Infection2' in x or 'haemorrhage' in x or 'wound pain' in x
                                        or 'Loosening' in x or 'FatalPE' in x or 'Reopsin28' in x or 'Dis48m' in x)
#display condition_1 data
rules.loc[condition_1]

#overwrite rules with condition_1 data
rules = rules.loc[condition_1]
rules.info()

#overwrite rules with rules that contain only 1 antecedent and describe data
rules = rules[(rules['antecedent_len'] == 1)]
rules.info()

#condition_2 to contain data whereby consequents do not contain complications
condition_2 = rules['consequents'].apply(lambda x:'died548' not in x and 'PEin90' not in x
                                        and 'DVTin90' not in x and 'MIin30' not in x and 'CVAin30' not in x and 'TIain30' not in x
                                        and 'RFin30' not in x and 'CIin30' not in x and 'read18m' not in x and 'CDiff' not in x
                                        and 'Bleed' not in x and 'Infection2' not in x and 'haemorrhage' not in x and 'wound pain' not in x
                                        and 'Loosening' not in x and 'FatalPE' not in x and 'Reopsin28' not in x and 'Dis48m' not in x)
#display condition_2 data
rules.loc[condition_2]

#overwrite rules with condition_1 data
rules = rules.loc[condition_2]
rules.info()

#condition_3 to contain data whereby consequents do not contain comorbidities 
#or demographic information with support values >30%
condition_3 = rules['consequents'].apply (lambda x: 'Age_60-69' not in x and 'Age_70-79' not in x
                                          and 'Male' not in x and 'Female' not in x and 'HT' not in x)
#display condition_3 data
rules.loc[condition_3]

#rules2 to contain condition_3 data
rules2 = rules.loc[condition_3]
rules2.info()

#condition_4 to contain data whereby antecedents contain the complications listed
condition_4 = rules['antecedents'].apply(lambda x: 'died548' in x or 'read18m' in x or 'Loosening' in x or 'Dis48m' in x)

#display condition_4 data
rules.loc[condition_4]

#rules3 to contain condition_4 data
rules3 = rules.loc[condition_4]
rules3.info()

#combine rules2 and rules3
result = pd.concat([rules2, rules3])
result.info()

#drop any duplicate rules
result.drop_duplicates(inplace=True)

#sort values by lift in descending order
result.sort_values(by='lift', ascending=False, inplace=True)

#change default formatting to show all rows
pd.set_option('display.max_rows', None)

#display top 5% of rules
result.head(56)

result.to_csv(r'/anothernewfilename.csv', index = False, header = True)