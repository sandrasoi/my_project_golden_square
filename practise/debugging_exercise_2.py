def encode(text, key):
    cipher = make_cipher(key)
    print(cipher)

    ciphertext_chars = []
    for i in text:
        print(f"Cipher index of {i} is: {cipher.index(i)}")
        #print(f"The i is {i}")
        ciphered_char = chr(65 + cipher.index(i))
        #print(f"Encoding is done by taking the character {i}")
        #print(cipher.index(i))
        ciphertext_chars.append(ciphered_char)

    return "".join(ciphertext_chars)


def decode(encrypted, key):
    cipher = make_cipher(key)
    #print(cipher)

    plaintext_chars = []
    for i in encrypted:
        #print(f"This is i: {i}")
        #plain_char = cipher[65 - ord(i)]
        plain_char = cipher[ord(i)-65]
        print(ord(i))
        print(plain_char)
        #print(f"This is ord(i): {ord(i)}")
        #print(f"This is the plain char decoded: {plain_char}")
        plaintext_chars.append(plain_char)

    return "".join(plaintext_chars)


def make_cipher(key):
    alphabet = [chr(i + 97) for i in range(0, 26)]
    cipher_with_duplicates = list(key) + alphabet

    cipher = []
    for i in range(0, len(cipher_with_duplicates)):
        if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
            cipher.append(cipher_with_duplicates[i])

    return cipher

# When you run this file, these next lines will show you the expected
# and actual outputs of the functions above.
print(f"""Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")
Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
""")


print(f"""
Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
Expected: theswiftfoxjumpedoverthelazydog
Actual: {decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')}
""")