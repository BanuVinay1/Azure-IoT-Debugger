import asyncio
import random
import json
from azure.iot.device.aio import IoTHubDeviceClient

# Azure IoT Hub connection string (replace with your actual connection string)
CONNECTION_STRING = "<YOUR CONNECTION STRING>"

# Sample telemetry data function
def generate_telemetry():
    return {
        "temperature": round(random.uniform(20.0, 35.0), 2),
        "humidity": round(random.uniform(30.0, 80.0), 2),
        "device_id": "iot-debugger-001"
    }

# Function to send test messages to IoT Hub
async def send_test_messages():
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    await client.connect()
    
    try:
        for _ in range(10):  # Send 10 test messages
            telemetry_data = generate_telemetry()
            message = json.dumps(telemetry_data)
            print(f"Sending message: {message}")
            await client.send_message(message)
            await asyncio.sleep(2)  # Delay between messages
    finally:
        await client.shutdown()

if __name__ == "__main__":
    asyncio.run(send_test_messages())
