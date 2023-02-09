import numpy as np

#Read a txt file into a list of list, line by line
def read_data (filename):
    with open(filename, "r") as file:
        data = []
        for line in file:
            values = line.strip().split()
            data.append([float(val) for val in values])
    return data
    
#Convert a list to a np.array
def convertToNumpy(lst):
    arr = np.array(lst)
    return arr

#Calculates the average of each column
def calc_averages(list_of_rows):
    avg = np.average(list_of_rows, axis=0)
    return round(avg[0], 4), round(avg[1], 4)

#Changes array of rows into list of columns
def transpose(input):
    array = np.array(input).T
    return array

def run():
    if (False):
        list_of_rows = read_data("data.txt")
        print(list_of_rows)
    if (False): print(convertToNumpy(read_data("data.txt")))
    if (True):
        col1_avg, col2_avg = calc_averages(convertToNumpy(read_data("data.txt")))
        print(col1_avg, col2_avg)
    if (True):
        print(transpose(convertToNumpy(read_data("data.txt"))))
run()

