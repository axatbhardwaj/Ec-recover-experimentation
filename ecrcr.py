from typing import cast
import json
from web3 import Web3
from eth_account.messages import encode_defunct

# dummy key pair for testing
# ❯ cast w n
# Successfully created new keypair.
# Address:     0xA72187c81E3bfe04353bFD4b691b04dda93F1435
# Private key: 0x096df25a2615ec4b50fa753b5127526725286d8f54d28c073b818b765cdb8fdb


def recover_address(message, signature):
    """
    Recovers the Ethereum address that signed the given message.

    Args:
        message (str): The original message that was signed.
        signature (str): The signature of the message.

    Returns:
        str: The Ethereum address that signed the message, or None if recovery fails.
    """
    try:
        w3 = Web3()
        message_encoded = encode_defunct(text=message)
        recovered_address = w3.eth.account.recover_message(message_encoded, signature=signature)
        return recovered_address
    except Exception as e:
        print(f"Error recovering address: {e}")
        return None


payload = {
    "name": "Lionel Messi",
    "position": "Forward",
    "club": "FC Barcelona",
}

# Convert payload to a proper string format
message = json.dumps(payload)
print(f"Message: {message}")



# this is the paylaod that is going to be signed by agent's payload 
# function to sign the message
def sign_message(message, private_key):
    w3 = Web3()
    message_encoded = encode_defunct(text=message)
    signed_message = w3.eth.account.sign_message(
        message_encoded, private_key
    )
    return signed_message   

# dummy private key
address = "0xA72187c81E3bfe04353bFD4b691b04dda93F1435"
private_key = "0x096df25a2615ec4b50fa753b5127526725286d8f54d28c073b818b765cdb8fdb"
signature = sign_message(message, private_key)
print(f"Signature: {signature.signature.hex()}")


# Recover the address from the signature and verify it on the DB service
recovered_address = recover_address(message, signature.signature.hex())
print(f"Recovered address: {recovered_address}")

# Verify the recovered address
if recovered_address and recovered_address.lower() == address.lower():
    print("Signature verified successfully!")
else:
    print("Signature verification failed.")