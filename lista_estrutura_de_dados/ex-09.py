from collections import Counter

logs = [
    ('192.168.1.1', 'página_inicial'),
    ('192.168.1.2', 'login'),
    ('192.168.1.1', 'perfil'),
    ('192.168.1.3', 'página_inicial'),
    ('192.168.1.1', 'logout')
]

lista_ips = []

for log in logs:
    lista_ips.append(log[0])

visitantes_unicos = set(lista_ips)

freq_acesso = dict(Counter(lista_ips))

print(f"Visitantes únicos: {len(visitantes_unicos)}")
print(f"Frequência de acesso: {freq_acesso}")

