##### ----- Imports ----- #####
import pandas as pd

def get_data_from_web(url):
    data = pd.read_csv(url)
    return data

##### ----- Variables ----- #####
data = [['A1', 28], ['A2', 32], ['A3', 1], ['A4', 0],
        ['A5', 10], ['A6', 22], ['A7', 30], ['A8', 19],
		['B1', 145], ['B2', 27], ['B3', 36], ['B4', 25],
		['B5', 9], ['B6', 38], ['B7', 21], ['B8', 12],
		['C1', 122], ['C2', 87], ['C3', 36], ['C4', 3],
		['D1', 0], ['D2', 5], ['D3', 55], ['D4', 62],
		['D5', 98], ['D6', 32]]

pd = get_data_from_web('https://nyu-cds.github.io/courses/data/houseelf_earlength_dna_data.csv')

##### ----- Functions ----- #####
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