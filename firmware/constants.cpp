#include "constants.h"
namespace constants {
  // Communications parameters
  const int baudrate = 9600;

  // Device parameters
  const int modelNumber = 1761;
  const int serialNumberMin = 0;
  const int serialNumberMax = 255;
  const int firmwareNumber = 2;

  // Pin assignment
  const int relayDriverCsPin = 49;
  const int relayDriverInPin = 48;
  const int digitalOutputPins[digitalOutputCount] = {22,23};
  const int digitalInputPins[digitalInputCount] = {24};

  // Timestamp parameters
  const int clockTicksPerSecond = 1000;

  // Blink parameters
  const int dutyCycleMin = 0;
  const int dutyCycleMax = 100;
}
