'''
    LPUART Register Reader on Teensy 4.1 with NXP i.MX RT1060 (Cortex-M7)

    This script reads the registers of LPUART peripherals from the microcontroller's
    memory space. It lists various registers such as version, baud rate, and status
    for each LPUART and provides explanations of each register's purpose.

    Author: [MicroControleurMonde]
    Date: [06.12.2024]
    Version: 1.0
'''
import machine

def read_register(address, size=4):
    """
    Function to read a register at a given address.
    This function uses machine.mem32 to read 32-bit values from memory at the 
    specified address. It defaults to reading 4 bytes.
    """
    return machine.mem32[address]

def list_lpuart_registers():
    """
    Function to list and read the registers of all LPUART peripherals.
    This function iterates through a predefined list of LPUART peripherals and 
    reads their registers at specific memory addresses. It also provides explanations 
    for each register and handles any errors that occur during the memory read process.
    """
    # Dictionary of LPUART peripherals with their base memory addresses
    lpuarts = {
        'LPUART1 (Serial6)': 0x40184000,
        'LPUART2 (Serial3)': 0x40188000,
        'LPUART3 (Serial2)': 0x4018C000,
        'LPUART4 (Serial4)': 0x40190000,
        'LPUART5 (Serial8)': 0x40194000,
        'LPUART6 (Serial1)': 0x40198000,
        'LPUART7 (Serial7)': 0x4019C000,
        'LPUART8 (Serial5)': 0x401A0000,
    }
    # Dictionary of register names with their offsets from the base address
    registers = {
        'VERID': 0x0,   # Version ID Register
        'PARAM': 0x4,   # Parameter Register
        'GLOBAL': 0x8,  # LPUART Global Register
        'PINCFG': 0xC,  # LPUART Pin Configuration Register
        'BAUD': 0x10,   # LPUART Baud Rate Register
        'STAT': 0x14,   # LPUART Status Register
        'CTRL': 0x18,   # LPUART Control Register
        'DATA': 0x1C,   # LPUART Data Register
        'MATCH': 0x20,  # LPUART Match Address Register
        'MODIR': 0x24,  # LPUART Modem IrDA Register
        'FIFO': 0x28,   # LPUART FIFO Register
        'WATER': 0x2C   # LPUART Watermark Register
    }
    # Dictionary with explanations for each register
    explanations = {
        'VERID': 'Device version ID.',
        'PARAM': 'Parameters of the LPUART device (FIFO capacity, etc.).',
        'GLOBAL': 'Global configuration of the LPUART.',
        'PINCFG': 'Pin configuration for the LPUART.',
        'BAUD': 'Baud rate register (transmission speed).',
        'STAT': 'Status of the LPUART (e.g., transmission and reception errors).',
        'CTRL': 'Control of the LPUART (enable/disable, interrupts, etc.).',
        'DATA': 'Data to transmit or received data.',
        'MATCH': 'Match address for receiving a message.',
        'MODIR': 'Configuration for modem or IrDA.',
        'FIFO': 'FIFO (First-In, First-Out) configuration for data management.',
        'WATER': 'FIFO watermark thresholds (minimum number of data before an interrupt).'
    }
    # Loop through each LPUART and read the registers
    for lpuart_name, base_address in lpuarts.items():
        print(f"\nChecking registers for {lpuart_name} (Base address: {hex(base_address)})")   
        # Read and display all registers for the current LPUART
        for reg_name, offset in registers.items():
            try:
                reg_value = read_register(base_address + offset)
                print(f"{lpuart_name} - Register {reg_name}: {hex(reg_value)}")
                print(f"Explanation: {explanations.get(reg_name, 'No explanation available')}")
            except Exception as e:
                print(f"Error reading register {reg_name} for {lpuart_name}: {e}")

# Run the function to list the LPUART registers
list_lpuart_registers()
