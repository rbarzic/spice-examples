# Makefile for osu_soc/inverter

CELL=ringosc
FIX_SPICE_NETLIST?=../../scripts/fix_spice_netlist.py

schem:
	gschem $(CELL).sch &

netlist:
	gnetlist -g spice-sdb -o $(CELL).sch.spi $(CELL).sch
	$(FIX_SPICE_NETLIST) $(CELL).sch.spi

sim_interactive:
	ngspice -a tb_$(CELL).spi

sim_batch:
	ngspice -a -b -r $(CELL).raw tb_$(CELL).spi

wave:
	bspwave $(CELL).raw &


