import pandas as pd

# Plot YearsAtCompany from attrition_pop as a histogram
attrition_pop['YearsAtCompany'].hist(bins=np.arange(0, 41, 1))
plt.show()

# Sample 400 employees weighted by YearsAtCompany
attrition_weight = attrition_pop.sample(n=400, weights="YearsAtCompany")

# Plot YearsAtCompany from attrition_weight as a histogram
attrition_weight['YearsAtCompany'].hist(bins = np.arange(0, 41, 1))
plt.show()

#The weighted sample mean is around 11, which is higher than the population mean of around 7. 
#The fact that the two numbers are different means that the weighted simple random sample is biased.