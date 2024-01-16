import matplotlib.pyplot as plt

#pepare your data
tax_years = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
tax_property = [10000, 10500, 11200, 11800, 20000, 21000, 21500, 22500]

#create the UI & plot the data
plt.plot(tax_years, tax_property)

# Customize UI 
plt.xlabel("Tax Years")
plt.ylabel("Average Property Tax")
plt.title("Average Property Taxes Per Home in Dublin,CA (2015-2022)")

# Enhance readability
plt.xticks(tax_years)  # Display all years on the x-axis
plt.grid(True)  # Add a grid for easier interpretation

# output
plt.show()