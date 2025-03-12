# Ethereum EC Recover Experimentation

This project demonstrates how to use elliptic curve signature recovery (EC Recover) in Ethereum to sign messages and recover the signing address. This is a fundamental cryptographic technique used in Ethereum for authentication and verification.

## Overview

EC Recover allows you to:
1. Sign a message with a private key
2. Verify who signed a message by recovering the address from the signature

This is useful for:
- Authentication systems that don't require passwords
- Proving ownership of an Ethereum address
- Verifying the authenticity of messages

## How It Works

The process follows these steps:
1. Create a message (in this case, a JSON payload)
2. Sign the message with a private key
3. The signature is generated
4. Anyone can recover the address that created the signature using the original message and the signature

## Code Explanation

The `ecrcr.py` file contains:

- `sign_message()`: Signs a message with a private key
- `recover_address()`: Recovers the Ethereum address from a message and signature
- Example usage with a dummy key pair for demonstration

## Requirements

- Python 3.13.2+
- Web3.py library

## Installation

```bash
pip install web3
```

## Usage

Run the script:

```bash
python ecrcr.py
```

Expected output:
```
Message: {"name": "Lionel Messi", "position": "Forward", "club": "FC Barcelona"}
Signature: [hex signature]
Recovered address: 0xA72187c81E3bfe04353bFD4b691b04dda93F1435
Signature verified successfully!
```

## Security Notes

- Never share your private keys
- The private key in this code is only for demonstration purposes
- For production use, always use secure key management practices

## Applications

This technique can be used for:
- Decentralized authentication
- Proving ownership of blockchain addresses
- Secure messaging systems
- Smart contract interactions requiring signature verification
