import asyncio
from bleak import BleakClient

address = "C1:FD:AA:08:58:48"
MODEL_NBR_UUID = "AM2V210"

async def main():
    print("Connecting to device...")
    async with BleakClient("C1:FD:AA:08:58:48") as client:
        print("Connected")
        # Read a characteristic, etc.
        ...

    # Device will disconnect when block exits.
    #async BleakClient.disconnect()
    #print("Disconnected")

# Using asyncio.run() is important to ensure that device disconnects on
# KeyboardInterrupt or other unhandled exception.
asyncio.run(main())