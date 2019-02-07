#ifndef _CONSTANTS_H_
#define _CONSTANTS_H_

namespace constants {
  enum {relayCount=8};
  enum {digitalOutputCount=2};
  enum {digitalInputCount=1};

  // Communications parameters
  extern const int baudrate;

  // Device parameters
  extern const int modelNumber;
  extern const int serialNumberMin;
  extern const int serialNumberMax;
  extern const int firmwareNumber;

  // Pin assignment
  extern const int relayDriverCsPin;
  extern const int relayDriverInPin;
  extern const int digitalOutputPins[digitalOutputCount];
  extern const int digitalInputPins[digitalInputCount];

  // Scheduler parameters
  extern const int clockTicksPerSecond;

  // Blink parameters
  extern const int dutyCycleMin;
  extern const int dutyCycleMax;
}
#endif
