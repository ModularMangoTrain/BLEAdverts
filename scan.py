import asyncio
from bleak import BleakScanner
import csv

f = open("data.csv", "w", newline = "", encoding = "utf-8") #opens/creates csv file in write mode
writer = csv.writer(f)
writer.writerow(['RSSI', 'Name', 'Manufacturer Data'])

def callback(device, advertisement_data):
    writer.writerow([
        getattr(advertisement_data, "rssi", None),
        getattr(advertisement_data, "local_name", "Unknown"),
        getattr(advertisement_data, "manufacturer_data", {})
    ])
    f.flush()

async def main():
    adapter = "hci0"  # your USB BLE dongle
    scanner = BleakScanner(detection_callback=callback, adapter=adapter)
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
