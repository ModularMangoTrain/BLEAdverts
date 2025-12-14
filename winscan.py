from bleak import BleakScanner
import asyncio
import csv
from datetime import datetime

f = open("data.csv", "w", newline="", encoding="utf-8")
writer = csv.writer(f)
writer.writerow(['Timestamp', 'MAC Address', 'RSSI', 'Name', 'Manufacturer Data'])

def callback(device, advertisement_data):
    writer.writerow([
        datetime.now().isoformat(),
        device.address,
        advertisement_data.rssi,
        advertisement_data.local_name or "Unknown",
        advertisement_data.manufacturer_data
    ])
    f.flush()

async def main():
    scanner = BleakScanner(detection_callback=callback, adapter="TP-Link Bluetooth 5.4 USB Adapter")
    await scanner.start()
    print("Scanning for BLE devices... Press Ctrl+C to stop")
    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping scan (Ctrl+C pressed)")
    finally:
        await scanner.stop()
        f.close()

if __name__ == "__main__":
    asyncio.run(main())
