# Makefile for inv_spice 

inv_netlist:
	gnetlist -g spice-sdb -o inv_spice.spi inv_spice.sch

interactive:
	ngspice -a tb_inv_spice.spi

batch:
	ngspice -a -b -r inv_spice.raw tb_inv_spice.spi

get_spice_lib:
	wget ecee.colorado.edu/~ecen4827/spice/ltspice/5827_035.lib


