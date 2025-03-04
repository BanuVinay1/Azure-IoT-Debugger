Azure IoT Debugger

Overview:
The **Azure IoT Debugger** is a Python-based tool designed to send test telemetry data (temperature, humidity) to an **Azure IoT Hub** device. It allows developers to validate their IoT Hub connectivity and simulate real-world IoT device behavior.

Features:
- Sends **random temperature and humidity values** as test telemetry.
- Uses **Azure IoT SDK** to send messages securely.
- Sends **10 test messages** with a **2-second delay** between each.
- Simple and lightweight for quick debugging.

Prerequisites:
1. **Python 3.8+** installed
2. **Azure IoT Hub** setup
3. **IoT Device registered in IoT Hub**
4. **Install dependencies**

pip install azure-iot-device

Configuration:
1. **Replace the connection string** in `IoT_Debugger.py` with your IoT Hub device connection string:

   CONNECTION_STRING = "Your IoT Hub Device Connection String"


Usage:
1. **Activate your virtual environment:
   iot_env\Scripts\activate

2. **Run the script**:
   python IoT_Debugger.py
  
3. **Expected Output**:
   Sending message: {"temperature": 31.6, "humidity": 62.04, "device_id": "iot-debugger-001"}
   Sending message: {"temperature": 26.57, "humidity": 43.61, "device_id": "iot-debugger-001"}
 
Verify in Azure IoT Hub
1. Go to **Azure Portal** → **IoT Hub**
2. Navigate to **Devices** → **Select your Device**
3. Check incoming telemetry in **Monitoring**

Cloud-to-Device Messaging (Command Execution)
az iot device c2d-message send --hub-name "<YOUR HUB>>" \
    --device-id "<YOUR DEVICE ID>>" \
    --data '{"command": "turn_on_fan"}'
The device will receive the command and execute it.
You will see the message on your terminal

Contributing
Pull requests and enhancements are welcome! Feel free to submit an issue or PR. 