print("====Задание 11====")

query_log = [
    ("uniswap", 5000),
    ("aave", 8500),
    ("uniswap", 7500),
    ("compound", 4500)
]


subgraph_stats = {}
for sg, cnt in query_log:
    subgraph_stats[sg] = subgraph_stats.get(sg, 0) + cnt


most_loaded = max(subgraph_stats, key=subgraph_stats.get)


total_queries = sum(subgraph_stats.values())


for sg, cnt in subgraph_stats.items():
    print(f"{sg}: {cnt:,} запросов")

print(f"Самый нагруженный: {most_loaded}")
print(f"Всего запросов: {total_queries:,}")

print("====Задание 12====")
import hashlib

def sign(message, private_key):

    data = message + private_key
    return hashlib.sha256(data.encode()).hexdigest()

def verify(message, signature, private_key):

    expected_signature = sign(message, private_key)
    return expected_signature == signature


msg = "Send 10 BTC to Bob"
fake_msg = "Send 100 BTC to Bob"
secret_key = "my_secret_key"


sig = sign(msg, secret_key)


check_valid = verify(msg, sig, secret_key)

check_invalid = verify(fake_msg, sig, secret_key)

short_sig = sig[:24] + " ..."


print(f"Подпись: {short_sig}")
print(f"Проверка верной подписи: {check_valid}")
print(f"Проверка при подмене сообщения: {check_invalid}")

print("====Задание 13====")
def compare_bits_and_qubits(n):

    quantum_states = 2 ** n
    classical_states = n
    return quantum_states, classical_states


qubits_list = [1, 2, 8, 127]


for n in qubits_list:
    q_states, c_states = compare_bits_and_qubits(n)

    print(f"{n:>3} кубит(ов): {q_states:,} состояний одновременно | классика: {c_states} состояний")
print("====Задание 14====")
def factorize(n):
    factors = []
    d = 2

    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors


numbers = [15, 21, 91]


for num in numbers:
    result_factors = factorize(num)

    print(f"{num} = {' x '.join(map(str, result_factors))}")
print("====Задание 15====")

generations = [127, 433, 1121]


growth_rates = []
for i in range(len(generations) - 1):
    rate = generations[i+1] / generations[i]
    growth_rates.append(rate)


avg_growth_rate = sum(growth_rates) / len(growth_rates)


forecast = round(generations[-1] * avg_growth_rate)


rounded_rates = [round(r, 2) for r in growth_rates]


print(f"Поколения кубитов: {generations}")
print(f"Коэффициенты роста: {rounded_rates}")
print(f"Средний темп роста: x{avg_growth_rate:.2f}")
print(f"Прогноз следующего поколения: ~{forecast} кубитов")
