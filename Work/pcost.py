# pcost.py
#
# Exercise 1.27
import report

def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    portfolio = report.read_portfolio(filename)
    return portfolio.total_cost
    
    
def main(args):
    if len(args) != 2:
        raise SystemExit('Usage: %s portfoliofile' % args[0])
    print('Total cost:', portfolio_cost(args[1]))


if __name__ == '__main__':
    import sys
    main(sys.argv)