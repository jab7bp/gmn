from ROOT import *
from beam_variables import *
import numpy as np

def plot_Q2(runnum, rootFiles, save):

	global hist_Q2, hQ2_stack, Q2_stack_can, hQ2_mean

	Q, Q2, hQ2, hQ2_mean = [], [], [], []

	Me = (0.0005)*0.938

	bins = 200

	stack_title = "Momentum transfer, Q-squared"
	Q2_stack_can = TCanvas("Q2_stacked_can", stack_title)
	hQ2_stack = THStack("hQ2_stack", stack_title)

	lineColor = 1	
	

	for run in runnum:
		E = BeamEnergyFromRun(int(run))

		index = runnum.index(run)
		min_bin = qBinFromRun(int(run))[0]
		max_bin = qBinFromRun(int(run))[1]

		cut_min = CutFromRun(int(run))[0]
		cut_max = CutFromRun(int(run))[1]


		tCh_Q2 = TChain("T")
		tCh_Q2.Add(rootFiles[index])

		hist_Q2 = TH1F('hist_Q2_' + run, 'Q-Squared Transfer', bins, min_bin, max_bin)

		cut1 = TCut("bb.gem.track.nhits[0] > 3")
		cut2 = TCut("(bb.sh.e + bb.ps.e)/bb.tr.p > " + str(cut_min) + " && (bb.ps.e + bb.ps.e)/bb.tr.p < " + str(cut_max))

		all_cuts = cut1 + cut2

		###Variables: E = Beam Energy; bb.tr.p[0] = scattered electron energy; bb.tr.pz[0] = scattered electron energy in "z"
		###Mp = mass of proton; angle = (bb.tr.pz[0]/bb.tr.p[0])

		eq_Q2 = "2*%f*bb.tr.p[0]*(1-cos(bb.tr.pz[0]/bb.tr.p[0]))>> hist_Q2_" + run


		tCh_Q2.Draw(eq_Q2 % E, all_cuts)

		#PLOT DISPLAY STUFF#
		if(lineColor == 5):
			lineColor+=1
		hist_Q2.SetLineColor(lineColor)
		lineColor+=1

		##Store calculated variables in arrays##
		hQ2.append(hist_Q2)
		hQ2_stack.Add(hist_Q2)
		#print(hist_Q2.GetMean(1))

	
	hQ2_stack.Draw("nostack")
	Q2_stack_can.Update()

	if(save):
		Q2_stack_can.Print("./momentum-transfers_plot.pdf")
		
	return 1