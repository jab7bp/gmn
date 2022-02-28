#include "TString.h"
#include "TObjString.h"
#include "TObjArray.h"
#include <fstream>

apparatus = "sbs"
apparatus_LC = apparatus.lower()
apparatus_UC = apparatus.upper()

protorootfile = "$OUT_DIR/" + apparatus + "gem_replayed_XXXXX_stream0_seg0_0.root" + "\n"

outfile = open(apparatus_UC + "GEM_ped_and_commonmode.cfg", "w+")

nmodules = 31

## 0 -> UVa XY GEM, 1 -> UVa UV GEM, 2 -> INFN GEM

m0 = m1 = m2 = m3 = m4 = m5 = m6 = m7 = m8 = m9 =\
m10 = m11 = m12 = m13 = m14 = m15 = m16 = m17 = m18 = m19 =\
m20 = m21 = m22 = m23 = m24 = m25 = m26 = m27 = m28 = m29 = \
m30 = m31 = ["UVa XY"]

m0 = m1 = m2 = m3 = [m0[0], "Inline Layer 1"]
m4 = m5 = m6 = m7 = [m4[0], "Inline Layer 2"]
m8 = m9 = m10 = m11 = [m8[0], "Inline Layer 3"]
m12 = m13 = m14 = m15 = [m12[0], "Inline Layer 4"]
m16 = m17 = m18 = m19 = [m16[0], "Inline Layer 5"]
m20 = m21 = m22 = m23 = [m20[0], "Inline Layer 6"]
m24 = m25 = m26 = m27 = [m24[0], "Pol. R Layer 0"]
m28 = m29 = m30 = m31 = [m28[0], "Pol. R Layer 1"]

m0 = m4 = m8 = m12 = m16 = m20 = m24 = m28 = [m0[0], m0[1], "G0"]
m1 = m5 = m9 = m13 = m17 = m21 = m25 = m29 = [m1[0], m1[1], "G1"]
m2 = m6 = m10 = m14 = m18 = m22 = m26 = m30 = [m2[0], m2[1], "G2"]
m3 = m7 = m11 = m15 = m19 = m23 = m27 = m31 = [m3[0], m3[1], "G3"]


### PRINT PROTOROOTFILE ###

outfile.write("protorootfile " + protorootfile)

#Define the histograms here:

#####     COMMONMODES    #####

outfile.write("\n########   Commonmode histograms    ########\n")
for module in range(0, nmodules+1):
	outfile.write("newpage 3 2\n")
	outfile.write("title Module %i Common-mode (%s - %s - %s)\n" % (module, (locals()["m" +str(module)])[0], (locals()["m" +str(module)])[1], (locals()["m" +str(module)])[2]))
	outfile.write("hcommonmodeU_sorting_%s_gem_m%i -drawopt colz\n" % (apparatus_LC, module))
	outfile.write("hcommonmodeU_danning_%s_gem_m%i -drawopt colz\n" % (apparatus_LC, module))
	outfile.write("hcommonmodeU_diff_%s_gem_m%i -drawopt colz\n" % (apparatus_LC, module))
	outfile.write("hcommonmodeV_sorting_%s_gem_m%i -drawopt colz\n" % (apparatus_LC, module))
	outfile.write("hcommonmodeV_danning_%s_gem_m%i -drawopt colz\n" % (apparatus_LC, module))
	outfile.write("hcommonmodeV_diff_%s_gem_m%i -drawopt colz\n" % (apparatus_LC, module))
	outfile.write("\n")


outfile.write("\n########   Pedestal histograms    ########\n")

#####    PEDESTALS    #######
for module in range(0, nmodules+1):
	outfile.write("newpage 4 4\n")
	outfile.write("title Module %i Pedestals (%s - %s - %s)\n" % (module, (locals()["m" +str(module)])[0], (locals()["m" +str(module)])[1], (locals()["m" +str(module)])[2]))
	outfile.write("hpedrmsU_distribution_%s_gem_m%i \n" % (apparatus_LC, module))
	outfile.write("hpedmeanU_distribution_%s_gem_m%i \n" % (apparatus_LC, module))
	outfile.write("hpedrmsV_distribution_%s_gem_m%i \n" % (apparatus_LC, module))
	outfile.write("hpedmeanV_distribution_%s_gem_m%i \n" % (apparatus_LC, module))

	outfile.write("hpedrmsU_by_strip_%s_gem_m%i -nostat \n" % (apparatus_LC, module))
	outfile.write("hpedmeanU_by_strip_%s_gem_m%i -nostat \n" % (apparatus_LC, module))
	outfile.write("hpedrmsV_by_strip_%s_gem_m%i -nostat \n" % (apparatus_LC, module))
	outfile.write("hpedmeanV_by_strip_%s_gem_m%i -nostat \n" % (apparatus_LC, module))

	#these are somewhat redundant and expensive and slow to render:
	outfile.write("hrawADCs_by_stripU_%s_gem_m%i -drawopt colz -nostat \n" % (apparatus_LC, module))
	outfile.write("hrawADCs_by_stripV_%s_gem_m%i -drawopt colz -nostat \n" % (apparatus_LC, module))
	#hpedestalU_bb_gem_m0 -drawopt colz -nostat
	#hpedestalV_bb_gem_m0 -drawopt colz -nostat

	outfile.write("hADCpedsubU_%s_gem_m%i -drawopt colz -nostat \n" % (apparatus_LC, module))
	outfile.write("hADCpedsubV_%s_gem_m%i -drawopt colz -nostat \n" % (apparatus_LC, module))
	#hrawADCpedsubU_bb_gem_m0 -drawopt colz -nostat
	#hrawADCpedsubV_bb_gem_m0 -drawopt colz -nostat

	outfile.write("hCommonModeMean_by_APV_U_%s_gem_m%i -drawopt colz -nostat \n" % (apparatus_LC, module))
	outfile.write("hCommonModeMean_by_APV_V_%s_gem_m%i -drawopt colz -nostat \n" % (apparatus_LC, module))
	outfile.write('macro plotfitgaus.C("hADCpedsubU_allstrips_%s_gem_m%i"); \n' % (apparatus_LC, module))
	outfile.write('macro plotfitgaus.C("hADCpedsubV_allstrips_%s_gem_m%i"); \n' % (apparatus_LC, module))
	outfile.write("\n")

outfile.close()