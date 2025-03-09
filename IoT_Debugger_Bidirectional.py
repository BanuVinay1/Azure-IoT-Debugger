import asyncio
import random
import json
import os
from azure.iot.device.aio import IoTHubDeviceClient
from azure.iot.device import exceptions

# Azure IoT Hub connection string (replace with your actual connection string)
CONNECTION_STRING = "<Your Connection String>"


if not CONNECTION_STRING:
    raise ValueError("ERROR: IOT_HUB_CONNECTION_STRING environment variable is not set!")

# Function to generate telemetry data
def generate_telemetry():
    return {
        "temperature": round(random.uniform(20.0, 35.0), 2),
        "humidity": round(random.uniform(30.0, 80.0), 2),
        "device_id": "iot-debugger-001"
    }

# Function to send telemetry messages to IoT Hub
async def send_test_messages(client):
    try:
        for _ in range(10):  # Send 10 test messages
            telemetry_data = generate_telemetry()
            message = json.dumps(telemetry_data)
            print(f"Sending message: {message}")
            await client.send_message(message)
            await asyncio.sleep(2)  # Delay between messages
    except Exception as e:
        print(f"Error sending message: {e}")

# Function to receive messages from IoT Hub with a timeout
async def receive_c2d_messages(client, timeout=5):
    while True:
        try:
            message = await asyncio.wait_for(client.receive_message(), timeout=timeout)
            command = message.data.decode()
            print(f"Received command from cloud: {command}")

            # Process the command
            command_data = json.loads(command)
            if "command" in command_data:
                execute_command(command_data["command"])
            else:
                print("Received unknown command format.")

        except asyncio.TimeoutError:
            print("No Cloud-to-Device messages received, checking again...")
        except exceptions.ClientError as e:
            print(f"IoT Hub connection error: {e}")
            await client.connect()  # Reconnect if needed
        except Exception as e:
            print(f"Error receiving message: {e}")

# Function to execute received commands
def execute_command(command):
    print(f"Executing command: {command}")
    if command == "turn_on_fan":
        print("Fan is now ON!")
    elif command == "turn_off_fan":
        print("Fan is now OFF!")
    else:
        print(f"Unknown command: {command}")

# Main function to handle both sending and receiving messages
async def main():
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    await client.connect()

    print("Connected to IoT Hub. Listening for commands...")

    try:
        await asyncio.gather(
            send_test_messages(client),
            receive_c2d_messages(client)
        )
    except Exception as e:
        print(f"Connection lost. Restarting... {e}")
        await client.shutdown()
        await main()  # Restart the loop

if __name__ == "__main__":
    asyncio.run(main())
