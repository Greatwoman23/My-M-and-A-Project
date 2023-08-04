# Welcome to My M And A
***

## Task
The task is to merge three customers tables from a new company called Only Wood Box into a database schema that consist of:
"gender" - 'string'
"firstname" - 'string'
"Lastname" - 'string'
"email" - 'string'
"age" - 'string'
"city" - 'string'
"country" - 'string'
"created_at" - 'string'
"referral" - 'string'

## Description
This code processes and merges three datasets extracted from CSV files. It starts by loading the datasets into pandas DataFrames. Then, it prints the column names and data information of each DataFrame for inspection. The cleaning process involves dropping irrelevant columns, splitting data in specific columns, and renaming the resulting columns accordingly.
The 'Gender' column is particularly fixed to ensure consistency by mapping inconsistent values to standardized ones across all DataFrames. After cleaning, the three datasets are merged into a single DataFrame using pandas 'concat' function. Null values are dropped from the merged DataFrame for data integrity.
Finally, the 'City' column values are converted to title case for consistent formatting. The resulting merged DataFrame contains the combined and cleaned data from all three datasets, ready for further analysis or storage in a database.
Created a gitignore file to exclude .csv and .db files in the project

## Installation
pandas library was installed , which is essential for data manipulation in Python. 
A custom module called my_ds_babel.py was also imported.

## Usage
Execute the code: 
Open a terminal or command prompt, navigate to the directory where you saved the Python file, and run the script by executing the command python my_m_and_a.py. This will start the execution of the code.
Observe the output: 
As the code runs, it will load the CSV files from specific URLs into pandas DataFrames. The column names and data information of each DataFrame will be printed to the console for inspection.
Data cleaning and merging: 
The code will then proceed to clean and process the three DataFrames. It will drop irrelevant columns, split specific columns, and fix inconsistencies in the 'Gender' column to ensure data consistency.
Final merged DataFrame:
Once the cleaning and processing are complete, the code will merge the three cleaned DataFrames into a single DataFrame using the pandas 'concat' function. Any null values will be dropped from the merged DataFrame to maintain data integrity.
Output: 
The final merged DataFrame, named merged_wood_data, will contain all the combined and cleaned data from the three original datasets. This DataFrame can be further analyzed, used in machine learning models, or stored in a database.


```
./my_m_and_a.py
```
### The Core Team
deniran_o
aniyom_e


<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px'></span>
