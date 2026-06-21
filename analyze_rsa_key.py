# -*- coding: utf-8 -*-
import sys
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

def inspect_public_key():
    # Открытый ключ (содержит только N и e)
    public_pem = b"""-----BEGIN PUBLIC KEY-----
MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAKj34GkxFhD90vcNLYLInFEX6Ppy1tPf
9Cnzj4p4WGeKLs1Pt8QuKUpRKfFLfRYC9AIKjbJTWit+CqvjWYzvQwECAwEAAQ==
-----END PUBLIC KEY-----"""

    print("=" * 80)
    print("        АНАЛИЗ ОТКРЫТОГО КЛЮЧА RSA: ЧТО ВИДИТ ВНЕШНИЙ НАБЛЮДАТЕЛЬ")
    print("=" * 80)

    # Загружаем открытый ключ
    public_key = serialization.load_pem_public_key(
        public_pem,
        backend=default_backend()
    )

    public_numbers = public_key.public_numbers()
    n = public_numbers.n
    e = public_numbers.e

    print(f" Открытая экспонента (e)  : {e}")
    print(f" Размер модуля (N)        : {n.bit_length()} бит")
    print(f" Публичный модуль (N)     : {n}")
    print("-" * 80)
    
    # Пытаемся обратиться к секретным сомножителям p и q
    try:
        p = public_key.private_numbers().p
        print(f" Секретный множитель (p)  : {p}")
    except AttributeError:
        print(" Секретный множитель (p)  : НЕ ДОСТУПЕН (Отсутствует в открытом ключе)")

    try:
        q = public_key.private_numbers().q
        print(f" Секретный множитель (q)  : {q}")
    except AttributeError:
        print(" Секретный множитель (q)  : НЕ ДОСТУПЕН (Отсутствует в открытом ключе)")
        
    print("-" * 80)
    print(" ЗАДАЧА ВЗЛОМА: Найти два простых числа p и q, чтобы p * q == N")
    print("=" * 80)

if __name__ == "__main__":
    inspect_public_key()
