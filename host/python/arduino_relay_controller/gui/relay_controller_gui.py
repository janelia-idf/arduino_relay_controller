import sys, platform, serial, time, math, functools
from PyQt4 import QtCore
from PyQt4 import QtGui
from olfactometer_ui import Ui_MainWindow
import json
from arduino_olfactometer import ArduinoOlfactometers

DEBUG = False

class OlfactometerMainWindow(QtGui.QMainWindow,Ui_MainWindow):

    def __init__(self,parent=None):
        super(OlfactometerMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.initialize()
        self.connectActions()

    def initialize(self):
        self.olfactometers = ArduinoOlfactometers()
        self.device_count = len(self.olfactometers)
        if self.device_count == 0:
            raise RuntimeError('No Arduino olfactometers detected, check connections.')
        self.valve_count = self.olfactometers[0].valve_count
        self.mfc_count = self.olfactometers[0].mfc_count
        self.valveComboBox.insertItems(1,[str(d) for d in range(self.valve_count)])
        self.valveComboBox.setCurrentIndex(0)
        self.mfcComboBox.insertItems(1,[str(m) for m in range(self.mfc_count)])
        self.mfcComboBox.setCurrentIndex(0)
        self.updateDeviceComboBoxes()
        self.infoLabels = [self.infoLabel_0,self.infoLabel_1,self.infoLabel_2,self.infoLabel_3]

    def updateDeviceComboBoxes(self):
        device_labels = []
        for device_index in range(self.device_count):
            o = self.olfactometers[device_index]
            device_name = o.getDeviceName()
            serial_number = o.getArduinoSerialNumber()
            if o.device_name == '':
                device_label = 'index: {index}, serial_number: {serial_number}, port: {port}'.format(index=device_index,
                                                                                                     serial_number=serial_number,
                                                                                                     port=o.port)
            else:
                device_label = 'index: {index}, serial_number: {serial_number}, name: {name}'.format(index=device_index,
                                                                                                     serial_number=serial_number,
                                                                                                     name=device_name)
            device_labels.append(device_label)

        self.infoDeviceComboBox.clear()
        self.infoDeviceComboBox.insertItems(1,device_labels)

        self.valveDeviceComboBox.clear()
        self.valveDeviceComboBox.insertItems(1,device_labels)

        self.mfcDeviceComboBox.clear()
        self.mfcDeviceComboBox.insertItems(1,device_labels)

    def connectActions(self):
        self.getInfoPushButton.clicked.connect(self.infoClicked_Callback)
        self.setSerialNumberPushButton.clicked.connect(self.setSerialNumberClicked_Callback)
        self.getSerialNumberPushButton.clicked.connect(self.getSerialNumberClicked_Callback)
        self.setNamePushButton.clicked.connect(self.setNameClicked_Callback)
        self.getNamePushButton.clicked.connect(self.getNameClicked_Callback)
        self.setValveOnPushButton.clicked.connect(self.setValveOnClicked_Callback)
        self.setValvesOffPushButton.clicked.connect(self.setValvesOffClicked_Callback)
        self.getValveOnPushButton.clicked.connect(self.getValveOnClicked_Callback)
        self.setMfcPushButton.clicked.connect(self.setMfcClicked_Callback)
        self.getMfcSettingPushButton.clicked.connect(self.getMfcSettingClicked_Callback)
        self.getMfcMeasurePushButton.clicked.connect(self.getMfcMeasureClicked_Callback)

    def infoClicked_Callback(self):
        if self.device_count < len(self.infoLabels):
            info_count = self.device_count
        else:
            info_count = len(self.infoLabels)
        self.deviceCountLabel.setText("Olfactometer Count: {count}".format(count=info_count))
        for info_index in range(info_count):
            info_dict = self.olfactometers[info_index].getArduinoOlfactometerInfo()
            info_str = json.dumps(info_dict,sort_keys=True,indent=2,separators=(',', ': '))
            self.infoLabels[info_index].setText(info_str)

    def setSerialNumberClicked_Callback(self):
        device_index = int(self.infoDeviceComboBox.currentIndex())
        serial_number = int(self.serialNumberSpinBox.value())
        self.olfactometers[device_index].setArduinoSerialNumber(serial_number)
        self.serialNumberLabel.setText(str(serial_number))
        index = self.infoDeviceComboBox.currentIndex()
        self.updateDeviceComboBoxes()
        self.infoDeviceComboBox.setCurrentIndex(index)

    def getSerialNumberClicked_Callback(self):
        device_index = int(self.infoDeviceComboBox.currentIndex())
        serial_number = self.olfactometers[device_index].getArduinoSerialNumber()
        self.serialNumberLabel.setText(str(serial_number))

    def setNameClicked_Callback(self):
        device_index = int(self.infoDeviceComboBox.currentIndex())
        name = str(self.nameLineEdit.text())
        self.olfactometers[device_index].device_name = name
        self.nameLabel.setText(str(name))
        index = self.infoDeviceComboBox.currentIndex()
        self.updateDeviceComboBoxes()
        self.infoDeviceComboBox.setCurrentIndex(index)

    def getNameClicked_Callback(self):
        device_index = int(self.infoDeviceComboBox.currentIndex())
        name = self.olfactometers[device_index].device_name
        self.nameLabel.setText(str(name))

    def setValveOnClicked_Callback(self):
        device_index = int(self.valveDeviceComboBox.currentIndex())
        valve = int(self.valveComboBox.currentText())
        self.olfactometers[device_index].setOdorValveOn(valve)
        self.valveOnLabel.setText(str(valve))

    def setValvesOffClicked_Callback(self):
        device_index = int(self.valveDeviceComboBox.currentIndex())
        self.olfactometers[device_index].setOdorValvesOff()
        self.valveOnLabel.setText(str(-1))

    def getValveOnClicked_Callback(self):
        device_index = int(self.valveDeviceComboBox.currentIndex())
        valve_on = self.olfactometers[device_index].getOdorValveOn()
        self.valveOnLabel.setText(str(valve_on))

    def setMfcClicked_Callback(self):
        device_index = int(self.mfcDeviceComboBox.currentIndex())
        mfc = int(self.mfcComboBox.currentText())
        percent_capacity = self.mfcSettingSpinBox.value()
        try:
            self.olfactometers[device_index].setMfcFlowRate(mfc,percent_capacity)
            self.mfcSettingLabel.setText(str(percent_capacity))
            self.mfcErrorLabel.clear()
        except IOError:
            self.mfcErrorLabel.setText("No MFC Detected!")

    def getMfcSettingClicked_Callback(self):
        device_index = int(self.mfcDeviceComboBox.currentIndex())
        mfc = int(self.mfcComboBox.currentText())
        try:
            percent_capacity = self.olfactometers[device_index].getMfcFlowRateSetting(mfc)
            self.mfcSettingLabel.setText(str(percent_capacity))
            self.mfcErrorLabel.clear()
        except IOError:
            self.mfcErrorLabel.setText("No MFC Detected!")

    def getMfcMeasureClicked_Callback(self):
        device_index = int(self.mfcDeviceComboBox.currentIndex())
        mfc = int(self.mfcComboBox.currentText())
        try:
            percent_capacity = self.olfactometers[device_index].getMfcFlowRateMeasure(mfc)
            self.mfcMeasureLabel.setText(str(percent_capacity))
            self.mfcErrorLabel.clear()
        except IOError:
            self.mfcErrorLabel.setText("No MFC Detected!")

    def main(self):
        self.show()

def arduinoOlfactometerGui():
    app = QtGui.QApplication(sys.argv)
    mainWindow = OlfactometerMainWindow()
    mainWindow.main()
    app.exec_()

# -----------------------------------------------------------------------------
if __name__ == '__main__':
    arduinoOlfactometerGui()
