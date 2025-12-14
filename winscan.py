from bleak import BleakScanner
import asyncio
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
    f.flush() #makes python write any buffered data to disk, avoiding any incidents of missing data

async def main():
    # Pass callback to the constructor
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
