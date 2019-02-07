#!python
from __future__ import print_function
import os
import sys
import flask
import flask_sijax
import argparse
from arduino_olfactometer import ArduinoOlfactometer

network_port = 5000

# Setup application w/ sijax
path = os.path.join('.', os.path.dirname(__file__), 'static/js/sijax/')
app = flask.Flask(__name__)
app.config["SIJAX_STATIC_PATH"] = path
app.config["SIJAX_JSON_URI"] = '/static/js/sijax/json2.js'
flask_sijax.Sijax(app)

class SijaxHandler(object):
    """A container class for all Sijax handlers.

    Grouping all Sijax handler functions in a class
    (or a Python module) allows them all to be registered with
    a single line of code.
    """

    @staticmethod
    def setOdorValveOn(obj_response):
        valve = 2
        olfactometer.setOdorValveOn(valve)

    @staticmethod
    def setOdorValvesOff(obj_response):
        olfactometer.setOdorValvesOff()

@flask_sijax.route(app, "/")
def index():
    if flask.g.sijax.is_sijax_request:
        # The request looks like a valid Sijax request
        # Let's register the handlers and tell Sijax to process it
        flask.g.sijax.register_object(SijaxHandler)
        return flask.g.sijax.process_request()

    return flask.render_template('olfactometer.html')

@app.route('/kill')
def abort():
    actuation.controller.close()
    pid = os.getpid()
    os.kill(pid,signal.SIGTERM)

@app.route('/olfactometer/setOdorValveOn')
def setOdorValveOn():
    try:
        device = int(flask.request.args['device'])
    except KeyError:
        device = 0
    try:
        valve = int(flask.request.args['valve'])
        olfactometer.setOdorValveOn(device,valve)
        return 'device: {device} valve: {valve}, set: on'.format(device=device,
                                                                 valve=valve)
    except KeyError:
        pass

@app.route('/olfactometer/setOdorValvesOff')
def setOdorValveOff():
    try:
        device = int(flask.request.args['device'])
    except KeyError:
        device = 0
    try:
        olfactometer.setOdorValvesOff(device)
        return 'device: {device} valves, set: off'.format(device=device)
    except KeyError:
        pass

@app.route('/olfactometer/setMfcFlowRate')
def setMfcFlowRate():
    try:
        device = int(flask.request.args['device'])
    except KeyError:
        device = 0
    try:
        mfc = int(flask.request.args['mfc'])
        percent_capacity = int(flask.request.args['percent_capacity'])
        olfactometer.setMfcFlowRate(device,mfc,percent_capacity)
        return 'device: {device}, mfc: {mfc}, percent_capacity: {percent_capacity}'.format(device=device,
                                                                                           mfc=mfc,
                                                                                           percent_capacity=percent_capacity)
    except KeyError:
        pass

@app.route('/olfactometer/getMfcFlowRateSetting')
def getMfcFlowRateSetting():
    try:
        device = int(flask.request.args['device'])
    except KeyError:
        device = 0
    try:
        mfc = int(flask.request.args['mfc'])
        percent_capacity = olfactometer.getMfcFlowRateSetting(device,mfc)
        return 'device: {device}, mfc: {mfc}, percent_capacity: {percent_capacity}'.format(device=device,
                                                                                           mfc=mfc,
                                                                                           percent_capacity=percent_capacity)
    except KeyError:
        pass

@app.route('/olfactometer/getMfcFlowRateMeasure')
def getMfcFlowRateMeasure():
    try:
        device = int(flask.request.args['device'])
    except KeyError:
        device = 0
    try:
        mfc = int(flask.request.args['mfc'])
        percent_capacity = olfactometer.getMfcFlowRateMeasure(device,mfc)
        return 'device: {device}, mfc: {mfc}, percent_capacity: {percent_capacity}'.format(device=device,
                                                                                           mfc=mfc,
                                                                                           percent_capacity=percent_capacity)
    except KeyError:
        pass

def arduinoOlfactometerWebserver():
    global olfactometer
    olfactometer = None

    parser = argparse.ArgumentParser(description='Arduino Olfactometer Webserver')
    parser.add_argument('-d', '--debug',
                        help='start the server in local-only debug mode',
                        action='store_true')
    args = parser.parse_args()

    server = 'remote'
    debug = False
    if args.debug:
        server = 'local'
        debug = True

    # Open connection to olfactometer
    olfactometer = ArduinoOlfactometer()

    if server == 'local':
        print(' * using debug server - localhost only')
        app.run(port=network_port,debug=debug)
    else:
        print(' * using builtin server - remote access possible')
        app.run(host='0.0.0.0',port=network_port)


# -----------------------------------------------------------------------------
if __name__ == '__main__':
    arduinoOlfactometerWebserver()
