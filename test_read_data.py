import asyncio
from bleak import BleakClient
address = "E4:E1:12:53:E7:93"
CHARACTERISTIC_UUID = "f0001111-4202-cd8d-eb11-3386a69ec3e6"

async def start_read():
    async with BleakClient(address) as client:
        print(client.is_connected)
        while (True):
            value = bytes(await client.read_gatt_char(CHARACTERISTIC_UUID))
            print(value)

        ...

    # Device will disconnect when block exits.
    ...

# Using asyncio.run() is important to ensure that device disconnects on
# KeyboardInterrupt or other unhandled exception.
asyncio.run(start_read())