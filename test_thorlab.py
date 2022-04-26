import pymeasure
from pymeasure.instruments.thorlabs import ThorlabsPM100USB
import pyvisa as visa

# remember to install ni-visa 
# (read more from pyvisa doc)
rm = visa.ResourceManager()
print(rm.list_resources())
#lst = rm.list_resources('?*')

inst = rm.open_resource('USB0::0x1313::0x8072::1914794::INSTR', timeout=1)
#print(rm)


powermeter = ThorlabsPM100USB('USB0::0x1313::0x8072::1914794::INSTR')
print(powermeter.id)
powermeter.wavelength = 520
print(powermeter.wavelength)
print(powermeter.power)

#print(pymeasure.__version__)