def transform_input(input):
    s = "".join([str(ord(c) - 96) for c in input.replace(" ", "").lower()])
    return [s[i:i + 3] for i in range(0, len(s), 3)]


def main():
    p = 37
    q = 89
    e = 19
    d = 667

    n = p * q
    tab = transform_input("Sophia Antipolis")
    print("input :", end=" ")
    print(tab)
    encrypted = [(int(k) ** e) % n for k in tab]
    print("encrypted :", end=" ")
    print(encrypted)
    decrypted = [(int(k) ** d) % n for k in encrypted]
    print("decrypted :", end=" ")
    print(decrypted)


if __name__ == '__main__':
    main()
