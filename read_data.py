import os
import sys
import pandas as pd
import numpy as np
try:
        import matplotlib.pyplot as plt
except:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
import heartpy as hp
import utils
import csv

"""
#fileSourse =  str(sys.argv[1])
#fileName = str(sys.argv[2])
fileSourse =  [
"C://Users//msi-pc//Downloads//HABIT//5.23-//batch stop 2//6.20//acce",
"C://Users//msi-pc//Downloads//HABIT//5.23-//batch stop 2//6.20//gyro",
"C://Users//msi-pc//Downloads//HABIT//5.23-//batch stop 2//6.20//ppg",
"C://Users//msi-pc//Downloads//HABIT//5.23-//batch stop 2//6.21//acce",
"C://Users//msi-pc//Downloads//HABIT//5.23-//batch stop 2//6.21//gyro",
"C://Users//msi-pc//Downloads//HABIT//5.23-//batch stop 2//6.21//ppg",
"C://Users//msi-pc//Downloads//HABIT//5.23-//batch stop 2//6.22//acce",
"C://Users//msi-pc//Downloads//HABIT//5.23-//batch stop 2//6.22//gyro",
"C://Users//msi-pc//Downloads//HABIT//5.23-//batch stop 2//6.22//ppg",
]
fileName = [
"6.20-stop-acce-batch-2",
"6.20-stop-gyro-batch-2",
"6.20-stop-ppg-batch-2",
"6.21-stop-acce-batch-2",
"6.21-stop-gyro-batch-2",
"6.21-stop-ppg-batch-2",
"6.22-stop-acce-batch-2",
"6.22-stop-gyro-batch-2",
"6.22-stop-ppg-batch-2"]

for i in range(0, len(fileSourse)):
	utils.combine_raw_data(fileSourse[i],fileName[i])

"""


fileSourse = "test//"
outputFile = "output//"
fileName = "2020-6-24-14-42"

file = np.genfromtxt(fileSourse+fileName+'.csv',delimiter=',' )        
file = np.transpose(np.unique(file, axis=0))
file[0]=file[0]-18000000

#utils.calc_heart_rate(file)
utils.plot_sensor_data(fileName, file, outputFile,2)
plt.show()



