# Makefile for osu_soc/ringosc

CELL=ringosc

schem:
	xschem $(CELL).sch

netlist:
	xschem -o . -n -s -q --tcl 'set top_subckt 1' ./ringosc.sch

sim_interactive:
	ngspice -a tb_$(CELL).spi

sim_batch:
	ngspice -a -b -r $(CELL).raw tb_$(CELL).spi

wave:
	bspwave $(CELL).raw &


