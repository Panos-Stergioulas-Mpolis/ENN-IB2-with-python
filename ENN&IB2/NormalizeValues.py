import pandas as pd

def normalization(inputFile, outputFile):

    theFile = pd.read_csv(inputFile)
    cols = theFile.columns[:-1]
    rangeOfValues = theFile[cols].max() - theFile[cols].min()
    x = theFile[cols] - theFile[cols].min()
    theFile[cols] = x / rangeOfValues
    theFile.to_csv(outputFile, index=False)


input_file_name = input("Enter the name of the input file: ")
output_file_name = 'normalized_'+input_file_name

normalization(input_file_name, output_file_name)
