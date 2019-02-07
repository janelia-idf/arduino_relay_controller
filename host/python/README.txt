========================
arduino_relay_controller
========================

arduino_relay_controller is a python package to control the Arduino
relay controller over USB, using the python module, the command line, a
GUI, or a webpage using a webserver.


Install
-------

See INSTALL.txt

Python Module
-------------

Typical usage often looks like this::

    from arduino_relay_controller import ArduinoRelayController, ArduinoRelayControllers

    relay_controllers = ArduinoRelayControllers()
    device_count = len(relay_controllers)
    if device_count == 0:
        raise RuntimeError('No Arduino relay controllers detected, check connections.')
    valve_count = relay_controllers[0].valve_count
    mfc_count = relay_controllers[0].mfc_count

    o = ArduinoRelay_Controllers[0]
    o.setMfcFlowRate(mfc=1,percent_capacity=75)
    print o.getMfcFlowRateSetting(mfc=1)
    print o.getMfcFlowRateMeasure(mfc=0)
    o.setOdorValveOn(valve=4)
    o.setOdorValvesOff()

Author: Peter Polidoro

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
