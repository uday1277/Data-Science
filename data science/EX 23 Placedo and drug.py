import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# Simulated data for demonstration purposes
control_group = [24.5, 25.8, 23.7, 26.1, 25.4, 24.9, 24.2, 26.3, 25.7, 24.8]
treatment_group = [21.8, 22.9, 22.1, 23.5, 21.2, 23.1, 22.7, 24.4, 23.8, 22.2]

# Calculate mean and standard deviation for each group
control_mean = np.mean(control_group)
control_std = np.std(control_group)

treatment_mean = np.mean(treatment_group)
treatment_std = np.std(treatment_group)

# Perform two-sample t-test for independent samples
t_statistic, p_value = ttest_ind(control_group, treatment_group)

# Set significance level
alpha = 0.05

# Determine statistical significance
if p_value < alpha:
    result = "Reject null hypothesis: The new treatment has a statistically significant effect."
else:
    result = "Fail to reject null hypothesis: There is no statistically significant effect of the new treatment."

# Visualize the data and results
plt.bar(['Control Group', 'Treatment Group'], [control_mean, treatment_mean], yerr=[control_std, treatment_std])
plt.ylabel('Mean Value')
plt.title('Comparison of Control and Treatment Groups')
plt.show()

# Print the p-value and the result of the hypothesis test
print(f'Calculated p-value: {p_value}')
print(result)
  
