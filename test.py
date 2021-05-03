from pandas import datetime
from matplotlib import pyplot
import csv
def parser(x):
	return sample.resample('60Min', how=conversion, base=30)
 
series = read_csv('details.csv', header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
print(series.head())
series.plot()
pyplot.show()

series = read_csv('detailtemp.csv', header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
print(series.head())
series.plot()
pyplot.show()

series = read_csv('detailvol.csv', header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
print(series.head())
series.plot()
pyplot.show()
