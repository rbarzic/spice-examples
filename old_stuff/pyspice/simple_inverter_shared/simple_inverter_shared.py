#!/usr/bin/env python3
import matplotlib.pyplot as plt
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

# logger = Logging.setup_logging(logging_level=lg.DEBUG)
logger = Logging.setup_logging()



libnspice_path = os.environ.get('LIBNGSPICE_SO')
if libnspice_path:
    NgSpiceShared.LIBRARY_PATH = libnspice_path

ngspice_shared = NgSpiceShared.new_instance()


spice_library = SpiceLibrary('.')

parser = SpiceParser(path="./inv_spice.spi")
circuit = parser.build_circuit()

circuit.include(spice_library['NM'])
circuit.PulseVoltageSource('input', # Name
                           'vin', circuit.gnd, # Connection
                           initial_value = 0,
                           pulsed_value = 5,
                           pulse_width = 100*ns,
                           period = 200*ns,
                           delay_time=20*ns,
                           rise_time=10*ns,
                           fall_time=10*ns)

circuit.V('xx',
          'VCC', circuit.gnd,
          5
          )

print(circuit)


simulator = circuit.simulator(temperature=25,
                              nominal_temperature=25,
                              simulator='ngspice-shared',
                              ngspice_shared=ngspice_shared)
analysis = simulator.transient(step_time= 10*ps, end_time=1*µs)

axe = plt.subplot(111)
axe.set_title('Simple Inverter')
axe.set_xlabel('Time [s]')
axe.set_ylabel('Voltage [V]')
axe.grid()
# Fixme: axis vs axe ...
plot(analysis['vin'], axis=axe)
plot(analysis['vout'], axis=axe)
plt.tight_layout()
plt.show()



# Local Variables:
# eval: (blacken-mode)
# End:
