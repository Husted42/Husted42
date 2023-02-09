import numpy as np

#Read a txt file into a list of list, line by line
def read_data (filename):
    with open(filename, "r") as file:
        data = []
        for line in file:
            values = line.strip().split()
            data.append([float(val) for val in values])
    return data

#print list
def printRows():
    list_of_rows = read_data("data.txt")
    print(list_of_rows)

#Convert a list to a np.array
def convertToNumpy(lst):
    arr = np.array(lst)
    return arr

def run():
    if (False): printRows()
    if (True): print(convertToNumpy(read_data("data.txt")))
run()

