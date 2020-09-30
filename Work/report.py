# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {
                'name' : row[0],
                'shares' : int(row[1]),
                'price' : float(row[2])
            }
            portfolio.append(holding)
    return portfolio
    
def read_prices(filename):
    holding = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                holding[row[0]] = float(row[1])
            except IndexError:
                pass
            
    return holding
    
def make_report(portfolio, prices):
    report = []
    for p in portfolio:
        tupl = (p['name'], p['shares'], prices[p['name']], prices[p['name']] - p['price'])
        report.append(tupl)
    return report
    
portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)
    
headers = ('Name', 'Shares', 'Price', 'Change')
print(f'%10s %10s %10s %10s' %headers)
#print(f'{"":-<10s} {"":-<10s} {"":-<10s} {"":-<10s}')
print(('-' * 10 + ' ') * len(headers))

for name, shares, price, change in report:
    line = '$' + '%0.2f' % price
    print(f'{name:>10s} {shares:>10d} {line:>10s} {change:>10.2f}')