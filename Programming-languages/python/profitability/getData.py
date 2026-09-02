import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

##### Dataset of key values #####
''' Takes the first link when you search (input) on proff '''
def getLink(input):
    #Scrape
    URL = 'https://www.proff.dk/branches%C3%B8g?q=' + str(input)
    response = requests.get(URL)
    contents = response.text
    soup = BeautifulSoup(contents, 'html.parser')
    soupList = soup.find_all('section', class_='panel full-width') 
    soupList = soup.find_all('div', class_='search-block-info') 
    soupList = soupList[0]
    
    #Regular expressions
    string = str(soupList)
    string = re.search(r'<a(?:.*?)>(.*?)<\/a>', string).group(0)
    string = re.search(r'href="(.*?)"', string).group(0)
    string = re.sub(r'href=', '', string)
    string = re.sub(r'\"', '', string)
    string = 'https://www.proff.dk' + string
    return (string)

''' returns the source code from the regnskab page '''
def getHtml(input):
    url = re.sub(r'firma', 'regnskab', input)
    response = requests.get(url)
    contents = response.text
    soup = BeautifulSoup(contents, 'html.parser')
    return soup

''' runs getLink and getHtml 
    returns a html code for regnskab page '''
def runHtml(input):
    link = getLink(input)
    html = getHtml(link)
    return html
runHtml('carlsberg')

''' returns a list of list like: [row=(label), col=(date), value=(value)]
    ready to be added to dataframe '''
def getData(input):
    html = runHtml(input)
    html = html.find_all('tr', class_='detailed')
    lst = []
    for elm in html:
        label = re.search(r'(<span(?:.*?)>).*(<\/span>)', str(elm)).group(0)
        label = re.sub(r'<span>', "", label)
        label = re.sub(r'<\/span>', "", label)
        data = re.findall(r'{(?:.*?)}', str(elm))
        valueList = []
        for point in data:
            date = re.search(r'\d{4}', point)
            date = date.group(0)
            value = re.search(r'"value":.*}', point).group(0)
            value = re.sub(r'"value":', '', value)
            value = re.sub(r'}', '', value)
            if value == 'null':
                value = 0.0
            valueList.append([str(label), int(date), float(value)])
        lst.append(valueList)
    return lst

''' returns list of all the different labels '''
def getRowLabels():
    n = getData('carlsberg')
    lst = []
    for elm in n:
        lst.append((elm[0][0]))
    return lst

''' creates a dataframe with:
        col = last three years
        rows = labels
    Then values get's inserted 1 by 1 '''
def createDataframe(input, currentYear):
    rowLabels = getRowLabels()
    col = [currentYear, currentYear-1, currentYear-2]
    df = pd.DataFrame(np.zeros((len(rowLabels), len(col))), index = rowLabels, columns=col)
    for elm in getData(input):
        for point in elm:
            label = point[0]
            year = point[1]
            value = point[2]
            if year in col:
                df.at[label, year] = round(value/1000)
    return df

##### dataset for training #####
''' Creates a list of percentage increase'''
def modifyToX(inp):
    lst = []
    for i in range(0, len(inp.index)):
        dat2020 = float(inp.iloc[i, 1])
        dat2019 = float(inp.iloc[i, 2])
        if dat2020 == 0 or dat2019 == 0:
            dat = .0
        else: 
            dat = (dat2020 - dat2019)/dat2019
        lst.append(dat)
    return lst

'''If rate of return is positive return 1, else 0'''
def modifyToY(inp):
    # Primært resultat
    p2021 = inp.iloc[5, 0]
    p2020 = inp.iloc[5, 1]

    # Passiver i alt
    a2021 = inp.iloc[54, 0]
    a2020 = inp.iloc[54, 1]

    # Afkastningsgrad
    ag2021 = (p2021 * 100) / a2021 
    ag2020 = (p2020 * 100) / a2020
    
    increase = (ag2021 - ag2020) / ag2020
    if increase > 0:
        return 1
    else:
        return 0
    
def createDfForPipeline(input):
    lst = []
    for elm in input:
        print(elm)
        dataFrame = createDataframe(elm, 2021)
        xList = modifyToX(dataFrame)
        y = modifyToY(dataFrame)
        row = [elm] + [y] + xList
        lst.append(row)
    df = pd.DataFrame(lst)
    return df

print(createDfForPipeline(['lego', 'carlsberg']))

