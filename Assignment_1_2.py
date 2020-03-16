# File:   Assignment_1_2.py
# Name:   Shani Kumar
# Date:   03/15/2020
# Course: DSC-550 - Data Mining
# Desc:   01. Create an array of size [10,50] and use the random function to fill it with integers between
#             1 and 500 (inclusive). Load it to a DataFrame.
#         02. Calculate the sum of each row; the sum of each column; and the sum of all entries.
#         03. Determine the minimum; maximum; average; and standard deviation of all entries.
#         04. Sort the DataFrame: by rows, by columns, on row 2, on column 2.
# Usage:  This program is to complete assignment 1.2 requirements
import numpy as np
import pandas as pd

# Create 2D array using random function with value (1, 500) inclusive.
myArray = np.random.randint(1, 501, size=(10, 50))

arrayDf = pd.DataFrame(myArray)  # load to a DataFrame

# Print array data
print("Constructed Array: \n{}".format(arrayDf.values))

# print sum of element by each row
print("Sum by each row: \n{}".format(arrayDf.sum(axis=1).values))

# print sum of element by each column
print("Sum by each column: \n{}".format(arrayDf.sum(axis=0).values))

# print sum of all element
print("Sum of all the element: \n{}".format(arrayDf.values.sum()))

# Print minimum; maximum; average; and standard deviation of all entries
print("Some statistical details:\nMin. Value: {}\nMax. Value: {}\n"
      "Std. Dev. : {}".format(arrayDf.values.min(), arrayDf.values.max(), arrayDf.values.std()))

# Print sorted values by columns (0 and 1)
print("Sort by columns ('0' & '1'): \n{}".format(arrayDf.sort_values(axis=0, by=[0, 1])))

# Print sorted values by rows (0 and 1)
print("Sort by rows ('0' & '1'): \n{}".format(arrayDf.sort_values(axis=1, by=[0, 1])))

# Print sorted values by column 2
print("Sort by column '2': \n{}".format(arrayDf.sort_values(axis=0, by=2)))

# Print sorted values by row 2
print("Sort by row '2': \n{}".format(arrayDf.sort_values(axis=1, by=2)))
