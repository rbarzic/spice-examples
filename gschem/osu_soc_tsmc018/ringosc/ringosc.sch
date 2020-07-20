v 20191008 2
C 40000 40000 0 0 0 title-B.sym
N 45700 47500 47900 47500 4
{
T 46500 47500 5 10 1 1 0 0 1
netname=vcc
}
N 47900 47000 47900 47500 4
N 47600 45200 47600 44000 4
N 46000 44000 47600 44000 4
{
T 46500 44000 5 10 1 1 0 0 1
netname=gnd
}
C 54700 45800 1 0 0 spice-subcircuit-IO-1.sym
{
T 55600 46200 5 10 0 1 0 0 1
device=spice-IO
T 55550 46050 5 10 1 1 0 0 1
refdes=P0
}
C 45900 47800 1 180 0 spice-subcircuit-IO-1.sym
{
T 45000 47400 5 10 0 1 180 0 1
device=spice-IO
T 45050 47550 5 10 1 1 180 0 1
refdes=P1
}
C 46200 44300 1 180 0 spice-subcircuit-IO-1.sym
{
T 45300 43900 5 10 0 1 180 0 1
device=spice-IO
T 45350 44050 5 10 1 1 180 0 1
refdes=P2
}
C 43000 43000 1 0 0 spice-subcircuit-LL-1.sym
{
T 43100 43300 5 10 0 1 0 0 1
device=spice-subcircuit-LL
T 43100 43400 5 10 1 1 0 0 1
refdes=A1
T 43000 43100 5 10 1 1 0 0 1
model-name=ringosc
}
C 46100 45500 1 0 0 invx1.sym
{
T 46200 46400 5 10 1 1 0 0 1
refdes=X1
T 46900 46200 5 10 0 0 0 0 1
symversion=1.0
T 46900 45500 5 10 0 0 0 0 1
footprint=none
T 46900 46400 5 10 1 1 0 0 1
model-name=invx1
T 46900 45800 5 10 1 1 0 0 1
file=invx1.sch.spi
T 46900 45600 5 10 1 1 0 0 1
device=invx1
}
C 48100 45500 1 0 0 invx1.sym
{
T 48200 46400 5 10 1 1 0 0 1
refdes=X2
T 48900 46200 5 10 0 0 0 0 1
symversion=1.0
T 48900 45500 5 10 0 0 0 0 1
footprint=none
T 48900 46400 5 10 1 1 0 0 1
model-name=invx1
T 48900 45800 5 10 1 1 0 0 1
file=invx1.sch.spi
T 48900 45600 5 10 1 1 0 0 1
device=invx1
}
C 50000 45500 1 0 0 invx1.sym
{
T 50100 46400 5 10 1 1 0 0 1
refdes=X3
T 50800 46200 5 10 0 0 0 0 1
symversion=1.0
T 50800 45500 5 10 0 0 0 0 1
footprint=none
T 50800 46400 5 10 1 1 0 0 1
model-name=invx1
T 50800 45800 5 10 1 1 0 0 1
file=invx1.sch.spi
T 50800 45600 5 10 1 1 0 0 1
device=invx1
}
N 46100 46100 46100 47100 4
N 46100 47100 51600 47100 4
N 51600 47100 51600 46100 4
N 51100 46100 52400 46100 4
C 52400 45500 1 0 0 invx1.sym
{
T 52500 46400 5 10 1 1 0 0 1
refdes=X4
T 53200 46200 5 10 0 0 0 0 1
symversion=1.0
T 53200 45500 5 10 0 0 0 0 1
footprint=none
T 53200 46400 5 10 1 1 0 0 1
model-name=invx1
T 53200 45800 5 10 1 1 0 0 1
file=invx1.sch.spi
T 53200 45600 5 10 1 1 0 0 1
device=invx1
}
N 47200 46100 48100 46100 4
N 49200 46100 50000 46100 4
N 53500 46100 54900 46100 4
{
T 53900 46100 5 10 1 1 0 0 1
netname=o18oscout
}
N 46600 46600 46600 47000 4
N 46600 47000 52900 47000 4
N 52900 47000 52900 46600 4
N 50500 46600 50500 47000 4
N 48600 46600 48600 47000 4
N 46600 45600 46600 45200 4
N 46600 45200 52900 45200 4
N 52900 45200 52900 45600 4
N 50500 45600 50500 45200 4
N 48600 45600 48600 45200 4
