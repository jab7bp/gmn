import sys,os
import csv
import argparse
import numpy as np
import math
import inspect
import operator
import getpass
from root_tools import *


from ROOT import PyConfig
PyConfig.IgnoreCommandLineOptions = True
from ROOT import *

from beam_variables import *
from W import *
from Q2 import *

parser = argparse.ArgumentParser(description = 'HV current plots')
parser.add_argument('-runnum', '--runnum', nargs= '*', help = "Enter run numbers", type = str, required =False)
parser.add_argument('-plot', '--plotGEM', default = None, nargs ='*', help = "speficy which GEM to plot.", action = "store", type = str, required = False)
parser.add_argument('-s', '--save', default = False, action = "store_true", help = "Choose to save plot or not", required = False)
parser.add_argument('-n', '--name', default = None, help = "specify name of file", action = "store", type = str, required = False)
parser.add_argument('-q', '--qtrans', default = False, action = "store_true", help = "Choose whether or not to calculate momentum transfer q-squared", required = False)
parser.add_argument('-w', '--inv_mass', default = False, action = "store_true", help = "Choose whether or not to calculate invariant mass, W" , required = False)

#parser.add_argument('-current', '--current', nargs = '*', default = [0.0], action = "store", type = float, required = False)

args = parser.parse_args()

pi = np.pi

if(getpass.getuser() == "a-onl")
	rootFile_dir = "/adaqfs/home/a-onl/sbs/Rootfiles/"
else:
	rootFile_dir = "/Users/john/UVa/SBS/analysis/rootFiles/"
prefix = "gmn_replayed_"
postfix = "_stream0_seg0_0.root"

rootFiles = []
TFiles = []

runnum = args.runnum
save = args.save
name = args.name
qtrans = args.qtrans
inv_mass = args.inv_mass

for run in runnum:
	rootFiles.append(rootFile_dir + prefix + run + postfix)
	TFiles.append(TFile(rootFiles[runnum.index(run)]))

if(inv_mass):
	plot_W(runnum, rootFiles, save, name, qtrans)

if(qtrans):
	plot_Q2(runnum, rootFiles, save)


input("Enter a key to stop.")