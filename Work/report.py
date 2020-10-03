# report.py
#
# Exercise 2.4-3.2
import fileparse
import stock
import tableformat
from portfolio import Portfolio

def read_portfolio(filename, **opts):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
   with open(filename) as lines:
        return Portfolio.from_csv(lines, **opts)
    
def read_prices(filename):
    '''
    Returns the dictionary of stockholder name as the key and price as the value
    '''
    with open(filename) as lines:
        return dict(fileparse.parse_csv(lines, types=[str, float], has_headers=False))
    
    
def make_report(portfolio, prices):
    '''
    Collects data from the dictionary and the list and creates 
    new list of combined columns
    '''
    report = []
    for p in portfolio:
        tupl = (p.name, p.shares, prices[p.name], prices[p.name] - p.price)
        report.append(tupl)
    return report


def print_report(report, formatter):
    '''
    Prints beautifully formatted table
    '''
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in report:
        #line = '$' + '%0.2f' % price
        #print(f'{name:>10s} {shares:>10d} {line:>10s} {change:>10.2f}')
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)
    
    
def portfolio_report(portfolio_filename, prices_filename, fmt='txt'):
    '''
    Make a stock report given portfolio and price data files.
    '''
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)   
    
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)


def main(args):
    if len(args) != 4:
        raise SystemExit('Usage: %s portfile pricefile' % args[0])
    portfolio_report(args[1], args[2], args[3])
    
    
if __name__ == '__main__':
    import sys
    main(sys.argv)