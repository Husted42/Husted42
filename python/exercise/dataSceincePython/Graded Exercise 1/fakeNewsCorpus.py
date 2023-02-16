import csv 
import copy
data = 'news_sample.csv'

with open('news_sample.csv', 'r') as csv_in, open('redacted_news_sample.csv','w', newline = '') as csv_out :
    csv_reader = csv.reader(csv_in)
    csv_writer = csv.writer(csv_out)
    for row in csv_reader:
        new_row = [cell.lower() for cell in row]
        csv_writer.writerow(new_row)
