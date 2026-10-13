print("====Задание 6====")
import hashlib


def sha256(data):
    return hashlib.sha256(data.encode()).hexdigest()


def get_merkle_root(transactions):

    current_level = [sha256(tx) for tx in transactions]


    while len(current_level) > 1:
        next_level = []
        for i in range(0, len(current_level), 2):

            if i + 1 < len(current_level):
                combined = current_level[i] + current_level[i + 1]
            else:
                combined = current_level[i] + current_level[i]
            next_level.append(sha256(combined))
        current_level = next_level

    return current_level[0]



txs = ["tx1", "tx2", "tx3", "tx4"]


root = get_merkle_root(txs)


print(f"Merkle root: {root}")
print("====Задание 7====")
def check_51_attack_threat(pool_share):

    return pool_share > 0.5


shares = [0.3, 0.51, 0.49, 0.6]


for p in shares:
    is_threat = check_51_attack_threat(p)
    status = "УГРОЗА (атака 51%)" if is_threat else "безопасно"

    print(f"Доля мощности {p:.0%}: {status}")
print("====Задание 8====")
import random


random.seed(42)

total_transactions = 6
tangle = {}

for i in range(total_transactions):
    if i < 2:

        tangle[i] = "— (начальная)"
    else:

        tangle[i] = random.sample(range(i), 2)


for tx_id, approves in tangle.items():
    print(f"Транзакция {tx_id} подтверждает: {approves}")

print("====Задание 9====")
def calculate_iota_time(n, k=1000):

    return k / n


transaction_counts = [10, 100, 1000]


for n in transaction_counts:
    t = calculate_iota_time(n)

    print(f"n={n:>4} транзакций -> время подтверждения = {t:.2f} усл.ед.")

print("====Задание 10====")

transactions = [
    {"from": "Alice", "to": "Bob", "amount": 50},
    {"from": "Bob", "to": "Alice", "amount": 20},
    {"from": "Alice", "to": "Carol", "amount": 10},
    {"from": "Bob", "to": "Carol", "amount": 15}
]

target_address = "Alice"


alice_txs = [tx for tx in transactions if tx["from"] == target_address or tx["to"] == target_address]


balance = 0
for tx in alice_txs:
    if tx["to"] == target_address:
        balance += tx["amount"]
    if tx["from"] == target_address:
        balance -= tx["amount"]


print(f"Транзакции {target_address} ({len(alice_txs)}):")
for tx in alice_txs:
    print(f"  {tx['from']} -> {tx['to']}: {tx['amount']}")
print(f"Баланс {target_address}: {balance}")
