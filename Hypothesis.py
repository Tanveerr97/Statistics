import numpy as np
from scipy import stats

# Sample data
sample_data = np.array([55, 47, 53, 50, 52, 48, 60, 45, 49, 51])

# Known value to compare the sample mean
known_value = 10

# Perform the one-sample t-test
t_stat, p_value = stats.ttest_1samp(sample_data, known_value)

# Output results
print("t-statistic:", t_stat)
print("p-value:", p_value)

# Conclusion
if p_value < 0.05:
    print("Reject the null hypothesis: the sample mean is significantly different from", known_value)
else:
    print("Fail to reject the null hypothesis: the sample mean is not significantly different from", known_value)


***********************************************************************************************************************************

import numpy as np
from scipy import stats

# Sample data for two groups
group_a = np.array([82, 85, 88, 91, 87, 85, 90])
group_b = np.array([78, 80, 75, 79, 74, 76, 73])

# Perform the independent two-sample t-test
t_stat, p_value = stats.ttest_ind(group_a, group_b)

# Output results
print("t-statistic:", t_stat)
print("p-value:", p_value)

# Conclusion
if p_value < 0.05:
    print("Reject the null hypothesis: the means of Group A and Group B are significantly different.")
else:
    print("Fail to reject the null hypothesis: the means of Group A and Group B are not significantly different.")










