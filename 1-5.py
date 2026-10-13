print("====Задание 1====")


def calculate_hourly_transactions(networks_tps):
    hourly_tx = {}

    for network, tps in networks_tps.items():
        hourly_tx[network] = tps * 3600


    leader = max(networks_tps, key=networks_tps.get)

    return hourly_tx, leader



networks = {
    "Ethereum": 30,
    "Binance Smart Chain": 160,
    "Solana": 50000
}


hourly_tx, leader = calculate_hourly_transactions(networks)


for network, tx_count in hourly_tx.items():

    print(f"{network}: {tx_count:,} транзакций/час")

print(f"Лидер: {leader}")

print("====Задание 2====")

def calculate_read_operations(write_ops):

    min_reads = write_ops * 100
    max_reads = write_ops * 10000


    return min_reads, max_reads



writes_per_second = 500


min_r, max_r = calculate_read_operations(writes_per_second)


print(f"Записей в секунду: {writes_per_second:,}")
print(f"Минимум чтений/с: {min_r:,}")
print(f"Максимум чтений/с: {max_r:,}")

print("====Задание 3====")
import hashlib


class Block:
    def __init__(self, index, data, prev_hash):
        self.index = index
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        string_to_hash = str(self.index) + str(self.data) + str(self.prev_hash)
        return hashlib.sha256(string_to_hash.encode()).hexdigest()


chain = []


chain.append(Block(index=0, data="Genesis Block", prev_hash="0"))


chain.append(Block(index=1, data="Transaction 1", prev_hash=chain[-1].hash))


chain.append(Block(index=2, data="Transaction 2", prev_hash=chain[-1].hash))


for block in chain:

    short_hash = block.hash[:16] + "..."
    short_prev = block.prev_hash if block.prev_hash == "0" else block.prev_hash[:16] + "..."

    print(f"Блок {block.index}: hash={short_hash} prev={short_prev}")
print("====Задание 4====")
import hashlib

def get_sha256(input_string):

    return hashlib.sha256(input_string.encode()).hexdigest()


text = "blockchain"


hash_result = get_sha256(text)


print(f"SHA-256('{text}') =")
print(hash_result)
print("====Задание 5====")
import hashlib


def mine_block(data, difficulty):

    prefix = "0" * difficulty
    nonce = 0

    while True:

        string_to_hash = data + str(nonce)
        current_hash = hashlib.sha256(string_to_hash.encode()).hexdigest()


        if current_hash.startswith(prefix):
            return nonce, current_hash


        nonce += 1



block_data = "block1"
target_difficulty = 4


found_nonce, block_hash = mine_block(block_data, target_difficulty)


print(f"difficulty={target_difficulty}, nonce={found_nonce}")
print(f"hash={block_hash}")
