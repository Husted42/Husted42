import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

currentYear = 2021

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

''' creates the dataframe with:
        col = last three years
        rows = labels
    Then values get's inserted 1 by 1 '''
def createDataframe(input):
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

print(createDataframe('lego'))