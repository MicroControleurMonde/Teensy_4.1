import machine
import time
"""
File: clock_control.py
Description: This file manages the activation and deactivation of the TRNG (True Random Number Generator) clock
             in the Clock Control Module (CCM) of the Teensy 4.1 microcontroller (based on the NXP i.MX RT1062 processor).
             The included functions allow checking the status of the clocks and displaying useful information for debugging.
Author: [MicroControllerWorld]
Date: [05.12.2024]
Version: 1.0
"""

# Base address for the clock control register
CCM_BASE_ADDR = 0x400FC000  # Base address of CCM (Clock Control Module)
CCM_CCGR6_OFFSET = 0x80     # Offset for the CCGR6 register

def activate_trng_clock():
    """
    Activates the TRNG clock by modifying the CCGR6 register to set the corresponding CG6 bit (bit 12).
    This function activates the TRNG clock and displays the register status before and after activation.
    A delay of 10ms is introduced to allow synchronization of the registers before checking the status.
    """
    print("Activating TRNG clock...")
    # Display the register value before modification
    print(f"Initial value of CCGR6 (before activation): {hex(machine.mem32[CCM_BASE_ADDR + CCM_CCGR6_OFFSET])}")
    # Activate the TRNG clock (CG6)
    machine.mem32[CCM_BASE_ADDR + CCM_CCGR6_OFFSET] |= (1 << 12)  # Bit 12 for CG6
    time.sleep(0.01)  # Small delay to ensure synchronization
    # Display the register value after activation
    print(f"Value of CCGR6 (after activation): {hex(machine.mem32[CCM_BASE_ADDR + CCM_CCGR6_OFFSET])}")
    clock_status = machine.mem32[CCM_BASE_ADDR + CCM_CCGR6_OFFSET]
    print("TRNG clock status after activation:", hex(clock_status))

def deactivate_trng_clock():
    """
    Deactivates the TRNG clock by modifying the CCGR6 register to clear the corresponding CG6 bit (bit 12).
    This function deactivates the TRNG clock and displays the register status before and after deactivation.
    A delay of 10ms is introduced to allow synchronization of the registers before checking the status.
    """
    print("Deactivating TRNG clock...")
    # Display the register value before modification
    print(f"Initial value of CCGR6 (before deactivation): {hex(machine.mem32[CCM_BASE_ADDR + CCM_CCGR6_OFFSET])}")
    # Deactivate the TRNG clock (CG6)
    machine.mem32[CCM_BASE_ADDR + CCM_CCGR6_OFFSET] &= ~(1 << 12)  # Bit 12 for CG6
    time.sleep(0.01)  # Small delay to ensure synchronization
    # Display the register value after deactivation
    print(f"Value of CCGR6 (after deactivation): {hex(machine.mem32[CCM_BASE_ADDR + CCM_CCGR6_OFFSET])}")
    clock_status = machine.mem32[CCM_BASE_ADDR + CCM_CCGR6_OFFSET]
    print("TRNG clock status after deactivation:", hex(clock_status))

def check_clock_status():
    """
    Checks the current status of the TRNG clock by analyzing the bits in the CCGR6 register.
    This function reads the CCGR6 register and checks bits 13-12 (corresponding to CG6) to determine
    whether the TRNG clock is enabled or not. The register status is displayed in hexadecimal.
    """
    clock_status = machine.mem32[CCM_BASE_ADDR + CCM_CCGR6_OFFSET]
    # Convert to unsigned integer
    clock_status_unsigned = clock_status & 0xFFFFFFFF
    # Check bits 13-12 for CG6
    trng_clock_enabled = (clock_status_unsigned >> 12) & 0b11  # Get the 2 bits for CG6
    # Display the status
    if trng_clock_enabled == 0b01 or trng_clock_enabled == 0b10 or trng_clock_enabled == 0b11:
        print("TRNG clock is enabled.")
    else:
        print("TRNG clock is not enabled.")
    # Display the raw value of the register
    print("Raw value of the CCGR6 register:", hex(clock_status_unsigned))

def init_clocks():
    """
    Initializes the system clocks.
    This function initializes the TRNG clock by enabling it, checks its status, then disables it
    and checks its status again. It allows testing the clock activation and deactivation process
    and displays information for debugging purposes.
    """
    print("Initializing clocks...")
    # Activate the TRNG clock
    activate_trng_clock()
    # Check the status of the TRNG clock
    check_clock_status()
    
    # Deactivate the TRNG clock
    deactivate_trng_clock()
    # Check the status after deactivation
    check_clock_status()
    print("Clock initialization complete.")

def main():
    """
    Main function to test the activation and deactivation of clocks.
    This function starts the clock testing process, initializes the clocks, and then waits
    for one second to ensure the clock changes are applied before exiting.
    """
    print("Starting MCU clock test...")
    init_clocks()  # Initialize the clocks
    time.sleep(1)  # Wait a bit to ensure the clock is stable
    print("Clocks initialized.")

if __name__ == "__main__":
    main()
