# 1)create a simple Data Frame in Pandas with the following data?
#       i)Name ii) age iii) city
import pandas as pd
data={
  'Name':['Sneha','Sachin','Shreya','Sweta'],
  'Age':[34,26,20,20],
  'City':['Pune','Kolkata','Mumbai','Delhi']
}
df=pd.DataFrame(data)
print(df)

#2) select only the rows from a Pandas Data Frame where the 'Age' is greater than 30?
print("question 2")
result = df[df['Age'] > 30]
print(result)

#3) sort the Data Frame by the 'Age' column in ascending order?
sorted_df=df.sort_values(by='Age')
print(sorted_df)


#4) handle missing values (None) in a Pandas Data Frame
data_with_none = {
    'Name': ['Alice', 'Bob', None, 'David'],
    'Age': [25, None, 30, 22],
    'City': ['New York', 'Los Angeles', 'Chicago', None]
}
df_with_none = pd.DataFrame(data_with_none)
print("Data Frame with None values:")
print(df_with_none)


# 5) drop the 'City' column from the Data Frame?
df_dropped = df_with_none.drop(columns=['City'])
print("Data Frame after dropping 'City' column:")
print(df_dropped)

# 6) merge two Pandas Data Frames based on a common column?
data1 = {
    'Name': ['Alice', 'Bob'],
    'Age': [25, 30]
}
data2 = {
    'Name': ['Alice', 'Bob'],
    'City': ['New York', 'Los Angeles']
}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
merged_df = pd.merge(df1, df2, on='Name')
print("Merged Data Frame:")
print(merged_df)

# 7) add a new column to an existing Pandas Data Frame?
df['Country'] = ['India', 'India', 'India', 'India']
print("Data Frame after adding 'Country' column:")
print(df)

# 8) rename a column in a Pandas Data Frame?
df_renamed = df.rename(columns={'City': 'Location'})
print("Data Frame after renaming 'City' to 'Location':")
print(df_renamed)

# 9) How do you get the summary statistics (e.g. mean, median, count) of a Pandas Data Frame?
summary_stats = df.describe()
print("Summary statistics of the Data Frame:")
print(summary_stats)

# 10) How do you check if a Pandas Data Frame is empty? 
is_empty = df.empty
print("Is the Data Frame empty?", is_empty)
