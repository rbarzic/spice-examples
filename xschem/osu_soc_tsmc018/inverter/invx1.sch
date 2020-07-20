v {xschem version=2.9.7 file_version=1.1}
G {}
V {}
S {}
E {}
N 180 70 180 100 {lab=out}
N 80 130 140 130 {lab=in}
N 80 40 140 40 {lab=in}
N 80 40 80 130 {lab=in}
N 180 -50 180 10 {lab=vcc}
N 110 -50 180 -50 {lab=vcc}
N 180 40 230 40 {lab=vcc}
N 230 -50 230 40 {lab=vcc}
N 180 -50 230 -50 {lab=vcc}
N 180 160 180 200 {lab=gnd}
N 180 130 230 130 {lab=gnd}
N 230 130 230 200 {lab=gnd}
N 180 200 230 200 {lab=gnd}
N 180 80 280 80 {lab=out}
N 40 80 80 80 {lab=in}
N 130 200 180 200 {lab=gnd}
C {pmos4.sym} 160 40 0 0 {name=M1 model=pfet w=1u l=0.18u m=1}
C {nmos4.sym} 160 130 0 0 {name=M2 model=nfet w=1u l=0.18u m=1}
C {ipin.sym} 40 80 0 0 {name=p1 lab=in
}
C {opin.sym} 280 80 0 0 {name=p2 lab=out}
C {ipin.sym} 110 -50 0 0 {name=p3 lab=vcc}
C {ipin.sym} 130 200 0 0 {name=p4 lab=gnd
}
