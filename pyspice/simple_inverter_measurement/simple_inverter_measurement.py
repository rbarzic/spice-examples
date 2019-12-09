#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import PySpice
import PySpice.Logging.Logging as Logging
import logging as lg

from PySpice.Doc.ExampleTools import find_libraries
from PySpice.Spice.Library import SpiceLibrary
from PySpice.Spice.Netlist import Circuit
from PySpice.Spice.Parser import SpiceParser
from PySpice.Unit import *

from PySpice.Spice.NgSpice.Shared import NgSpiceShared

from PySpice.Probe.Plot import plot
import os

ps = 1e-12
ns = 1e-9
µs = 1e-6
ms = 1e-3

VDD = 1.8

# logger = Logging.setup_logging(logging_level=lg.DEBUG)
logger = Logging.setup_logging()


libnspice_path = os.environ.get("LIBNGSPICE_SO")
if libnspice_path:
    NgSpiceShared.LIBRARY_PATH = libnspice_path

ngspice_shared = NgSpiceShared.new_instance()


spice_library = SpiceLibrary(".")

parser = SpiceParser(path="./INVX1.spi")
circuit = parser.build_circuit()

# circuit.include(spice_library["NM"])
circuit.include("../../imported/osu_soc/cadence/lib/tsmc018/lib/tsmc018.m")
circuit.include(
    "../../imported/osu_soc/cadence/lib/tsmc018/signalstorm/osu018_stdcells.sp"
)
circuit.PulseVoltageSource(
    "input",  # Name
    "vin",
    circuit.gnd,  # Connection
    initial_value=0,
    pulsed_value=VDD,
    pulse_width=100 * ns,
    period=200 * ns,
    delay_time=20 * ns,
    rise_time=10 * ns,
    fall_time=10 * ns,
)

circuit.V("xx", "VCC", circuit.gnd, VDD)
circuit.X("1", "INVX1", "vin", "vout", "vcc", circuit.gnd)

print(circuit)


simulator = circuit.simulator(
    temperature=25,
    nominal_temperature=25,
    simulator="ngspice-shared",
    ngspice_shared=ngspice_shared,
)
analysis = simulator.transient(step_time=10 * ps, end_time=500 * ns)


def find_rising_edge(data, threshold):
    return np.flatnonzero((data[:-1] < threshold) & (data[1:] > threshold)) + 1


def find_falling_edge(data, threshold):
    return np.flatnonzero((data[:-1] > threshold) & (data[1:] < threshold)) + 1


axe = plt.subplot(111)
axe.set_title("Simple Inverter")
axe.set_xlabel("Time [s]")
axe.set_ylabel("Voltage [V]")
axe.grid()
# Fixme: axis vs axe ...

plot(analysis["vin"], axis=axe)
plot(analysis["vout"], axis=axe)
print(f"-D- type of analysis['vin'] : {type(analysis['vin'])}")
print(f"-D- analysis['vin'].abscissa = {type(analysis['vin'].abscissa)}")
print(
    f"-D- analysis['vin'].abscissa[-1] = {type(analysis['vin'].abscissa[-1])}"
)
print(f"-D- analysis['vin'].abscissa[-1] = {(analysis['vin'].abscissa[-1])}")


vin_rising_edges = find_rising_edge(analysis["vin"].as_ndarray(), VDD / 2.0)
print(f"-D- Rising edges : {vin_rising_edges}")

vin_falling_edges = find_falling_edge(analysis["vin"].as_ndarray(), VDD / 2.0)
print(f"-D- falling edges : {vin_falling_edges}")


vout_rising_edges = find_rising_edge(analysis["vout"].as_ndarray(), VDD / 2.0)
print(f"-D- Rising edges : {vout_rising_edges}")

vout_falling_edges = find_falling_edge(analysis["vout"].as_ndarray(), VDD / 2.0)
print(f"-D- falling edges : {vout_falling_edges}")

# We have an inverter !
rising_delays = vout_rising_edges - vin_falling_edges
falling_delays = vout_falling_edges - vin_rising_edges

print(f"-D- Rising delays : {rising_delays}")

# plot([x1, x2], [y1, y2], color='k', linestyle='-', linewidth=2)
plt.plot([0, 500 * ns], [VDD / 2.0, VDD / 2.0], "k-", lw=1, dashes=[2, 2])
plt.tight_layout()
plt.show()


# Local Variables:
# eval: (blacken-mode)
# End:
