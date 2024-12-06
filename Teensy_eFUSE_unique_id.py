import machine
"""
MicroPython script to read the unique device ID from the eFuse (OTP) memory of a microcontroller.
This script reads the 64-bit unique ID stored in the eFuse memory by accessing the appropriate 
registers and displays the high and low parts of the ID in hexadecimal format.
The unique ID is typically used for device identification purposes, especially in security and 
authentication applications.
Author: [MicroControleurMonde]
Date: [05.12.2024]
"""
# Base address of the eFuse (OTP) for the UNIQUE_ID
EFUSE_BASE_ADDR = 0x400F8000  # Base address of the OCOTP
UNIQUE_ID_ADDR = EFUSE_BASE_ADDR + 0x420  # Address of ID starts

# Function to read a register at a specific address
def read_register(address):
    """
    Read a 32-bit value from a memory-mapped register at the specified address.
    Args:
        address (int): The memory address to read from.
    Returns:
        int: The 32-bit value read from the register.
    """
    return machine.mem32[address]

# Function to read and display the unique device ID
def read_unique_id():
    """
    Reads the 64-bit unique ID from the eFuse (OTP) memory and displays both 
    the high and low parts in hexadecimal format.
    The unique ID is split across two 32-bit registers, and the script combines 
    them to form a 64-bit ID.
    """
    print("Reading unique ID:")
    # Read the 64-bit unique ID (2 registers, each 32 bits)
    unique_id_high = read_register(UNIQUE_ID_ADDR)  # High part of the unique ID
    print("DEBUG Higher part of unique ID (hex) :", hex(unique_id_high))
    unique_id_low = read_register(UNIQUE_ID_ADDR + 4)  # Low part of the unique ID
    print("DEBUG Lower part of unique ID (hex) :", hex(unique_id_low))
    # Combine the two parts to get the full 64-bit ID
    unique_id = (unique_id_high << 32) | unique_id_low
    # Display the full 64-bit unique ID in hexadecimal format
    print(f"Device unique ID (hex) : {unique_id:#018x}")
# Test reading the unique ID
read_unique_id()
