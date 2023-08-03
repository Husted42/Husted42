##### ----- Imports ----- #####
import numpy as np
from numpy import random
import pandas as pd

def get_data_from_web(url):
    data = pd.read_csv(url)
    return data

##### ----- Variables ----- #####
globalNp_array = np.arange(6).reshape((3,2))
globalPd_dataframe = pd.DataFrame(
        globalNp_array,
        index = ["a", "b", "c"],
        columns = ["col1", "col2"])

data = [['A1', 28], ['A2', 32], ['A3', 1], ['A4', 0],
	    ['A5', 10], ['A6', 22], ['A7', 30], ['A8', 19],
		['B1', 145], ['B2', 27], ['B3', 36], ['B4', 25],
		['B5', 9], ['B6', 38], ['B7', 21], ['B8', 12],
		['C1', 122], ['C2', 87], ['C3', 36], ['C4', 3],
		['D1', 0], ['D2', 5], ['D3', 55], ['D4', 62],
		['D5', 98], ['D6', 32]]

pd = get_data_from_web('https://nyu-cds.github.io/courses/data/houseelf_earlength_dna_data.csv')

##### ----- Functions - Numpy ----- #####
''' Showcase of weigthed probabilty '''
def weightedProb():
    X = ['a', 'b', 'c']
    P = [0.2, 0.3, 0.5]
    return np.random.choice(X, p=P)

''' Test by many samples '''
def monteCarloCheck():
    a, b, c = 0, 0, 0
    for i in range (0, 1000):
        res = weightedProb()
        if res == 'a': a += 1
        elif res == 'b': b += 1
        else: c += 1
    sum = a+b+c
    return (round(a/sum, 1), round(b/sum, 1), round(c/sum, 1))

''' The probality for a computer to be sold '''
def computerShop():
    computers = ['Dell', 'XP', 'Lenovo', 'Asus', 'Mac']
    weights = np.array([56433, 25463, 20455, 65068, 18476])
    weights = weights / sum(weights) # Get percentage
    return np.random.choice(computers, p=weights, size=(3,4), replace=True)

def intoArray ():
    print("----- Introduction to arrays in numpy -----")
    a = np.array([1,2,3,4])
    b = np.array([1,2,3,4], float)
    c = np.array((1,2,3,4))
    print (str(a)+ " " +str(b)+ " " +str(c))
    print("Arrange:    " + str(np.arange(2.0, 2.4, 0.1)))
    print("Zeros/Ones: " + str(np.zeros(4)) + str(np.ones(4)))
    print("Calculations:")
    print(a)
    print(3*a)
    print(a+a)
    print(a*a)
    print(a/a)
    print(np.cos(a))
    print("Random arrays:")
    print(np.random.rand(3))
    print(np.random.rand(3,5))
    print(np.random.randint(1,3,5))
    print("")

def multiArray ():
    print("----- Multidimensional arrays -----")
    a = np.array([[1,2,3,4], [2,3,4,5]])
    print(a)
    print("shape:" + str(a.shape))

def e1 ():
    print("----- e1 -----")
    c = np.average( np.random.randint(1,7,10000) + np.random.randint(1,7,10000) )
    print (c)
    print ("")

##### ----- Functions - Pandas ----- #####
def convertList():
    np_array = np.array([1., 2., 3.,])
    pd_series = pd.Series(np_array, index=["line 1", "line 2", "line 3" ])
    return pd_series

def convertDic():
    pd_series = pd.Series({'a':1.0, 'b':2.0, 'c':3.0})
    return pd_series

def printPandaCal():
    #Series
    pd_series = convertList()
    
    #prints
    print(pd_series * 2)
    print(np.log(pd_series))
    print(pd_series["line 2"])
    print((pd_series + pd_series[1:]).dropna())

def dataFrame():
    np_array = np.arange(6).reshape((3,2))
    df = pd.DataFrame(np_array, index=['a', 'b', 'c'],
                  columns=['col1', 'col2'])
    return df

def categories():
    print()
    print("Print categories: ")
    series = pd.Series(['male', 'female', 'female'], dtype="category")
    series = pd.Series(['male', 'female', 'female']).astype('category')
    series = pd.Series(pd.Categorical(['male', 'female', 'female']))
    series = pd.Series(pd.Categorical(['male', 'female', 'female'],
                                    categories=['female', 'male']))
    print(series.cat.categories)

def printDataframeList ():
    print()
    print("Print dataframe of list: ")
    np_array = np.arange(6).reshape((2,3))
    df = pd.DataFrame(np_array, index=['a', 'b'], columns=['col1', 'col2', 'col3'])
    print(df)

def printDataframeDicOfList ():
    print()
    print("Print dataframe list of dictonaries: ")
    list_of_dicts = [{'col1': 0, 'col2': 1, 'col3': 2},
                 {'col1': 3, 'col2': 4, 'col3': 5}]
    df = pd.DataFrame(list_of_dicts, index=['a', 'b'])
    print(df)

def printDataframeSetup():
    df = pd.DataFrame(
        globalNp_array,
        index = ["a", "b", "c"],
        columns = ["col1", "col2"])
    print(df.index)
    print(df.columns)
    print(df.values)

def indexInData():
    df = dataFrame()
    #Selecting by labels
    print("Selecting by labels: ")
    print(df.loc['a':'b'])
    
    #Selecting by labels 2
    print()
    print("Selecting by labels 2")
    print(df.loc['a':'b', :'col1'])

    #Selecting wit a boolean array
    print()
    print("Selecting wit a boolean array")
    print(df.loc[:, 'col1']>2)
    print()
    df.loc[df.loc[:, 'col1']>2] = 0
    print(df)

def total(inp):
	num = 0
	for elm in inp: 
		num = num + elm[1]
	return num

''' Input: (data, letter) '''
def totalSite(inp, l): 
	num = 0
	for elm in inp:
		if elm[0][0] == 'C':
			num = num + elm[1]
	return num

def earSize(inp):
    if inp <= 10: return 'small'
    else: return 'large'

def gcContent(inp):
    g = inp.count('G')
    c = inp.count('C')
    return c+g / len(inp)

def newTable(inp):
    tab = inp.copy(deep = True)
    tab['earlength'] = inp.apply(lambda row : earSize(row['earlength']), axis = 1)
    tab['dnaseq'] = inp.apply(lambda row : gcContent(row['dnaseq']), axis = 1)
    return tab

##### ----- Calls ----- #####
## -- Call: Numpy -- ##
print('Test for weighted probabilty: ', monteCarloCheck() == (0.2, 0.3, 0.5))
print('\n Sample from computerShop :\n', computerShop())

def run ():
    if (True): intoArray()
    if (True): e1()
    if (True): multiArray()
run()

## -- Call: Pandas -- ##
def run1():
    if (False): print(convertList())
    if (False): print(convertDic())
    if (False): printPandaCal()
    if (False): categories()
    if (False): printDataframeList()
    if (False): printDataframeDicOfList()    
    if (False): printDataframeSetup()    
    if (False): indexInData()
run1()

def run2():
    if (True):
        print('How many sites are there?')
        print(len(data), '\n\n')

        print('How many birds were counted at the 7th site?')
        print(data[6][1], '\n\n')

        print('How many birds were counted at the last site?')
        print(data[len(data)-1][1], '\n\n')

        print('What is the total number of birds counted across all sites?')
        print(total(data), '\n\n')

        print('What is the average number of birds seen on a site?')
        print(round(total(data)/len(data), 2), '\n\n')

        print('What is the total number of birds counted on sites with codes beginning with C?')
        print(totalSite(data, 'c'), '\n\n')

        print('Imports the data into a data structure of your choice')
        print(pd, '\n\n')

        print('For each row in the dataset checks to see if the ear length is large (>10 cm) or small (<=10 cm) and determines the GC-content of the DNA sequence (i.e., the percentage of bases that are either G or C)')
        print(earSize(pd['earlength'].iloc[0]), gcContent(pd['dnaseq'].iloc[0]), '\n\n')

        print('Store the information in a table')
        pd2 = newTable(pd)
        print(pd2, '\n\n')

        print('Prints the average GC-content for both large-eared elves and small-eared elves to the screen.')
        print(round(pd2.loc[pd2['earlength'] == 'small', 'dnaseq'].mean(), 2))
        print(round(pd2.loc[pd2['earlength'] == 'large', 'dnaseq'].mean(), 2))