import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from PyAstronomy.pyTiming import pyPDM
import plotly.graph_objects as go
import math

data_1002 = pd.read_csv('20231002_p4/20231002.csv')
data_1023 = pd.read_csv('20231023_p4/20231023.csv')
data_1026 = pd.read_csv('20231026_p2/20231026.csv')
data_1027 = pd.read_csv('20231027_p3/20231027.csv')
data_1028 = pd.read_csv('20231028_p3/20231028.csv')

time = [data_1002['J.D.-2400000'], data_1023['J.D.-2400000'], data_1026['J.D.-2400000'], data_1027['J.D.-2400000'], data_1028['J.D.-2400000']]
flux = [data_1002['rel_flux_T1'], data_1023['rel_flux_T1'], data_1026['rel_flux_T1'], data_1027['rel_flux_T1'], data_1028['rel_flux_T1']]
mag = [data_1002['Source_AMag_T1'], data_1023['Source_AMag_T1'], data_1026['Source_AMag_T1'], data_1027['Source_AMag_T1'], data_1028['Source_AMag_T1']]
mag_err = [data_1002['Source_AMag_Err_T1'], data_1023['Source_AMag_Err_T1'], data_1026['Source_AMag_Err_T1'], data_1027['Source_AMag_Err_T1'], data_1028['Source_AMag_Err_T1']]
err = [data_1002['rel_flux_err_T1'], data_1023['rel_flux_err_T1'],data_1026['rel_flux_err_T1'], data_1027['rel_flux_err_T1'], data_1028['rel_flux_err_T1']]


# PDM

fig4 = {}
# f1 = {}
# f2 = {}
# t1 = {}
# t2 = {}
modetxt = ['period', 'frequency']
descrx = ['Period (days)', 'Frequency (1/day)']
moden = 0
cover = 3
periodsearch = [1, 1000, 0.1]

x = pd.concat(time[0:])
y = pd.concat(mag[0:])

bins = math.floor(np.sqrt(len(x)))

#     bins = 10

#     x = np.random.rand(100)
#     print(x)
#     y = numpy.sin(x*2.0*numpy.pi*3.0 + 1.7)

#     print(y)

#     Get a ``scanner'', which defines the frequency interval to be checked.
#     Alternatively, also periods could be used instead of frequency.

S = pyPDM.Scanner(minVal=periodsearch[0], maxVal=periodsearch[1], dVal=periodsearch[2], mode=modetxt[moden])

# Carry out PDM analysis. Get frequency array
# (f, note that it is frequency, because the scanner's
# mode is ``frequency'') and associated Theta statistic (t).
# Use 10 phase bins and 3 covers (= phase-shifted set of bins).
P = pyPDM.PyPDM(x,y)

f1, t1 = P.pdmEquiBinCover(bins, cover, S)

# For comparison, carry out PDM analysis using 10 bins equidistant
# bins (no covers).
f2, t2 = P.pdmEquiBin(bins, S)