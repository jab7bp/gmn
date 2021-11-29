beam_variables = dict()
#kin_var --> {Energy: {Current: [Run Numbers]}}
beam_variables = {1.92 : {1.0 : 11207, 2.0 : 11214,3.0 : 11218, 4.0 : 11226, 5.0 : 11228, 6.0: ''}, 
	  		5.56 : {1.0 : '', 2.0 : '',3.0 : '', 4.0 : '', 5.0 : '', 6.0: ''},
			3.70 : {1.0 : 11420, 2.0 : 11421,3.0 : 11422, 4.0 : 11423, 5.0 : 11424, 6.0: 11425},
			7.0 : {6.0: 99999},
			}

##Dictionary to specify targets for specific run energies
targets = dict()
targets = {	"LH2": [1.92, 3.70, 5.6],
			"Targ": [7.0],
			}

##Dictionary to speficy the Invariant Mass min and max histogram bin values for each run energy
bin_variables_w = dict()
bin_variables_w = {1.92: [0.4, 1.8],
				3.70: [0.7, 2.7],
				5.56: [],
				}

##Dictionary to specify the Q-Squared min and max histogram bin values for each energy
bin_variables_q = dict()
bin_variables_q = {1.92: [0.4, 1.0],
				3.70: [1.0, 5.0],
				5.56: [],
				}	
						

##Dictionary to specify the energy cut min and max for each run energy
cut_energy = dict()
cut_energy = {1.92: [0.6, 0.8],
			3.70: [0.78, 1.15],
			5.56: [],
			}

elastic_peak = dict()
elastic_peak = {1.92: [0.96, 1.1], 
			3.70: [1.4, 1.55],
			}


def BeamEnergyFromRun(run):
	for energy, current in beam_variables.items():
		if (run in current.values()):
			return energy

def CurrentFromRun(run):
	for energy, current, in beam_variables.items():
		if (run in current.values()):
			current_index = list(current.values()).index(run)
			return list(current.keys())[current_index]

def TargetFromRun(run):
	for target, energy in targets.items():
		if (BeamEnergyFromRun(run) in energy):
			return target

def WBinFromRun(run):
	E = BeamEnergyFromRun(run)
	if (E in bin_variables_w.keys()):
		bin_index = list(bin_variables_w.keys()).index(E)
		return list(bin_variables_w.values())[bin_index]
		

def qBinFromRun(run):
	E = BeamEnergyFromRun(run)
	if (E in bin_variables_q.keys()):
		bin_index = list(bin_variables_q.keys()).index(E)
		return list(bin_variables_q.values())[bin_index]


def CutFromRun(run):
	E = BeamEnergyFromRun(run)
	if (E in cut_energy.keys()):
		cut_index = list(cut_energy.keys()).index(E)
		return list(cut_energy.values())[cut_index]

def PeakMinMaxFromRun(run):
	E = BeamEnergyFromRun(run)
	if (E in elastic_peak.keys()):
		peak_index = list(elastic_peak.keys()).index(E)
		return list(elastic_peak.values())[peak_index]

print(PeakMinMaxFromRun(11207))
