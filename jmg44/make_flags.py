import sys,os,glob

tplt = ""
with open(sys.argv[1]) as f:
	tplt = f.read()

print "using template:", sys.argv[1]
# print "===================================== TEMPLATE ============================================"
# print tplt
# print "==========================================================================================="

for d in sys.argv[2:]:
	if not os.path.isdir(d):
		print "ERROR! not a directory:",d
		break
	print "checking directory",d
	g = glob.glob( d+"/*.rif.gz" )
	g2 = glob.glob( d+"*/*_replonlybdry__atype1.rosetta_field.gz" )
	if len(g) != 1 or len(g2) != 1:
		print "glob error"
		break
	RIFTAG = os.path.basename(g[0])[:-7]
	RIFDIR = os.path.dirname(g[0])
	RIFRF  = g2[0][:-25]
	OUTDIR = "results/"+d
	# print "RIFTAG", RIFTAG
	# print "RIFDIR", RIFDIR
	# print "RIFRF ", RIFRF

	flags = tplt.replace( "RIFTAG", RIFTAG ).replace( "RIFDIR", RIFDIR ).replace( "RIFRF", RIFRF ).replace( "OUTDIR", OUTDIR )

	with open( d+"/"+RIFTAG+"_tplt_dock.flags", "w" ) as f:
		f.write( flags )
