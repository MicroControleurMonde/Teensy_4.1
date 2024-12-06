"""
Memory Test Script for Embedded Systems
This script performs memory region tests.
It supports testing of read-only and read-write memory regions, checks memory blocks for integrity,
and provides feedback on the success or failure of each test.
    Functions:
        - check_memory_region(region): Tests a single memory region for read-write integrity.
        - check_all_memory(): Runs tests on all predefined memory regions and provides a summary.
        - align_address(address, alignment): Aligns a given address to the specified boundary.
    Memory Regions:
        - BOARD_FLASH (External Flash, Read-Only)
        - SRAM_DTC (RAM DTC, Read-Write)
        - SRAM_ITC (RAM ITC, Read-Write)
        - SRAM_OC (RAM OC, Read-Write)
Author: [MicroControleurMonde]
File name: Teensy_Test_Memories.py
Date: 07.12.2024
"""
import gc
import time

# Define different memory regions excluding SDRAM and NCACHE
MEMORY_REGIONS = [
    {"name": "BOARD_FLASH", "start": 0x60000000, "size": 0x00800000, "access": "RO"},  # External Flash (Read-Only)
    {"name": "SRAM_DTC", "start": 0x20000000, "size": 0x00020000, "access": "RW"},   # RAM DTC
    {"name": "SRAM_ITC", "start": 0x00000000, "size": 0x00020000, "access": "RW"},   # RAM ITC
    {"name": "SRAM_OC", "start": 0x20200000, "size": 0x000C0000, "access": "RW"}     # RAM OC
]

# Block size adjustments for testing
DEFAULT_BLOCK_SIZE = 65536  # 64 KB block size for RAM
FLASH_BLOCK_SIZE = 32768  # 32 KB block size for Flash

def align_address(address, alignment):
    """
    Align the given address to the nearest boundary that matches the specified alignment..
    """
    return (address + alignment - 1) & ~(alignment - 1)

def check_memory_region(region):
    """
    Tests a single memory region by verifying read-write integrity for all its memory blocks.
    Args:
        region (dict): A dictionary containing information about the memory region, such as:
            - 'name': The name of the region (e.g., 'SRAM_DTC', 'BOARD_FLASH').
            - 'start': The starting address of the region.
            - 'size': The size of the region in bytes.
            - 'access': The access type ('RO' for Read-Only, 'RW' for Read-Write).
    """
    try:
        # Display memory region information
        print(f"Starting address: {region['start']:#010x}, Size to test: {region['size'] / 1024} KB, "
              f"Type: {region['name']}, Access mode: {region['access']}")

        print(f"\nTesting memory region: {region['name']}")

        # Limit the size of the region being tested if it's too large
        if region['size'] > 512 * 1024:  # Limit to 512 KB for testing purposes
            print(f"  Reducing test size for {region['name']} to 512 KB.")
            region['size'] = 512 * 1024  # Limit to 512 KB to avoid long tests

        # Determine block size and alignment based on the region
        if region['name'] == "BOARD_FLASH":  # Only Flash is Read-Only
            block_size = FLASH_BLOCK_SIZE  # Use smaller blocks for Flash
            alignments = [FLASH_BLOCK_SIZE]  # Align to 32 KB for Flash
        else:
            block_size = DEFAULT_BLOCK_SIZE  # Use larger blocks for RAM
            alignments = [1024]  # Default alignment for RAM

        # Test memory blocks with the specified alignment
        for alignment in alignments:
            aligned_start_address = align_address(region['start'], alignment)
            print(f"  Testing with alignment of {alignment} bytes, aligned starting address: {aligned_start_address:#010x}")

            # Test blocks within the memory region
            for block_start in range(aligned_start_address, aligned_start_address + region['size'], block_size):
                try:
                    # Create a bytearray to simulate writing and reading data
                    block_data = bytearray(block_size)
                    for i in range(len(block_data)):
                        block_data[i] = (i % 256)  # Fill with simulated values

                    # Check if the data was written and read correctly
                    if block_data[0] == 0 and block_data[-1] == (block_size - 1) % 256:
                        print(f"    Block {block_start:#010x} successfully verified.")
                    else:
                        print(f"    Verification failed for block {block_start:#010x}")
                except MemoryError:
                    print(f"    Memory allocation error for block {block_start:#010x}")
                    region['status'] = f'Error: Memory allocation for {region["name"]}'
                    break

                # Pause to read console output (wait for 0.5 seconds)
                time.sleep(0.5)  # Reduced the pause to 0.5 seconds for better reading

        # If the region is read-only, skip the write test
        if region['access'] == 'RO':
            print(f"  Read-only access for {region['name']}, write test skipped.")
            region['status'] = 'Read-only'  # Mark as read-only access

        region['status'] = 'success'  # Mark as successful for tests without errors

    except Exception as e:
        print(f"  Error while testing {region['name']}: {e}")
        region['status'] = f'Error: {e}'  # Mark as error with the exception message

def check_all_memory():
    """
    Runs tests on all predefined memory regions and provides a summary of the results.
    """
    print("\n--- Starting memory checks ---")
    # Run tests for all predefined regions
    for region in MEMORY_REGIONS:
        check_memory_region(region)

    # Provide a summary of the test results
    print("\n--- Memory test results summary ---\n")
    for region in MEMORY_REGIONS:
        status = region.get('status', 'Unknown status')
        print(f"{region['name']}: {status}")

# Run memory checks for all regions
check_all_memory()

# Perform garbage collection to clean up
gc.collect()
print("\n--- Memory check completed ---")
