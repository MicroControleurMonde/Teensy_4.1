'''
    Source: https://forum.pjrc.com/index.php?threads/teensy-4-x-unique_id.76004/#post-351089
    Credit: PaulS (14.10.2024)
    Code porting to read out 64-bit hardware Unique_ID and MAC Address OUI for Teensy 4.1
    Author: [MicroControleurMonde]
    File name: Teensy_eFUSE_unique_id.py
    Date: 09.12.2024
'''
import time
import machine

# Addresses of the CFG0, CFG1, and MAC0 registers
CFG0 = 0x401F4410
CFG1 = 0x401F4420
MAC0 = 0x401F4620

def read_unique_id():
    """
    Reads the unique ID from the hardware by accessing the CFG0 and CFG1 registers. Unique ID is a 64-bit identifier.
        Returns:
            str: The 64-bit unique ID formatted as a hexadecimal string.
    """
    print("Reading Unique ID...")
    try:
        # Read the values of CFG0 and CFG1
        cfg0_value = machine.mem32[CFG0]
        cfg1_value = machine.mem32[CFG1]
        #print("CFG0 Value: {:08X}".format(cfg0_value)) # Optional Print Debug
        #print("CFG1 Value: {:08X}".format(cfg1_value)) # Optional Print Debug

        # Format the Unique_ID as 64-bit hexadecimal value
        unique_id = "{:08X} {:08X}".format(cfg0_value, cfg1_value)
        print("Unique ID: " + unique_id)  # Full Unique ID displayed in hexa
        return unique_id
    except Exception as e:
        print(f"Error reading Unique ID: {e}")
        raise

def read_mac_address():
    """
    Reads the MAC address from the hardware by accessing the MAC0 register.
    The MAC address is derived from the first 24 bits of the 32-bit MAC0 value.
    These 24 bits represent the Organizationally Unique Identifier (OUI) and part 
    of the MAC address. The remaining 24 bits of the full 48-bit MAC address are 
    managed by the manufacturer and are not accessible directly from this register.
    Returns:
        str: The MAC address formatted as a string in the form XX:XX:XX:00:00:00, 
             where the last 3 octets are set to 00 for demonstration purposes.
    """
    print("Reading MAC Address...")
    try:
        # Read the value from the MAC0 register
        mac_value = machine.mem32[MAC0] & 0xFFFFFFFF   # Mask to ensure the value is unsigned
        #print("MAC0 Value: {:08X}".format(mac_value)) # Optional Print Debug

        # The MAC address is stored in the first 24 bits of MAC0
        mac_address = mac_value & 0xFFFFFF

        # Format the MAC address into 6 octets for display (last 3 octets set to 00)
        mac_formatted = "{:02X}:{:02X}:{:02X}:{:02X}:{:02X}:{:02X}".format(
            (mac_address >> 16) & 0xFF,
            (mac_address >> 8) & 0xFF,
            mac_address & 0xFF,
            0x00, 0x00, 0x00  # The last 3 octets are fixed to 00:00:00
        )
        print("MAC Address: " + mac_formatted)  # Display the MAC address
        return mac_formatted
    except Exception as e:
        print(f"Error reading MAC Address: {e}")
        raise

def reset():
    """
    Performs a software reset of the microcontroller.
    This function is useful for restarting the device after performing the necessary 
    operations or for testing purposes. The reset is currently disabled during testing 
    to prevent an unexpected disconnection.
    """
    print("Performing software reset...")
    machine.reset()  # Perform a software reset after a delay or event

# UART configuration for serial communication
print("Initializing UART...")
try:
    uart = machine.UART(1, baudrate=115200)   # UART with default configuration, you can test with UART(0) or UART(2) as well
    uart.init(bits=8, parity=None, stop=2)    # Specify UART parameters (if needed)
    #print("UART initialized successfully.")  # Optional Print Debug
except Exception as e:
    print(f"Error initializing UART: {e}")
    raise

# Initialize the built-in LED pin to indicate the board is active
print("Initializing LED...")
try:
    pin = machine.Pin("LED", machine.Pin.OUT)   # Integrated LED pin for Teensy 4.1
    pin.value(1)  								# Turn the LED on
    time.sleep(1)
    #print("LED is ON.") 						# Optional Print Debug
except Exception as e:
    print(f"Error initializing LED: {e}")
    raise

# Read the Unique_ID
try:
    unique_id = read_unique_id()
    uart.write(unique_id + "\n")
except Exception as e:
    print(f"Error reading Unique ID: {e}")
    raise

# Read the MAC Address
try:
    mac_address = read_mac_address()
    uart.write("MAC Address: " + mac_address + "\n")
except Exception as e:
    print(f"Error reading MAC Address: {e}")
    raise

''' Display a message before performing a reset (optional - to light off the LED) '''
# print("About to reset in 3 seconds...")
# uart.write("About to reset in 3 secs...\n")
# time.sleep(3)
# Perform a software reset (optional)
# reset()

