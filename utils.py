import os, glob
import sys
import pandas as pd
import numpy as np
import csv
try:
        import matplotlib.pyplot as plt
except:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
import heartpy as hp
import dateutil

def plot_sensor_data(title, data, output, index):
    plot_data = pd.DataFrame({'Time':data[0],'data':data[index]},columns=['data','Time'])
    print(plot_data)
    plot_data['Time'] = pd.to_datetime(plot_data['Time'], unit='ms', utc=True)
    f = plt.figure(figsize=(12,5))
    plt.xlabel("time")
    plt.title(title)
    plt.plot(plot_data['Time'], plot_data['data'])
    plt.savefig(output+title+'.png')

def calc_heart_rate(data, plot=0):
    plot_data = pd.DataFrame({'Time':data[0],'data':data[1]},columns=['data','Time'])
    plot_data['Time'] = pd.to_datetime(plot_data['Time'], unit='ms', utc=True)
    filtered = hp.filter_signal(data[1], [0.7, 3.5], sample_rate=20, 
                            order=3, filtertype='bandpass')
    wd, m = hp.process(filtered, sample_rate = 20, 
                    high_precision=True, clean_rr=True)
    print(m['bpm'])
    if plot == 1:
        hp.plotter(wd, m)
    return wd, m

def combine_raw_data(path, filename):
    count = 0
    os.chdir(path)
    results = pd.DataFrame()
    for counter, current_file in enumerate(glob.glob("*.csv")):
        print(current_file)
        if os.stat(current_file).st_size != 0 :
            namedf = pd.read_csv(current_file, header=None, sep=",").drop_duplicates()
            print(namedf)
            results = pd.concat([results, namedf[1:]])
            count+=1
            print(count)
        else: 
            print(current_file+" has no data")
    results.to_csv(filename+'.csv', index=None, header=None, sep=",")

