import random
import timeit
from CRC_08_LFSR import CRC8_SAE_J1850

def simulate_crc_error_detection(crc, num_tests: int, burst_error_size: int):
    """Simulates the error detection capability of CRC-8 against burst errors.
    
    Args:
        num_tests (int): Number of messages to test.
        burst_error_size (int): Number of bits flipped per test.

    Returns:
        float: Percentage of detected errors.
    """
    detected_errors = 0

    for _ in range(num_tests):
        payload_device_A = generate_random_data()
        uart_message = crc.generate_uart_message_from_device_A(payload_device_A)

        # Introduce burst error
        corrupted_message = introduce_bit_flip(uart_message, burst_error_size)

        # Check if error is detected
        if not crc.validate_received_message_at_device_B(corrupted_message):
            detected_errors += 1

    detection_rate = (detected_errors / num_tests) * 100
    print("\n" + "*" * 60) # Prints a formatted header for a test case
    print(f"CRC-8 detected {detection_rate:.2f}% of {burst_error_size}-bit errors.")

def measure_crc_execution_time(crc):
    """Measures the execution time of CRC-8 calculation."""
    payload_device_A = generate_random_data()

    # Measure execution time
    execution_time = timeit.timeit(lambda: crc.calculate_crc8(payload_device_A), number=100000)
    avg_time_per_crc = execution_time / 100000
    print("\n" + "*" * 60) # Prints a formatted header for a test case
    print(f"Average CRC-8 Execution Time (Python): {avg_time_per_crc:.6f} sec")

# Helper functions
def print_test_result(test_name, is_valid):
    """Helper function to print the test result, including the test case name."""
    result = "Passed" if is_valid else "Failed"
    print(f"{test_name} - Test {result}")

def generate_random_data() -> bytes:
    """Generates random 8-byte data."""
    return bytes([random.randint(0, 255) for _ in range(8)])

def introduce_bit_flip(data: bytes, burst_error_size: int) -> bytes:
    """Introduces a burst error by flipping 'burst_error_size' bits in the data."""
    corrupted_data = bytearray(data)
    
    for _ in range(burst_error_size):
        byte_index = random.randint(0, len(corrupted_data) - 1)
        bit_index = random.randint(0, 7)  # Flip a random bit in the byte
        corrupted_data[byte_index] ^= (1 << bit_index)  # XOR to flip the bit

    return bytes(corrupted_data)

def main():
    """Main function to execute all test cases."""
    crc = CRC8_SAE_J1850()
    # Run test cases
    simulate_crc_error_detection(crc, num_tests=10000, burst_error_size=2)
    simulate_crc_error_detection(crc, num_tests=10000, burst_error_size=4)
    simulate_crc_error_detection(crc, num_tests=10000, burst_error_size=8)
    measure_crc_execution_time(crc)

if __name__ == "__main__":
    main()