# import the required libraries
import pandas as pandas
import numpy as np

#import the required file and describe data
HES = pd.read_csv('filename.csv')
HES.info()

# list unique values in the Age column
uniqueValues = HES['Age'].unique()
print(uniqueValues)

# remove all episodes where Age = 0
calcmean = HES[(HES['Age'] == 0)].index
HES.drop(calcmean, inplace = True)
HES.info()

# calculate the mean of the remaining values in the Age column
HES['Age'].mean()

# import complete file again and replace values of 0 (in Age column) with 68
HES = pd.read_csv('filename.csv')
HES = HES.replace({'Age': {0:68}})

# delete unexplained, empty or duplicated features  
del HES ['Admission']
del HES ['Discharge']
del HES ['Surgery Type']
del HES ['Surgery Date']
del HES ['infection']
del HES ['Surgery30']
del HES ['Surgery6M']
del HES ['Charlson']
del HES ['ISTC']
del HES ['LOS']
del HES ['Rivaroxaban']
del HES ['Surgery2yr']
del HES ['Rev3yr']
del HES ['Rev4yr']
del HES ['U264']
del HES ['M302']
del HES ['M47']
del HES ['Date of Death']
del HES ['died90']
del HES ['Readmission28days']
del HES ['Reop4Infin28']
del HES ['Dis30d']
del HES ['hipdis18m']
del HES ['Dis3m']
del HES ['Dis6m']
del HES ['Dis12m']
del HES ['Dis24m']
del HES ['Dis36m']
del HES ['no_ofDisi']


# remove episodes with unexplained codes 
procNames = HES[(HES["proc"] == "THR-") | (HES["proc"] == "Res-") | (HES["proc"] == "THR-O") | (HES["proc"] == "Res-O")].index 
HES.drop(procNames, inplace=True)
genderNames = HES[(HES["Sex"] == 9)].index 
HES.drop(genderNames, inplace=True)

# replace values > 1 (in Dis48m column) with 1
HES = HES.replace({'Dis48m': {2:1, 3:1, 4:1, 5:1, 6:1, 7:1, 8:1, 9:1, 10:1, 11:1, 12:1}})

#remove procedure feature
del HES ['proc']

#convert Nan values to 0
HES = HES.fillna(0)

#convert all datatypes to int and describe data
HES = HES.astype(int)
HES.info()

# export file
HES.to_csv(r'newfilename.csv', index = False, header = True)


