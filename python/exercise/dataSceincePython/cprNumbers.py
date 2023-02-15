import re
import pandas as pd

data = '''1307026153 
2308134469 
1211004254'''

def group():
    df = pd.DataFrame(
        columns = ["DD", "MM", "YY", "IIII"]
    )
    pattern = re.compile('(^\d{2})(\d{2})(\d{2})(\d{4})')
    data_lines = data.split('\n')
    for data_line in data_lines:
        match = pattern.search(data_line)
        if match: 
            newRow = [str(match.group(1)), (match.group(2)),
                      (match.group(3)), (match.group(4))] 
            df.loc[len(df)] = newRow
    print(df)
group()
