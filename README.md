# EnviroCheck
## App for Measuring Air Temperature and Humidity
---
The EnviroCheck app runs on a Raspberry Pi RP2040 microcontroller and measures air temperature and humidity using an external DHT22 sensor. The app uses asynchronous POST requests to send the measured values to a web API (written in .NET Core), which then stores the data in a local database. If no external DHT22 sensor is connected, the app uses the embedded temperature sensor of the RP2040.
---
Note: This app has been tested on a Raspberry Pi RP2040 microcontroller. Its compatibility with other microcontrollers using the same chip is not confirmed.
