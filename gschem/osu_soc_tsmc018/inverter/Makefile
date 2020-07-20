# Makefile for osu_soc/inverter

CELL=invx1

schem:
	gschem $(CELL).sch &

netlist:
	gnetlist -g spice-sdb -o $(CELL).sch.spi $(CELL).sch
	
sim_interactive:
	ngspice -a tb_$(CELL).spi

sim_batch:
	ngspice -a -b -r $(CELL).raw tb_$(CELL).spi

wave:
	bspwave $(CELL).raw &


