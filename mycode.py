import pandas as pd
import os

# Fast dataframe creation from a Python dictionary
data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "city": ["New York", "London", "Tokyo"]
}

df = pd.DataFrame(data)

# print(df)

data_dir = "data"
os.makedirs(data_dir,exist_ok = True)

#  define the file path
file_path = os.path.join(data_dir,'sample_data.csv')
#  save the dataframe to a csv file without the index and inclunding the columns


df.to_csv(file_path,index= False)


print(f"CSV file saved to:{file_path}")



