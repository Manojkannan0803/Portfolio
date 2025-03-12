from CRC_08_LFSR import CRC8_SAE_J1850

# Define a test suite function to organize all tests
def run_test_suite():
    """Main function to execute all tests."""
    payload_device_A = bytes([0x12, 0x34, 0x56, 0x78, 0x9A, 0xBC, 0xDE, 0xF0])
    crc = CRC8_SAE_J1850() # Creating an instance of CRC8_SAE_J1850 class

    tests = [
        lambda: test_crc8_normal_operation(payload_device_A, crc),
        lambda: test_single_byte_corruption(payload_device_A, crc),
        lambda: test_multiple_bytes_corruption(payload_device_A, crc),
        lambda: test_multiple_bytes_corruption_with_crc(payload_device_A, crc),
        lambda: test_all_zero_data(crc),
        lambda: test_all_ff_data(crc),
        lambda: test_boundary_byte_values(crc),
        lambda: test_short_message(payload_device_A, crc),
        lambda: test_extra_long_message(payload_device_A, crc),
    ]
    
    for test in tests:
        test()

# Define individual test functions

def test_crc8_normal_operation(payload_device_A, crc):
    """Test case: Normal operation of CRC-8/SAE-J1850"""
    # Generate the UART message from Device A (with CRC)
    uart_message = crc.generate_uart_message_from_device_A(payload_device_A)
    crc_checksum = uart_message[-1]

    # Validate the message on Device B
    print("\n" + "*" * 60) # Prints a formatted header for a test case
    validation_result = crc.validate_received_message_at_device_B(uart_message)
    print_test_result("test_crc8_normal_operation", validation_result)

def test_single_byte_corruption(payload_device_A, crc):
    """Test case: Corruption of a single byte in the message"""
    uart_message = crc.generate_uart_message_from_device_A(payload_device_A)

    # Corrupt the data by changing one byte
    corrupted_data = bytearray(uart_message)
    corrupted_data[4] = 0x79  # Corrupt the 4th byte (0x78 -> 0x79)

    # Device B validates the corrupted message
    print("\n" + "*" * 60) # Prints a formatted header for a test case
    validation_result = crc.validate_received_message_at_device_B(bytes(corrupted_data))
    print_test_result("test_single_byte_corruption", validation_result)

def test_multiple_bytes_corruption(payload_device_A, crc):
    """Test case: Corruption of multiple bytes in the message"""
    uart_message = crc.generate_uart_message_from_device_A(payload_device_A)

    # Corrupt the data by changing one byte
    corrupted_data = bytearray(uart_message)
    corrupted_data[1] = 0x99  # Corrupt the 2nd byte (0x34 -> 0x99)
    corrupted_data[4] = 0xBB  # Corrupt the 5th byte (0x9A -> 0xBB)

    # Device B validates the corrupted message
    print("\n" + "*" * 60) # Prints a formatted header for a test case
    validation_result = crc.validate_received_message_at_device_B(bytes(corrupted_data))
    print_test_result("test_multiple_bytes_corruption", validation_result)

def test_multiple_bytes_corruption_with_crc(payload_device_A, crc):
    """Limitation of the Current CRC-8/SAE-J1850 Algorithm"""
    """Test case: Corruption of both message data and CRC checksum"""
    uart_message = crc.generate_uart_message_from_device_A(payload_device_A)

    # Corrupt the data by changing one byte and the CRC checksum
    corrupted_data = bytearray(uart_message)
    corrupted_data[1] = 0x99  # Corrupt the 2nd byte (0x34 -> 0x99)
    corrupted_data[8] = 0xFF  # Corrupt the CRC checksum (0x35 -> 0xFF)

    # Device B validates the corrupted message
    print("\n" + "*" * 60) # Prints a formatted header for a test case
    validation_result = crc.validate_received_message_at_device_B(bytes(corrupted_data))
    print_test_result("test_multiple_bytes_corruption_with_crc", validation_result)

def test_all_zero_data(crc):
    """Test case: All zero data"""
    payload_device_A = bytes([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    uart_message = crc.generate_uart_message_from_device_A(payload_device_A)

    # Device B validates the corrupted message
    print("\n" + "*" * 60) # Prints a formatted header for a test case
    validation_result = crc.validate_received_message_at_device_B(uart_message)
    print_test_result("test_all_zero_data", validation_result)

def test_all_ff_data(crc):
    """Test case: All 0xFF data"""
    payload_device_A = bytes([0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF])
    uart_message = crc.generate_uart_message_from_device_A(payload_device_A)

    # Device B validates the corrupted message
    print("\n" + "*" * 60) # Prints a formatted header for a test case
    validation_result = crc.validate_received_message_at_device_B(uart_message)
    print_test_result("test_all_ff_data", validation_result)

def test_boundary_byte_values(crc):
    """Test case: Alternating 0x00 and 0xFF data"""
    payload_device_A = bytes([0x00, 0xFF, 0x00, 0xFF, 0x00, 0xFF, 0x00, 0xFF])
    uart_message = crc.generate_uart_message_from_device_A(payload_device_A)

    # Device B validates the corrupted message
    print("\n" + "*" * 60) # Prints a formatted header for a test case
    validation_result = crc.validate_received_message_at_device_B(uart_message)
    print_test_result("test_boundary_byte_values", validation_result)

def test_short_message(payload_device_A, crc):
    """Test case: Short message (truncated)"""
    uart_message = crc.generate_uart_message_from_device_A(payload_device_A)

    # Simulate truncation by shortening the message (remove the last byte - CRC)
    truncated_message = uart_message[:-1]  # Truncate the message to 8 bytes (no CRC)

    # Device B validates the corrupted message
    try:
        print("\n" + "*" * 60) # Prints a formatted header for a test case
        validation_result = crc.validate_received_message_at_device_B(truncated_message)
        print_test_result("test_short_message", validation_result)
    except ValueError as e:
        print("test_short_message -> Test Failed:", e)

def test_extra_long_message(payload_device_A, crc):
    """Test case: Extra long message (add extra byte)"""
    uart_message = crc.generate_uart_message_from_device_A(payload_device_A)

    # Simulate extra data by adding an extra byte to the message
    longer_message = uart_message + bytes([0x01])  # Add an extra byte at the end

    # Device B validates the corrupted message
    try:
        print("\n" + "*" * 60) # Prints a formatted header for a test case
        validation_result = crc.validate_received_message_at_device_B(longer_message)
        print_test_result("test_extra_long_message", validation_result)
    except ValueError as e:
        print("test_extra_long_message -> Test Failed:", e)

# Helper functions
def print_uart_message_info(payload_device_A, uart_message, crc_checksum):
    """Helper function to print UART message details."""
    print("Original Data (in binary):")
    for byte in payload_device_A:
        print(f"{byte:08b}", end=" ")
    print()
    print(f"Generated UART Message (Payload + CRC): {uart_message.hex()}")
    print(f"CRC checksum computed: {crc_checksum:#04x}")

def print_test_result(test_name, is_valid):
    """Helper function to print the test result, including the test case name."""
    if is_valid:
        print(f"{test_name} - Test Passed: CRC Validation Passed (No errors detected).")
    else:
        print(f"{test_name} - Test Failed: CRC Mismatch (Error detected in the message).")

# Entry point: Run the test suite
if __name__ == "__main__":
    run_test_suite()