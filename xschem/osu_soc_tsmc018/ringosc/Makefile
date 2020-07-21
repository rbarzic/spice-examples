# Makefile for osu_soc/ringosc

CELL=ringosc
FIX_SPICE_NETLIST?=../../scripts/fix_spice_netlist.py

schem:
	xschem $(CELL).sch

netlist1:
	xschem -o . -n -s -q --script  ./set_top_subckt.tcl   ./ringosc.sch

netlist2:
	xschem -o . -n -s -q --tcl  ./set_top_subckt.tcl  ./ringosc.sch

netlist3:
	xschem -o . -n -s -q    ./ringosc.sch

sim_interactive:
	ngspice -a tb_$(CELL).spi

sim_batch:
	ngspice -a -b -r $(CELL).raw tb_$(CELL).spi

wave:
	bspwave $(CELL).raw &


