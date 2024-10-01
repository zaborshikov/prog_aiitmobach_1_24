import typing as tp
from typing import Optional

from testing import test

A_ORD = ord("a")
Z_ORD = ord("z")
A_ORD_CAP = ord("A")
Z_ORD_CAP = ord("Z")
SIZE_OF_ALPHABET = Z_ORD - A_ORD + 1


def get_start_ord(char_ord: int) -> Optional[int]:
    """
    Return ord of 'A' in the alphabet (lower or capital) and None
    if input is not an ord of letter of English alphabet.

    in  (int):
        letter ord
    out (int):
        starter ord or None (if it is not a letter)
    """

    if A_ORD <= char_ord <= Z_ORD:
        return A_ORD
    elif A_ORD_CAP <= char_ord <= Z_ORD_CAP:
        return A_ORD_CAP

    return None


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
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
    """

    raw_ciphertext = []

    for char in plaintext:
        char_ord = ord(char)
        start = get_start_ord(char_ord)

        if start is not None:
            encrypted_alpha = chr(
                start + (char_ord - start + shift) % SIZE_OF_ALPHABET
            )
        else:
            encrypted_alpha = char

        raw_ciphertext.append(encrypted_alpha)

    return "".join(raw_ciphertext)


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
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
    """

    return encrypt_caesar(ciphertext, shift=-shift)


def caesar_breaker_brute_force(
    ciphertext: str, dictionary: tp.Set[str]
) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift


if __name__ == "__main__":
    plain_texts = [
        "PYTHON",
        "python",
        "Python3.6",
        "",
        "abc",
        "zaz",
        "Prodam garazh",
    ]
    cipher_texts = [
        "SBWKRQ",
        "sbwkrq",
        "Sbwkrq3.6",
        "",
        "def",
        "cdc",
        "Surgdp jdudck",
    ]

    score_encrypt = test(
        list(zip(plain_texts)),
        cipher_texts,
        encrypt_caesar,
        return_acuracy=True,
    )

    score_decrypt = test(
        list(zip(cipher_texts)),
        plain_texts,
        decrypt_caesar,
        return_acuracy=True,
    )

    print(
        f"Score in encrypt: {score_encrypt}, score in decrypt {score_decrypt}"
    )
