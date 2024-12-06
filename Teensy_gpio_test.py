'''
Description: Tests GPIO pins by setting their outputs
and reading their inputs using direct memory-mapped I/O.
Author: [MicroControleurMonde]
Date: 06.12.2024
File: Teensy_gpio_test.py
'''
import machine
import time

# Dictionary of GPIOs with their corresponding memory addresses
GPIO_ADDRESSES = {
    5: 0x400C0000,  # GPIO5
    4: 0x401C4000,  # GPIO4
    3: 0x401C0000,  # GPIO3
    2: 0x401BC000,  # GPIO2
    1: 0x401B8000,  # GPIO1
    9: 0x4200C000,  # GPIO9
    8: 0x42008000,  # GPIO8
    7: 0x42004000,  # GPIO7
    6: 0x42000000,  # GPIO6
}

# Write a value (0 or 1) to a specific GPIO address
def write_gpio(address, value):
    """
    Write a value to the GPIO register at the given memory address.
    """
    machine.mem32[address] = value

# Read the value (0 or 1) from a specific GPIO address (simulate input)
def read_gpio(address):
    """
    Read the value from the GPIO register at the given memory address.
    """
    return machine.mem32[address]

def test_gpio(pin):
    """
    Test a specific GPIO pin by toggling its output and reading its input state.
    """
    if pin not in GPIO_ADDRESSES:
        print(f"Invalid GPIO {pin}.")
        return
    address = GPIO_ADDRESSES[pin]
    print(f"Testing GPIO {pin} at address {hex(address)}...")
    # Test output (set HIGH, then LOW)
    print(f"GPIO{pin}: Signal HIGH")
    write_gpio(address, 1)  # Set the GPIO to HIGH
    time.sleep(0.5)
    print(f"GPIO{pin}: Signal LOW")
    write_gpio(address, 0)  # Set the GPIO to LOW
    time.sleep(0.5)
    # Test input (read the GPIO state after the change)
    value = read_gpio(address)  # Read the GPIO value
    print(f"GPIO{pin}: Read value (input) = {value}")
    time.sleep(0.5)

def main():
    """
    Main function to run tests on all GPIO pins.
    This function iterates over all the GPIO pins defined in the GPIO_ADDRESSES dictionary,
    testing each pin by calling the `test_gpio` function for each pin.
    """
    print("Starting GPIO test...")
    # Test each GPIO pin by its address
    for pin in GPIO_ADDRESSES:
        test_gpio(pin)
    print("Test completed.")

# Run the GPIO test when the script is executed directly
if __name__ == "__main__":
    main()
