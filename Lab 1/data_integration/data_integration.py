import pandas as pd

# Load the transformed Iris dataset
iris_df = pd.read_csv('./data_collection/source1/iris.csv')

# Load the transformed Tulip dataset
tulip_df = pd.read_csv('./data_collection/source2/tulip_data.csv')


# Add a new 'Type' column to the Tulip and iris dataframe
iris_df['Type'] = 'Iris'
tulip_df['Type'] = 'Tulip'

# Change column names
new_column_names = {
    'Name': 'Species',
    'Petal Length (cm)': 'PetalLengthCm',
    'Petal Width (cm)': 'PetalWidthCm'
}
tulip_df.rename(columns=new_column_names, inplace=True)
combined_df = pd.concat([iris_df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species', 'Type']],
                         tulip_df[['Color', 'Height (cm)', 'PetalLengthCm', 'PetalWidthCm', 'Species', 'Type']]])
# Reset the index of the combined dataframe
combined_df.reset_index(drop=True, inplace=True)
# Save the merged dataset to a new file
combined_df.to_csv('./data_processing/merged_dataset.csv', index=False)

# Print the merged dataset
print(combined_df.head())