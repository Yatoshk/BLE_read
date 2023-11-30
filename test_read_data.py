import asyncio
from bleak import BleakClient
import time
address = "E4:E1:12:53:E7:93"
CHARACTERISTIC_UUID = "f0001111-4202-cd8d-eb11-3386a69ec3e6"
def callback(sender, data):
    temp = []
    for i in range(20,56,2):
        #print(int.from_bytes(data[i:i+2], byteorder='big'))
        temp.append(int.from_bytes(data[i:i+2], byteorder='big'))
    with open(r'data.txt', 'w') as fp:
        fp.truncate()
    with open(r'data.txt', 'w') as fp:
        for i in temp:
            fp.write("%s " % i)
    print(f"{len(list(data))}")
    time.sleep(0.3)

async def start_read():
    async with BleakClient(address)as client:
        print(client.is_connected)
        #while (True):
        #value = list(bytes(await client.read_gatt_char(CHARACTERISTIC_UUID, use_cached = False)))

        await client.start_notify(CHARACTERISTIC_UUID, callback)

        ...

    # Device will disconnect when block exits.
    ...

# Using asyncio.run() is important to ensure that device disconnects on
# KeyboardInterrupt or other unhandled exception.
asyncio.run(start_read())
