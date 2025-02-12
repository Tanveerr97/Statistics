<<<<<<< HEAD
# Blinkit-data-analyst-project
Blinkit-data-analyst-project
Data Exploration and Initial Analysis using Jupyter Notebook:
Check Missing Data: To identify if any columns contain missing (null) values.
data.isnull().sum()
If there are missing values, you need to decide whether to fill or drop them.
Check for Duplicates
# Check for duplicate rows
data.duplicated().sum()

# If you find duplicates, remove them
data = data.drop_duplicates()
After exploring the data, you will likely need to clean it before further analysis. Here are common data cleaning tasks you can perform in Jupyter
Handle Missing Data
If any columns have missing values, you can:
Fill the missing values with a default value (e.g., mean, median, or a fixed value).
Drop rows or columns with missing values.
# Drop rows with any missing values
data.dropna(inplace=True)
Outliers can significantly affect your analysis. You can identify outliers using statistical methods or visualization (like box plots) and then either remove or cap them.
After cleaning the data, you should save the cleaned version for further analysis or visualization.
# Save the cleaned dataset
data.to_csv('cleaned_blinkit_data.csv', index=False)
# Data Visualization in Power BI
After you've cleaned and transformed your data in Jupyter, it's time to visualize it using Power BI. Power BI allows you to create interactive and insightful reports and dashboards.
![Image](https://github.com/user-attachments/assets/09f7b921-3992-4eeb-bd77-a6e3a0a8d0ed)
=======
# Statistics
>>>>>>> b06ee1875e6d7dd515b75252bf683734b1fd2c45
