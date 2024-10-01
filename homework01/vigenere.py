from caesar import SIZE_OF_ALPHABET, get_start_ord
from testing import test


def decrypt_key(key: str) -> list[int]:
    """
    Create key from word for Vigenere ciphere

    in (str): str key (only english letters)
    out (list[int]): key for encrypt/decrypt
    """

    int_key = []

    for char in key:
        char_ord = ord(char)
        start = get_start_ord(char_ord)

        if start is not None:
            int_key.append(char_ord - start)
        else:
            raise ValueError(f"Char {char} is not English letter")

    return int_key


def encrypt_vigenere(
    plaintext: str, key: str, decrypt: bool = False, ignore_space: bool = False
) -> str:
    """
    Apply a Vigenere cipher to text
    (only for english letters, other will be ignored)

    in:
        plaintext       (str):  your text for encrypting
        key             (int):  key for encrypting
        *decrypt        (bool): decrypt plaintext by key, defalut False
        *ignore_space   (bool): ignore not english letters in indexing,
            default True

    out (str):
        encrypted text

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """

    raw_ciphertext = []
    int_key = decrypt_key(key)
    key_size = len(int_key)
    index_shift = 0

    if decrypt:
        int_key = [-i for i in int_key]

    i = 0
    for char in plaintext:
        char_ord = ord(char)
        start = get_start_ord(char_ord)

        if start is not None:
            shift = int_key[(i - index_shift) % key_size]
            encrypted_alpha = chr(start + (char_ord - start + shift) % SIZE_OF_ALPHABET)

            i += 1
        else:
            encrypted_alpha = char

            if ignore_space is False:
                i += 1

        raw_ciphertext.append(encrypted_alpha)

    return "".join(raw_ciphertext)


def decrypt_vigenere(plaintext: str, key: str, ignore_space: bool = False) -> str:
    """
    Decrypt a Vigenre cipher to text
    (only for english letters, other will be ignored)

    in:
        plaintext   (str): your text for decrypting
        key         (str): key for decrypting
        *ignore_space   (bool): ignore not english letters in indexing,
            default True
    out (str):
        decrypted text

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """

    return encrypt_vigenere(plaintext, key, True, ignore_space)


if __name__ == "__main__":
    plain_texts = [
        "PYTHON",
        "python",
        "ATTACKATDAWN",
        "garazhvsyoechoprodaetsyaestakcii",
        "GARAZH KUPI!!",
    ]
    keys = ["A", "a", "LEMON", "nedorogo", "BIRO"]
    cipher_texts = [
        "PYTHON",
        "python",
        "LXFOPVEFRNHR",
        "teuoqvbglshqycvfbhdskgeorwwobqow",
        "HIIOAP BIQQ!!",
    ]

    score_encrypt = test(
        list(zip(plain_texts, keys)), cipher_texts, encrypt_vigenere, {"ignore_space": True}, True
    )

    score_decrypt = test(
        list(zip(cipher_texts, keys)), plain_texts, decrypt_vigenere, {"ignore_space": True}, True
    )

    print(f"Score in encrypt: {score_encrypt}, score in decrypt {score_decrypt}")
