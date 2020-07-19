v 20130925 2
C 40000 40000 0 0 0 title-B.sym
C 46600 46500 1 0 0 asic-nmos-1.sym
{
T 48000 47300 5 8 0 0 0 0 1
device=NMOS_TRANSISTOR
T 47400 47300 5 10 1 1 0 0 1
refdes=M1
T 47400 47100 5 8 1 1 0 0 1
model-name=pch
T 47400 46800 5 8 1 0 0 0 1
w=1u
T 47400 46600 5 8 1 0 0 0 1
l=0.18u
}
C 46600 44700 1 0 0 asic-nmos-1.sym
{
T 48000 45500 5 8 0 0 0 0 1
device=NMOS_TRANSISTOR
T 47400 45500 5 10 1 1 0 0 1
refdes=M2
T 47400 45300 5 8 1 1 0 0 1
model-name=nch
T 47400 45000 5 8 1 0 0 0 1
w=1u
T 47400 44800 5 8 1 0 0 0 1
l=0.18u
}
N 47200 44000 47200 44700 4
N 47200 45700 47200 46500 4
N 46600 47000 46100 47000 4
N 46100 47000 46100 45200 4
N 46100 45200 46600 45200 4
N 45700 47500 47900 47500 4
{
T 46500 47500 5 10 1 1 0 0 1
netname=vcc
}
N 45300 46100 46100 46100 4
{
T 45700 46100 5 10 1 1 0 0 1
netname=A
}
N 47200 46100 48500 46100 4
{
T 47200 46100 5 10 1 1 0 0 1
netname=Y
}
N 47300 47000 47900 47000 4
N 47900 47000 47900 47500 4
N 47300 45200 47600 45200 4
N 47600 45200 47600 44000 4
N 46000 44000 47600 44000 4
{
T 46500 44000 5 10 1 1 0 0 1
netname=gnd
}
C 45500 46400 1 180 0 spice-subcircuit-IO-1.sym
{
T 44600 46000 5 10 0 1 180 0 1
device=spice-IO
T 44650 46150 5 10 1 1 180 0 1
refdes=P0
}
C 48300 45800 1 0 0 spice-subcircuit-IO-1.sym
{
T 49200 46200 5 10 0 1 0 0 1
device=spice-IO
T 49150 46050 5 10 1 1 0 0 1
refdes=P1
}
C 45900 47800 1 180 0 spice-subcircuit-IO-1.sym
{
T 45000 47400 5 10 0 1 180 0 1
device=spice-IO
T 45050 47550 5 10 1 1 180 0 1
refdes=P2
}
C 46200 44300 1 180 0 spice-subcircuit-IO-1.sym
{
T 45300 43900 5 10 0 1 180 0 1
device=spice-IO
T 45350 44050 5 10 1 1 180 0 1
refdes=P3
}
C 43000 43000 1 0 0 spice-subcircuit-LL-1.sym
{
T 43100 43300 5 10 0 1 0 0 1
device=spice-subcircuit-LL
T 43100 43400 5 10 1 1 0 0 1
refdes=A0
T 43000 43100 5 10 1 1 0 0 1
model-name=invx1
}
