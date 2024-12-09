# Teensy_4.1
Micropython code collection for Teensy 4.1 with MIMXRT1062DVJ6A

- **Teensy_clk.py**: 
  
    This file manages the activation and deactivation of the TRNG (True Random Number Generator) clock in the Clock Control Module (CCM) of the Teensy 4.1 microcontroller        (based on the NXP i.MX RT1062 processor).
  
    The included functions allow checking the status of the clocks and displaying useful information for debugging. [Code](https://github.com/MicroControleurMonde/Teensy_4.1/blob/main/Teensy_clk.py)
  
- **Teensy_eFUSE_unique_id.py**:

    MicroPython script to read the unique device ID from the eFuse (OTP) memory of a microcontroller. This script reads the 64-bit unique ID stored in the eFuse memory by       accessing the appropriate registers and displays the high and low parts of the ID in hexadecimal format.
    The unique ID is typically used for device identification purposes, especially in security and authentication applications. [Code](https://github.com/MicroControleurMonde/Teensy_4.1/blob/main/Teensy_eFUSE_unique_id.py)

- **Teensy_LPUART.py**:
  
    MicroPython script to read the registers of LPUART peripherals from the microcontroller's memory space. It lists various registers such as version, baud rate, and status
    for each LPUART and provides explanations of each register's purpose. [Comments](https://github.com/MicroControleurMonde/Teensy_4.1/blob/main/Teesny_LUPART.md) - [Code](https://github.com/MicroControleurMonde/Teensy_4.1/blob/main/Teensy_LPUART.py)
  
- **Teensy_gpio_test.py**
  
    Tests GPIO pins by setting their outputs and reading their inputs using direct memory-mapped I/O.
  
- **Teensy_Test_Memories.py**

    Tests Memory for Embedded Systems (BOARD_FLASH / SRAM_DTC / SRAM_ITC / SRAM_OC)

    Negative addresses reported for BOARD_FLASH during the testing (Block -0x20000000, etc.) are likely a result of  incorrect interpretation of the memory addresses.

  
# Reference:

- **Arm Platform Memory Map.txt**

    [Extract from NXP pdf - Arm Platform Memory Map for the i.MX RT1060](https://github.com/MicroControleurMonde/Teensy_4.1/blob/main/Arm%20Platform%20Memory%20Map.txt)
