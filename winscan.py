from bleak import BleakScanner
import asyncio

def callback(device, advertisement_data):
    rssi = getattr(advertisement_data, "rssi", None)
    name = getattr(advertisement_data, "local_name", "Unknown")
    mfg = getattr(advertisement_data, "manufacturer_data", {})
    print(f"{device.address} RSSI:{rssi} Name:{name} MFG:{mfg}")

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

if __name__ == "__main__":
    asyncio.run(main())
