class CRC8_SAE_J1850:
    """ Handles CRC calculation, and validation. """

    def __init__(self) -> None:
        self.CRC8_POLY: int = 0x1D  # SAE J1850 Polynomial
        self.CRC8_INIT: int = 0xFF  # Initial CRC value
        self.PAYLOAD_SIZE: int = 8   # 8-byte data payload
        self.CRC_SIZE: int = 1       # 1-byte CRC checksum
        self.UART_FRAME_SIZE: int = self.PAYLOAD_SIZE + self.CRC_SIZE  # Total 9-byte UART frame

    def calculate_crc8(self, data: bytes) -> int:
        """Computes SAE J1850 CRC-8 for given data using LFSR methodology."""
        crc: int = self.CRC8_INIT  # Set initial CRC value
        for byte in data:
            crc ^= byte # XOR with the current byte
            for _ in range(8): # Process 8 bits
                if (crc & 0x80) != 0:
                    crc = ((crc << 1) ^ self.CRC8_POLY) & 0xFF
                else:
                    crc = (crc << 1) & 0xFF

        # Apply the final XOR with 0xFF
        crc ^= 0xFF
        return crc

    def generate_uart_message_from_device_A(self, data_bytes: bytes) -> bytes:
        """Device A: Generates UART message with payload + CRC.
        Args:
            data_bytes (bytes): 8-byte payload.
        Returns:
            bytes: 9-byte UART message (Payload + CRC).
        """
        if len(data_bytes) != self.PAYLOAD_SIZE:
            raise ValueError(f"Invalid data length: Expected 8 bytes, got {len(data_bytes)} bytes")
        
        crc8_checksum: int = self.calculate_crc8(data_bytes)
        uart_message: bytes = data_bytes + bytes([crc8_checksum])  # Append CRC
        return uart_message

    def validate_received_message_at_device_B(self, received_message: bytes) -> bool:
        """Device B: Validates received UART message (checks CRC byte-by-byte).
        Args:
            received_message (bytes): 9-byte UART frame.
        Returns:
            bool: True if CRC is correct, False otherwise.
        """
        if len(received_message) != self.UART_FRAME_SIZE:
            raise ValueError(f"Invalid UART message length: Expected 9 bytes, got {len(received_message)} bytes")

        payload: bytes = received_message[:self.PAYLOAD_SIZE]  # Extract 8 bytes
        received_crc: int = received_message[self.PAYLOAD_SIZE]  # Last byte is CRC

        expected_crc: int = self.calculate_crc8(payload)

        print(f"Expected CRC: {expected_crc:#04x}, Received CRC: {received_crc:#04x}")

        if received_crc == expected_crc:
            print("CRC Validation Passed: No errors detected.")
            return True
        else:
            print("CRC Mismatch! Error detected in the message.")
            self.identify_corrupted_bytes(payload, received_message[:self.PAYLOAD_SIZE])
            return False

    def identify_corrupted_bytes(self, original_payload: bytes, received_payload: bytes) -> None:
        """Identifies corrupted bytes and reports bit differences.
        
        Args:
            original_payload (bytes): Expected 8-byte data.
            received_payload (bytes): Received 8-byte data.
        """
        for i in range(self.PAYLOAD_SIZE):
            if original_payload[i] != received_payload[i]:
                error_bits: int = original_payload[i] ^ received_payload[i]  # XOR to find changed bits
                print(f"Byte {i}: Error detected! Bit difference: {error_bits:#010b}")