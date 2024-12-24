from web3 import Web3

# Konfigurasi jaringan Sepolia
# ganti dengan endpointmu sendiri, saya sendiri menggunakan infura RPC
INFURA_URL = "https://sepolia.infura.io/v3/masukkanendpointmetamaskmu"
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Verifikasi koneksi
def is_connected():
    if web3.is_connected():
        print("Terhubung ke jaringan Sepolia")
    else:
        print("Tidak dapat terhubung ke jaringan Sepolia")
        exit()

# Fungsi untuk mengirim ETH secara otomatis
def send_eth(sender_address, private_key, recipient_address, amount_in_ether):
    try:
        # Periksa saldo pengirim
        sender_balance = web3.eth.get_balance(sender_address)
        sender_balance_eth = web3.from_wei(sender_balance, 'ether')
        print(f"Saldo pengirim: {sender_balance_eth} ETH")

        if sender_balance < web3.to_wei(amount_in_ether, 'ether'):
            print("Saldo tidak mencukupi untuk transaksi")
            return

        # Persiapkan transaksi
        nonce = web3.eth.get_transaction_count(sender_address,'pending')
        transaction = {
            'to': recipient_address,
            'value': web3.to_wei(amount_in_ether, 'ether'),
            'gas': 21000,
            'gasPrice': web3.to_wei('10', 'gwei'),
            'nonce': nonce,
            'chainId': 11155111
        }

        # Signature txn
        signed_transaction = web3.eth.account.sign_transaction(transaction, private_key)

        # Kirim transaksi
        tx_hash = web3.eth.send_raw_transaction(signed_transaction.raw_transaction)
        print(f"Transaksi berhasil dikirim! Hash: {web3.to_hex(tx_hash)}")

    except Exception as e:
        print(f"Gagal mengirim ETH: {str(e)}")

if __name__ == "__main__":
    is_connected()

    # Input pengguna untuk alamat pengirim, private key, alamat penerima, dan jumlah ETH
    sender_address = input("Masukkan alamat wallet pengirim: ").strip()
    private_key = input("Masukkan private key wallet pengirim: ").strip()
    recipient_address = input("Masukkan alamat wallet penerima: ").strip()
    amount = float(input("Masukkan jumlah ETH yang akan dikirim: "))

    send_eth(sender_address, private_key, recipient_address, amount)
