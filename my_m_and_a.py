import pandas as pd
import my_ds_babel



def my_m_and_a(wood_data_1, wood_data_2, wood_data_3):
    # Load the CSV files from their URLs into pandas DataFrames
    wood_df1 = pd.read_csv(wood_data_1)
    wood_df2 = pd.read_csv(wood_data_2, header=None)
    wood_df3 = pd.read_csv(wood_data_3)

    

    # Print the column names of each DataFrame
    print("DataFrame 1 Columns:")
    print(wood_df1.columns)
    print("DataFrame 2 Columns:")
    print(wood_df2.columns)
    print("DataFrame 3 Columns:")
    print(wood_df3.columns)

    # Checking the data information and data types of each DataFrame
    print(wood_df1.info())
    print(wood_df2.info())
    print(wood_df3.info())

    # Fixing wood_df1
    wood_df1_fixed = wood_df1.drop(columns=['UserName'])
    wood_df1_fixed['Age'] = wood_df1_fixed['Age'].astype(str)

    # Fixing wood_df2
    def split_dataframe_column(dataframe, column, separator):
        """ This function splits a column into several columns using a separator"""
        split_data = dataframe[column].str.split(separator, expand=True)
        num_columns = split_data.shape[1]
        column_names = ['col{}'.format(i) for i in range(num_columns)]
        split_data.columns = column_names
        dataframe = dataframe.drop(column, axis=1)
        dataframe = pd.concat([dataframe, split_data], axis=1)
        return dataframe

    wood_df2_fixed = split_dataframe_column(wood_df2, column=0, separator=';')

    df2_columns = {'col0': 'Age', 'col1': 'City', 'col2': 'Gender', 'col3': 'Name', 'col4': 'Email'}
    wood_df2_fixed.rename(columns=df2_columns, inplace=True)

    def split_and_rename_name_column(dataf, name_column):
        """ This function splits the name column into FirstName and LastName"""
        dataf[['FirstName', 'LastName']] = dataf[name_column].str.split(' ', 1, expand=True)
        dataf.drop(columns=[name_column], inplace=True)
        return dataf

    split_and_rename_name_column(wood_df2_fixed, 'Name')

    def reindex_dataframe_columns(dataframe):
        """ This function reindexes the DataFrame columns according to the provided database schema"""
        schema = [
            "Gender",
            "FirstName",
            "LastName",
            "Email",
            "Age",
            "City",
            "Country",
            "Created_at",
            "Referral"
        ]
        data = dataframe.reindex(columns=schema)
        return data

    wood_df2_fixed = reindex_dataframe_columns(wood_df2_fixed)

    # Fixing wood_df3
    wood_df3_fixed = wood_df3.drop(columns=['Name', 'Email', 'Age', 'City', 'Country'])

    wood_df3_fixed = split_dataframe_column(wood_df3_fixed, column='Gender', separator='\t')

    data_f3_columns = {'col0': 'Gender', 'col1': 'Name', 'col2': 'Email', 'col3': 'Age', 'col4': 'City', 'col5': 'Country'}
    wood_df3_fixed.rename(columns=data_f3_columns, inplace=True)

    wood_df3_fixed = wood_df3_fixed.apply(lambda x: x.str.replace('string_', '').str.replace('integer_', '') if x.dtype == 'object' else x)

    split_and_rename_name_column(wood_df3_fixed, 'Name')

    wood_df3_fixed = reindex_dataframe_columns(wood_df3_fixed)

    # Dropping null values in the DataFrames
    wood_df1_fixed.dropna(inplace=True)
    wood_df2_fixed.dropna(inplace=True)
    wood_df3_fixed.dropna(inplace=True)

    # Fixing the 'Gender' column for each DataFrame due to inconsistent values
    mapping = {'Female': 'Female', 'Male': 'Male', '0': 'Male', '1': 'Female', 'F': 'Female', 'M': 'Male'}
    wood_df1_fixed['Gender'] = wood_df1_fixed['Gender'].map(mapping)
    wood_df2_fixed['Gender'] = wood_df2_fixed['Gender'].map(mapping)

    mapping = {'Female': 'Female', 'Male': 'Male', 'boolean_0': 'Male', 'boolean_1': 'Female', 'character_M': 'Male'}
    wood_df3_fixed['Gender'] = wood_df3_fixed['Gender'].map(mapping)

    # Merge the data using pandas.concat() method
    merged_wood_data = pd.concat([wood_df1_fixed, wood_df2_fixed, wood_df3_fixed])

    # Change the 'City' column values of the merged data to title case
    merged_wood_data['City'] = merged_wood_data['City'].str.title()

    return merged_wood_data

#merged_wood_csv = my_m_and_a(wood_data1, wood_data2, wood_data3)
#my_ds_babel.csv_to_sql(merged_wood_csv, 'plastic_free_boutique.sql', 'customers')
#print(merged_wood_csv.head())
