# Conduct a paired t-test on dem_percent_12 and dem_percent_16
paired_test_results = pingouin.ttest(
    x = sample_dem_data['dem_percent_12'],
    y=sample_dem_data['dem_percent_16'],
    paired = True
) 

# Print paired t-test results
print(paired_test_results)

# Conduct a Wilcoxon test on dem_percent_12 and dem_percent_16
wilcoxon_test_results = pingouin.wilcoxon(
    x = sample_dem_data['dem_percent_12'],
    y=sample_dem_data['dem_percent_16']
) 

# Print Wilcoxon test results
print(wilcoxon_test_results)

# Select the weight_kilograms and late columns
weight_vs_late = late_shipments[['weight_kilograms', 'late']]

# Convert weight_vs_late into wide format
weight_vs_late_wide = weight_vs_late.pivot(columns='late', 
                                           values='weight_kilograms')


# Run a two-sided Wilcoxon-Mann-Whitney test on weight_kilograms vs. late
wmw_test = pingouin.mwu(x = weight_vs_late_wide['No'],
y= weight_vs_late_wide['Yes'])



# Print the test results
print(wmw_test)


# Run a Kruskal-Wallis test on weight_kilograms vs. shipment_mode
kw_test = pingouin.kruskal(
    data = late_shipments,
    dv= 'weight_kilograms',
    between='vendor_inco_term')

# Print the results
print(kw_test)
