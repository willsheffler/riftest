copy directory /work/sheffler/pub/rif_test

read through and appropriately modify input/rif_hier_template.flags

ONLY on machines with at least 128GB ram and a LONG time limit (digs27-34), run this to generate the RIF data. The calculation in the unchanged file should take about two hours on one of those digs, if you have the whole machine to yourself and use OMP_NUM_THREADS=32

OMP_NUM_THREADS=32 nice /work/sheffler/rosetta/rif_dock/source/cmake/build_omp/rif_hier @input/rif_hier_template.flags

you should have a bunch of files in your "outdir" now, one if which should be a big .rif.gz file. you must now run:

/work/sheffler/rosetta/rif_dock/source/cmake/build_omp/scheme_make_bounding_grids @input/make_bounding_grids_hack.flags -scheme:base_xmap_files <path to your .rif.gz file>

this should take a little while and generate 5 more files called WHATEVER.rif.gz_BOUNDING_HACK_RIF_{16,8,4,2,1}.xmap.gz

now you can run the docking with various scaffolds as follows. you can probably run this on any of the lab machines, though you will run into time limit issues... using 40 threads, an 8 hour time limit becomes more like a 15 minute time limit. Because reading in the rif takes some time, it'll be best to batch scaffolds together as much as you can without running into time limits.

OMP_NUM_THREADS=40 nice /work/sheffler/rosetta/rif_dock/source/cmake/build_omp/rif_dock_test @input/rif_dock_template.flags