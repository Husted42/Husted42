import re
import pandas as pd

data = '''1307026153 
2308134469 
1211004254
1517972564
151797-2564'''

def a(n):
    df = pd.DataFrame(
        columns = ["DD", "MM", "YY", "IIII"]
    )
    pattern = re.compile('(^\d{2})(\d{2})(\d{2})-?(\d{4})')
    data_lines = n.split('\n')
    for data_line in data_lines:
        match = pattern.search(data_line)
        if match: 
            newRow = [str(match.group(1)), (match.group(2)),
                      (match.group(3)), (match.group(4))] 
            df.loc[len(df)] = newRow
    return(df)

def b(n):
    cprNumber = n
    pattern = re.compile('(^\d{2})(\d{2})(\d{2})-?(\d{4})')
    match = pattern.search(cprNumber)
    A = int(match.group(4))
    B = int(match.group(3))
    if (A < 4000 and B < 100 ): return(1900)
    elif (4000 <= A < 5000 and B <= 36): return(2000)
    elif (4000 <= A < 5000 and 37 <= B <= 99): return(1900)
    elif (5000 <= A < 9000 and 00 <= B <= 57): return(2000)
    elif (5000 <= A < 9000 and 58 <= B <= 99): return(1800)
    elif (9000 <= A < 10000 and 00 <= B <= 36): return(2000)
    elif (9000 <= A < 10000 and 37 <= B <= 99): return(1900)
    else: return ("Error")

print(a(data))
print(b('1517972564'))