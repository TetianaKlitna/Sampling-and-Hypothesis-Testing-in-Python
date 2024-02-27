import pandas as pd

#The sample means for the two groups are available as xbar_no and xbar_yes. 
#The sample standard deviations are s_no and s_yes. The sample sizes are n_no and n_yes. 

# Calculate the numerator of the test statistic
numerator = xbar_no - xbar_yes

# Calculate the denominator of the test statistic
denominator = np.sqrt(s_no**2/n_no + s_yes**2/n_yes)

# Calculate the test statistic
t_stat = numerator/denominator

# Print the test statistic
print(t_stat)

# Calculate the degrees of freedom
degrees_of_freedom = n_no + n_yes - 2

# Calculate the p-value from the test stat
p_value = t.cdf(t_stat, degrees_of_freedom)

# Print the p_value
print(p_value)

# Calculate the differences from 2012 to 2016
sample_dem_data['diff'] = sample_dem_data['dem_percent_12'] - sample_dem_data['dem_percent_16']

# Find the mean of the diff column
xbar_diff = sample_dem_data['diff'].mean()

# Find the standard deviation of the diff column
s_diff = sample_dem_data['diff'].std()

# Plot a histogram of diff with 20 bins
sample_dem_data['diff'].hist(bins = 20)
plt.show()

# Conduct a t-test on diff
test_results = pingouin.ttest(
    x = sample_dem_data['diff'],
    y=0,
    paired = True,
    alternative = "two-sided"
)

                              
# Print the test results
print(test_results)

# Conduct a t-test on diff
test_results = pingouin.ttest(x=sample_dem_data['diff'], 
                              y=0, 
                              alternative="two-sided")

# Conduct a paired t-test on dem_percent_12 and dem_percent_16
paired_test_results = pingouin.ttest(x=sample_dem_data['dem_percent_12'],
    y=sample_dem_data['dem_percent_16'],
    paired=True)



                              
# Print the paired test results
print(paired_test_results)