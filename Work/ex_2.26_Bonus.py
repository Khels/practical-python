import csv

def conv(sdate):
    return tuple([ int(s) for s in sdate.split('/') ])
    
f = open('Data/dowstocks.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)

types = [str, float, conv, str, float, float, float, float, int]
converted = [func(val) for func, val in zip(types, row) ]
record = dict(zip(headers, converted))

print(record)


#{'name': 'AA', 'price': 39.48, 'date': (6, 11, 2007), 'time': '9:36am', 
#'change': -0.18, 'open': 39.67, 'high': 39.69, 'low': 39.45, 'volume': 181800}