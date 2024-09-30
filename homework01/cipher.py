from typing import Optional

A_ORD = ord('a')
Z_ORD = ord('z')
A_ORD_CAP = ord('A')
Z_ORD_CAP = ord('Z')
SIZE_OF_ALPHABET = Z_ORD - A_ORD + 1


def get_start_ord(char_ord: int) -> Optional[int]:
    '''
    Return ord of 'A' in the alphabet (lower or capital) and None
    if input is not an ord of letter of English alphabet.

    in  (int):
        letter ord
    out (int):
        starter ord or None (if it is not a letter)
    '''

    if A_ORD <= char_ord <= Z_ORD:
        return A_ORD
    elif A_ORD_CAP <= char_ord <= Z_ORD_CAP:
        return A_ORD_CAP

    return None


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    '''
    Apply a Caesar cipher to text
    (only for english letters, other will be ignored)

    in:
        plaintext   (str): your text for encrypting
        *shift      (int): shift for encrypting, default 3
    out (str):
        encrypted text

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    '''

    raw_ciphertext = []

    for char in plaintext:
        char_ord = ord(char)
        start = get_start_ord(char_ord)

        if start is not None:
            encrypted_alpha = chr(
                start + (char_ord - start + shift) % SIZE_OF_ALPHABET)
        else:
            encrypted_alpha = char

        raw_ciphertext.append(encrypted_alpha)

    return ''.join(raw_ciphertext)


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    '''
    Decrypt a Caesar cipher to text
    (only for english letters, other will be ignored)

    in:
        plaintext   (str): your text for decrypting
        *shift      (int): shift for decrypting, default 3
    out (str):
        decrypted text

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    '''

    return encrypt_caesar(ciphertext, shift=-shift)


def decrypt_key(key: str) -> list[int]:
    '''
    Create key from word for Vigenere ciphere

    in (str): str key (only english letters)
    out (list[int]): key for encrypt/decrypt
    '''
    int_key = []

    for char in key:
        char_ord = ord(char)
        start = get_start_ord(char_ord)

        if start is not None:
            int_key.append(char_ord - start)
        else:
            raise ValueError(f'Char {char} is not English letter')

    return tuple(int_key)


def encrypt_vigenere(plaintext: str, key: str, decrypt: bool = False) -> str:
    '''
    Apply a Vigenere cipher to text
    (only for english letters, other will be ignored)

    in:
        plaintext   (str):  your text for encrypting
        key         (int):  key for encrypting
        *decrypt    (bool): decrypt plaintext by key, defalut False
    out (str):
        encrypted text

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    '''

    raw_ciphertext = []
    int_key = decrypt_key(key)
    key_size = len(int_key)
    index_shift = 0

    if decrypt:
        int_key = [-i for i in int_key]

    for i, char in enumerate(plaintext):
        char_ord = ord(char)
        start = get_start_ord(char_ord)

        if start is not None:
            shift = int_key[(i - index_shift) % key_size]
            encrypted_alpha = chr(
                start + (char_ord - start + shift) % SIZE_OF_ALPHABET)
        else:
            encrypted_alpha = char

        raw_ciphertext.append(encrypted_alpha)

    return ''.join(raw_ciphertext)


def decrypt_vigenere(plaintext: str, key: str) -> str:
    '''
    Decrypt a Vigenre cipher to text
    (only for english letters, other will be ignored)

    in:
        plaintext   (str): your text for decrypting
        key         (str): key for decrypting
    out (str):
        decrypted text

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    '''

    return encrypt_vigenere(plaintext, key, True)


if __name__ == '__main__':
    # Ceaser
    print('CEASER')
    plain_texts = ['PYTHON', 'python', 'Python3.6',
                   '', 'abc', 'zaz', 'Prodam garazh']
    cipher_texts = ['SBWKRQ', 'sbwkrq', 'Sbwkrq3.6',
                    '', 'def', 'cdc', 'Surgdp jdudck']

    errors_encrypt = 0
    errors_decrypt = 0

    for i in range(len(plain_texts)):
        encrypted = encrypt_caesar(plain_texts[i])
        decrypted = decrypt_caesar(cipher_texts[i])

        if encrypted != cipher_texts[i]:
            print(encrypted, cipher_texts[i])
            errors_encrypt += 1
        if decrypted != plain_texts[i]:
            print(decrypted, plain_texts[i])
            errors_decrypt += 1

    encrypt_score = f'{len(plain_texts) - errors_encrypt}/{len(plain_texts)}'
    decrypt_score = f'{len(plain_texts) - errors_decrypt}/{len(plain_texts)}'

    print(f'Passed {encrypt_score} tests in encrypt')
    print(f'Passed {decrypt_score} tests in decrypt')

    # Vigenere
    print('\nVIGENERE')
    plain_texts = ['PYTHON', 'python', 'ATTACKATDAWN',
                   'garazhvsyoechoprodaetsyaestakcii']
    keys = ['A', 'a', 'LEMON', 'nedorogo']
    cipher_texts = ['PYTHON', 'python', 'LXFOPVEFRNHR',
                    'teuoqvbglshqycvfbhdskgeorwwobqow']

    errors_encrypt = 0
    errors_decrypt = 0

    for i in range(len(plain_texts)):
        encrypted = encrypt_vigenere(plain_texts[i], keys[i])
        decrypted = decrypt_vigenere(cipher_texts[i], keys[i])

        if encrypted != cipher_texts[i]:
            print(encrypted, cipher_texts[i])
            errors_encrypt += 1
        if decrypted != plain_texts[i]:
            print(decrypted, plain_texts[i])
            errors_decrypt += 1

    encrypt_score = f'{len(plain_texts) - errors_encrypt}/{len(plain_texts)}'
    decrypt_score = f'{len(plain_texts) - errors_decrypt}/{len(plain_texts)}'

    print(f'Passed {encrypt_score} tests in encrypt')
    print(f'Passed {decrypt_score} tests in decrypt')
