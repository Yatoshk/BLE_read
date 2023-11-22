import asyncio
from bleak import BleakClient

address = "E4:E1:12:53:DA:81"
MODEL_NBR_UUID = "None"

async def main():
    print("Connecting to device...")
    async with BleakClient(address) as client:
        print("Connecting to device...")
        print("Connected") if (client.is_connected) else print("No connection")
        # Read a characteristic, etc.
        print(client.services)
        

    # Device will disconnect when block exits.
    #async BleakClient.disconnect()
    #print("Disconnected")

# Using asyncio.run() is important to ensure that device disconnects on
# KeyboardInterrupt or other unhandled exception.
asyncio.run(main())