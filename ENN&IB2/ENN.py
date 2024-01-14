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

def enn(inputFile, outputFile):
    theFile = pd.read_csv(inputFile)

    rows_to_remove = []

    for index, row in theFile.iterrows():
        distances = calculate_euclidean_distances(theFile.values, row.values)
        top4 = np.argsort(distances)[:4]
        classes = theFile.iloc[top4]['class'].tolist()

        if classes[1] == classes[2] or classes[1] == classes[3]:
            nClass = classes[1]
        elif classes[2] == classes[1] or classes[2] == classes[3]:
            nClass = classes[2]
        elif classes[3] == classes[1] or classes[3] == classes[2]:
            nClass = classes[3]
        else:
            nClass = classes[1]

        if nClass != row['class']:
            rows_to_remove.append(index)

    theFile = theFile.drop(rows_to_remove)

    theFile.to_csv(outputFile, index=False)

input_file_name = input("Enter the name of the normalized input file: ")
output_file_name = 'ENN_' + input_file_name

enn(input_file_name, output_file_name)
