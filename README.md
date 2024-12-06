# Teensy_4.1
Micropython code collection for Teensy 4.1 with MIMXRT1062DVJ6A

- **Teensy_clk.py**: 
  
    This file manages the activation and deactivation of the TRNG (True Random Number Generator) clock in the Clock Control Module (CCM) of the Teensy 4.1 microcontroller        (based on the NXP i.MX RT1062 processor).
  
    The included functions allow checking the status of the clocks and displaying useful information for debugging.
  
- **Teensy_eFUSE_unique_id.py**:

    MicroPython script to read the unique device ID from the eFuse (OTP) memory of a microcontroller. This script reads the 64-bit unique ID stored in the eFuse memory by       accessing the appropriate registers and displays the high and low parts of the ID in hexadecimal format.
    The unique ID is typically used for device identification purposes, especially in security and authentication applications.

- **Teensy_LPUART.py**:
  
    MicroPython script to read the registers of LPUART peripherals from the microcontroller's memory space. It lists various registers such as version, baud rate, and status
    for each LPUART and provides explanations of each register's purpose. [Comments](https://github.com/MicroControleurMonde/Teensy_4.1/blob/main/Teesny_LUPART.md)
  
# References:

- **Arm Platform Memory Map.txt**
Extract from NXP pdf - Arm Platform Memory Map for the i.MX RT1060
