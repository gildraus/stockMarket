import requests
from datetime import datetime as dt
from pprint import pprint as pp

file1 = open("StochRSI(GOLD).txt", "w")
file2 = open("GOLD.txt", "w")

def request_alphavantage(**kwargs):
    params = {'apikey': 'N386S2HHGOQX87QB'}
    params.update(kwargs)
    return requests.get('https://www.alphavantage.co/query', params=params).json()


def data2df_cur(data):
    #comment
    #sa
    #ss
    '''
    currency data
    '''
    df = {'datetime': [], 'Open': [], 'High': [], 'Low': [], 'Close': [], 'Volume': []}
    for k, v in data.items():
        #    df['datetime'].append(k)
        df['datetime'].append(dt.strptime(k, '%Y-%m-%d'))
        df['Open'].append(float(v['1b. open (USD)']))
        df['High'].append(float(v['2b. high (USD)']))
        df['Low'].append(float(v['3b. low (USD)']))
        df['Close'].append(float(v['4b. close (USD)']))
        df['Volume'].append(v['5. volume'])
    return df


def data2df_stk(data):
    '''
    stock data
    '''
    df = {'datetime': [], 'Open': [], 'High': [], 'Low': [], 'Close': [], 'Volume': []}
    for k, v in data.items():
        #    df['datetime'].append(k)
        df['datetime'].append(dt.strptime(k, '%Y-%m-%d'))
        df['Open'].append(float(v['1. open']))
        df['High'].append(float(v['2. high']))
        df['Low'].append(float(v['3. low']))
        df['Close'].append(float(v['4. close']))
        df['Volume'].append(v['5. volume'])
    return df

def data2df_stochRSI(data):
    '''
    stochRSI
    '''
    df = {'datetime': [], 'FastK': [], 'FastD': []}
    for k, v in data.items():
        #    df['datetime'].append(k)
        df['datetime'].append(dt.strptime(k, '%Y-%m-%d'))
        df['FastK'].append(float(v['FastK']))
        df['FastD'].append(float(v['FastD']))
    return df



#g = request_alphavantage(function='TIME_SERIES_DAILY', symbol='ETHUSD', outputsize='full')

#data1 = g['Time Series (Daily)']

#dk = data2df_stk(data1)

s = request_alphavantage(function='STOCHRSI', symbol='ETHUSD', interval='daily', series_type='close', time_period='100', fastkperiod='3', fastdperiod='3', fastdmatype='1')

data3 = s['Technical Analysis: STOCHRSI']

dt = data2df_stochRSI(data3)



for i in range(800):
    file1.write("FastK: ")
    file1.write(str(dt['FastK'][i]))
    file1.write("\n")
    file1.write("FastD: ")
    file1.write(str(dt['FastD'][i]))
    file1.write("\n")
    file1.write("datetime: ")
    file1.write(str(dt['datetime'][i]))
    file1.write("\n")
    file1.write("\n")


#file1.writelines()
file1.close()
file2.close()
