import pandas as pd
import numpy as np

def calculate_euclidean_distances(data, reference_row):
    numeric_data = np.array(data)[:, :-1].astype(float)
    ref_row_values = np.array(reference_row[:-1]).astype(float)
    differences = ref_row_values - numeric_data
    sq = differences**2
    squared_distances = np.sum(sq, axis=1)
    distances = np.sqrt(squared_distances)
    return distances

def IB2(inputFile, outputFile):
    theFile = pd.read_csv(inputFile)
    CS = theFile.head(1).copy()

    for index, row in theFile.iterrows():
        distances = calculate_euclidean_distances(CS.values, row.values)
        top = np.argsort(distances)[:1]
        classes = CS.iloc[top]['class'].tolist()[0]
      
        if classes != row['class']:
            CS.loc[len(CS.index)] = row

        theFile = theFile.drop(index)

    CS.to_csv(outputFile, index=False)


input_file_name = input("Enter the name of the input file: ")
output_file_name = 'IB2_' + input_file_name

IB2(input_file_name, output_file_name)
