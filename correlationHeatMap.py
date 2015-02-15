import datetime
import pandas as pd
import pandas.io.data
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import matplotlib as mpl

def main():
	#read tickers from textfile and remove \n
	tickers = [line.strip() for line in open('tickers.txt')]

	#set maximum viewing area
	pd.set_option('display.max_rows', 1000) 

	#data set
	df = pd.io.data.get_data_yahoo(tickers, 
                               start=datetime.datetime(2013, 1, 1), 
                               end=datetime.datetime(2014, 1, 1))['Adj Close']

	stockCorr = correlation(df)
	print stockCorr

	#writes correlations to CSV, change header and index to false for just data
	stockCorr.to_csv("output.csv", header=True, index=True, na_rep=" ")

	graph(stockCorr)

def correlation(df):
	#define returns
	rets = df.pct_change()
	#calculate correlation
	corr = rets.corr()
	return corr

def graph(corr):
	#graph correlations
	plt.imshow(corr, cmap='copper', interpolation='none', aspect='auto')
	plt.colorbar()
	plt.xticks(range(len(corr)), corr.columns, rotation='vertical')
	plt.yticks(range(len(corr)), corr.columns);
	plt.suptitle('Stock Correlations Heat Map', fontsize=15, fontweight='bold')
	plt.show()

main()