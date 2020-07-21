v {xschem version=2.9.7 file_version=1.2}
G {}
V {}
S {}
E {}
N 50 -0 100 0 {lab=#net1}
N 210 -0 300 -0 {lab=#net2}
N 410 0 480 -0 {lab=#net3}
N -110 -0 -60 -0 {lab=#net3}
N -110 -80 -110 -0 {lab=#net3}
N -110 -80 460 -80 {lab=#net3}
N 460 -80 460 -0 {lab=#net3}
N -10 -120 -10 -40 {lab=vcc}
N -10 -120 530 -120 {lab=vcc}
N 530 -120 530 -40 {lab=vcc}
N 350 -120 350 -40 {lab=vcc}
N 150 -120 150 -40 {lab=vcc}
N -10 40 -10 100 {lab=gnd}
N -10 100 530 100 {lab=gnd}
N 530 40 530 100 {lab=gnd}
N 350 40 350 100 {lab=gnd}
N 150 40 150 100 {lab=gnd}
N 590 -0 690 0 {lab=o18oscout}
N 590 -0 700 -0 {lab=o18oscout}
N 700 -0 730 0 {lab=o18oscout}
N 10 160 150 160 {lab=gnd}
N 150 100 150 160 {lab=gnd}
N 10 -200 150 -200 {lab=vcc}
N 150 -200 150 -120 {lab=vcc}
C {opin.sym} 730 0 0 0 {name=p3 lab=o18oscout}
C {ipin.sym} 10 -200 0 0 {name=p1 lab=vcc}
C {ipin.sym} 10 160 0 0 {name=p2 lab=gnd}
C {../inverter/invx1.sym} 530 0 0 0 {name=x4}
C {../inverter/invx1.sym} 150 0 0 0 {name=x2}
C {../inverter/invx1.sym} 350 0 0 0 {name=x3}
C {../inverter/invx1.sym} -10 0 0 0 {name=x1}
