import pandas as pd
import numpy as np
#Gloabl variables
globalNp_array = np.arange(6).reshape((3,2))
globalPd_dataframe = pd.DataFrame(
        globalNp_array,
        index = ["a", "b", "c"],
        columns = ["col1", "col2"])

#Converting 1D numpy array to pandas series
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

def britishTest():
    df = pd.read_csv(r'C:\C\gitHub\code\python\exercise\data\british-english.csv', keep_default_na=False, header=None)
    df.columns= ['words']
    print(df)
    #select rows starting with letter A
    df.loc[df['words'].str.startswith('A')]

def run():
    if (False): print(convertList())
    if (False): print(convertDic())
    if (False): printPandaCal()
    if (False): categories()
    if (False): printDataframeList()
    if (False): printDataframeDicOfList()    
    if (False): printDataframeSetup()    
    if (False): indexInData()
    if (False): britishTest()
run()