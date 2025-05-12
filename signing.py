from web3 import Web3
from eth_account.messages import encode_defunct
import json
import sys  # Import sys module to access command-line arguments

# --- Configuration ---
# Dummy private key for testing
# You would replace this with a real private key in a production environment.
# IMPORTANT: Never expose your real private keys.
DUMMY_PRIVATE_KEY = 
# The public address corresponding to the DUMMY_PRIVATE_KEY
# EXPECTED_ADDRESS = "0xA72187c81E3bfe04353bFD4b691b04dda93F1435" # No longer needed for this version


def sign_message(message_text: str, private_key: str) -> str | None:
    """
    Signs a given text message and returns the signature.

    Args:
        message_text (str): The text message to be signed.
        private_key (str): The private key to sign the message with.

    Returns:
        str | None: The hexadecimal representation of the signature, or None if signing fails.
    """
    try:
        w3 = Web3()

        # 1. Encode the message for signing (EIP-191).
        #    encode_defunct prepends "\x19Ethereum Signed Message:\n" + len(message)
        message_encoded = encode_defunct(text=message_text)

        # 2. Sign the encoded message.
        signed_message_object = w3.eth.account.sign_message(
            message_encoded, private_key=private_key
        )

        # 3. Get the signature in hexadecimal format.
        signature_hex = signed_message_object.signature.hex()

        return signature_hex

    except Exception as e:
        print(f"An error occurred during signing: {e}")
        return None


if __name__ == "__main__":
    # --- Get Message from Command-Line Argument ---
    if len(sys.argv) < 2:
        print('Usage: python script_name.py "<message_to_sign>"')
        # Example: python your_script_name.py "{\"name\": \"Lionel Messi\", \"action\": \"goal\"}"
        sys.exit(1)  # Exit if no message is provided

    original_message_from_arg = sys.argv[1]

    print("--- Message Signing ---")
    # Attempt to parse as JSON for pretty printing, but sign the raw string argument
    try:
        # Try to parse as JSON for pretty printing if it's a JSON string
        parsed_json_message = json.loads(original_message_from_arg)
        print(
            f"Original Message (as provided):\n{json.dumps(parsed_json_message, indent=2)}\n"
        )
    except json.JSONDecodeError:
        # If not JSON, just print the raw string
        print(f"Original Message (as provided):\n{original_message_from_arg}\n")

    # --- Sign the Message ---
    # The DUMMY_PRIVATE_KEY is used here. In a real application,
    # this key would be managed securely.
    signature = sign_message(original_message_from_arg, DUMMY_PRIVATE_KEY)

    if signature:
        # Outputting the original message as received from args
        print(
            f"Original Message (raw string used for signing):\n{original_message_from_arg}\n"
        )
        print(f"Signature (Hexadecimal):\n{signature}\n")
    else:
        print("Failed to sign the message.")
