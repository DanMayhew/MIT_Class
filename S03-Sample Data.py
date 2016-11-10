import cauldron as cd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import sys


df = pd.read_csv('Olympic_Sample_Data.csv')

cd.display.header('Olympic Rowing Races Sample:')
cd.display.table(df)

#attempts to convert to hh:mm:ss object to format for calculations
   #df['500m'] = pd.to_timedelta

   #df = pd.read_csv('Olympic_Sample_Data.csv',converters={"Final":float64})

   #def hh_mm_ss2seconds(hh_mm_ss):
    #return reduce(lambda acc, x: acc*60 + x, map(int, hh_mm_ss.split(':')))

   #df = pd.read_csv('Olympic_Sample_Data.csv', sep=r'\s{2,}',
                     #converters={'Final': hh_mm_ss2seconds})

#test of division
  #df['Average'] = df['Place'] / df['Lane']

#shows data types
#for col in df:
    #print (col, df[col].dtypes)


#to create new csv
#df.to_csv('nameoffile.csv)









