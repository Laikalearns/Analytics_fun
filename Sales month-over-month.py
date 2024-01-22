# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 19:33:16 2022

@author: auxil
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\auxil\Desktop\\py4e\\PANDAS - matlab\\company_sales_data.csv")
monthlist = df ['month_number'].tolist()
profitlist = df ['total_profit'].tolist()

plt.plot(monthlist, profitlist, label = '2021 Profit', color="g", marker="o", markerfacecolor='k', linestyle='--', linewidth=3.25)

plt.xlabel('Months FY22')
plt.ylabel('Profits in M')
plt.legend(loc='lower right')
plt.title('Sales as of Last Year')
plt.xticks(monthlist)
plt.yticks([100000, 200000, 300000, 400000, 500000, 600000, 700000])
plt.show()