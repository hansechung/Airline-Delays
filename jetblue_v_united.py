# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 16:58:55 2018

@author: Hanse
"""

import numpy as np
import pandas as pd
# import dateutil
# import IPython
import matplotlib.pyplot as plt
import matplotlib as mpl
# import seaborn


jetblue_df = pd.read_csv("JFK_B9_Sep2017.csv", skiprows = 7, usecols = list(range(17)))
united_df = pd.read_csv("EWR_UA_Sep2017.csv", skiprows = 6)

jb_delaybydest = jetblue_df[['Destination Airport', 'Departure delay (Minutes)']]
ua_delaybydest = united_df[['Destination Airport', 'Departure delay (Minutes)']]
jb_delaybytime = jetblue_df[['Scheduled departure time', 'Departure delay (Minutes)']]
ua_delaybytime = united_df[['Scheduled departure time', 'Departure delay (Minutes)']]

#jb_df_delay = jetblue_df.groupby("Destination Airport").mean()
#ua_df_delay = united_df.groupby("Destination Airport").mean()

print(jb_delaybydest.head(5))
print(ua_delaybydest.head(5))

jb_avgdelay = jb_delaybydest.groupby('Destination Airport', as_index = False)[['Departure delay (Minutes)']].mean()
ua_avgdelay = ua_delaybydest.groupby('Destination Airport', as_index = False)[['Departure delay (Minutes)']].mean()

jb_avgdelay.rename(columns={'Destination Airport' : 'Dest'}, inplace = True)
ua_avgdelay.rename(columns={'Destination Airport' : 'Dest'}, inplace = True)

jb_avgdelay.rename(columns={'Departure delay (Minutes)' : 'Mean delay'}, inplace = True)
ua_avgdelay.rename(columns={'Departure delay (Minutes)' : 'Mean delay'}, inplace = True)

jb_avgdelay.sort_values('Mean delay', inplace = True, ascending = False)
ua_avgdelay.sort_values('Mean delay', inplace = True, ascending = False)

jbairports = jb_avgdelay.head(10)['Dest'].tolist()
jbdelays = jb_avgdelay.head(10)['Mean delay'].tolist()

uaairports = ua_avgdelay.head(10)['Dest'].tolist()
uadelays = ua_avgdelay.head(10)['Mean delay'].tolist()

fig, ax = plt.subplots()
ax.barh(jbairports, jbdelays)
ax.set(xlim=[0, 150], xlabel='Minutes of delay', ylabel='Destination',
       title='Jetblue Top 10 Delays from JFK')

fig2, ax2 = plt.subplots()
ax2.barh(uaairports, uadelays)
ax2.set(xlim=[0, 150], xlabel='Minutes of delay', ylabel='Destination',
       title='United Top 10 Delays from EWR')







