# Send ETH on Sepolia Network

## Introduction

This script allows you to send ETH on the Sepolia network automatically using Python and the `web3.py` library. Follow the steps below to get started.

---

## Requirements

1. **Python** version 3.x
2. **Libraries**:

   - `web3`

   Install using the command:

   ```bash
   pip install web3
   ```

---

## Steps

### 1. Get an RPC Endpoint

You need an RPC endpoint for the Sepolia network. This can be obtained from providers like [Infura](https://infura.io/) or [Alchemy](https://www.alchemy.com/).

#### How to Get an RPC Endpoint on Infura:

1. Create an account on [Infura](https://infura.io/).
2. Create a new project in the Infura dashboard.
3. Select the `Sepolia` network for your project.
4. Copy the generated RPC endpoint URL.

---

### 2. Prepare Sender and Receiver Wallets

You need:

- **Sender Wallet**: A wallet address with ETH balance on the Sepolia network. The private key of this wallet is required to sign the transaction.
- **Receiver Wallet**: The destination wallet address that will receive the ETH.

---

### 3. Configure the Private Key for the Sender Wallet

The private key is used to sign transactions. Store the private key securely and never share it. Example configuration format in the Python script:

```python
sender_address = "0xYourSenderAddress"
private_key = "YourPrivateKey"
recipient_address = "0xRecipientAddress"
amount = 0.01  # Amount of ETH to send
```

---

## Running the Script

1. Copy the Python code into a file named `index.py`.
2. Run the script using the terminal:
   ```bash
   python index.py
   ```
3. Enter:
   - Sender wallet address
   - Sender wallet private key
   - Receiver wallet address
   - Amount of ETH to send

---

## Important Notes

- **Security**: Never share your private key.
- **Nonce**: This script uses the latest nonce to ensure transactions are not duplicated.
- **Gas Fee**: Ensure the sender wallet has enough balance to cover the gas fees.
