def hamming_weight(n: int) -> int:
    cnt = 0
    while n > 0:
        cnt += n & 1
        n >>= 1
    return cnt


if __name__ == "__main__":
    print(hamming_weight(5))
    print(hamming_weight(11))
    print(hamming_weight(4294967293))
    print(hamming_weight(128))