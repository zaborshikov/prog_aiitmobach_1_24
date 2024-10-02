import typing as tp
from random import randint
from typing import Optional

from testing import accuracy_score, test

A_ORD = ord("a")
Z_ORD = ord("z")
A_ORD_CAP = ord("A")
Z_ORD_CAP = ord("Z")
SIZE_OF_ALPHABET = Z_ORD - A_ORD + 1


def get_start_ord(char_ord: int) -> Optional[int]:
    """
    Determine the starting ordinal value for a given character ordinal.

    Args:
        char_ord (int): The ordinal value of the character.

    Returns:
        Optional[int]: The starting ordinal value for the alphabet
        (either lowercase 'a' or uppercase 'A') if the character is
        an English letter. Returns None if the character is not an
        English letter.
    """

    if A_ORD <= char_ord <= Z_ORD:
        return A_ORD
    elif A_ORD_CAP <= char_ord <= Z_ORD_CAP:
        return A_ORD_CAP

    return None


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts the given plaintext using the Caesar cipher technique.
    The Caesar cipher shifts each letter in the plaintext
    by a specified number of positions
    down the alphabet. Non-alphabetic (only english)
    characters are not affected.

    Args:
        plaintext (str): The text to be encrypted.
        shift (int, optional): The number of positions to shift each letter.
        Defaults to 3.

    Returns:
        str: The encrypted text.

    Examples:
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
    Decrypt a Caesar cipher text
    (only for English letters, others will be ignored)

    Args:
        ciphertext (str): The text to be decrypted.
        shift (int): The shift used for decrypting, default is 3.

    Returns:
        str: The decrypted text.

    Examples:
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
    ciphertext: str, dictionary: tp.Set[str], return_text: bool = False
) -> int:
    """
    Attempts to break a Caesar cipher by brute force.
    This function tries all possible shifts
    (from 0 to 24) to decrypt the given
    ciphertext and checks if the resulting
    plaintext is a valid word in the provided
    dictionary. It returns the shift value
    that successfully decrypts the ciphertext
    into a valid word.

    Works only with english letters and spaces.

    Args:
        ciphertext (str): The encrypted message to be decrypted.
        dictionary (tp.Set[str]): A set of valid
        words to check against the decrypted text.

    Returns:
        int: The shift value that successfully
        decrypts the ciphertext into a valid word.
        If no valid word is found, it returns the
        last shift value (24).

    Examples:
        >>> caesar_breaker_brute_force( \
                encrypt_caesar('Hello how are you', shift=6), \
                ("hello", "hi") \
            )
        6
    """
    shift = 0

    for shift in range(24 + 1):
        result = decrypt_caesar(ciphertext, shift)
        for word in result.lower().split():
            if word in dictionary:
                if return_text:
                    return result
                return shift

    return -1


if __name__ == "__main__":

    shifts = [randint(0, 24) for _ in range(9)]
    results = [
        caesar_breaker_brute_force(
            encrypt_caesar("Hello how are you", shift), ("hello", "hi")
        )
        for shift in shifts
    ] + [caesar_breaker_brute_force("Nothing", ("hello", "hi"))]

    shifts.append(-1)

    print(f"Score in bruteforce: {accuracy_score(results, shifts)}")

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
        return_accuracy=True,
    )

    score_decrypt = test(
        list(zip(cipher_texts)),
        plain_texts,
        decrypt_caesar,
        return_accuracy=True,
    )

    print(
        f"Score in encrypt: {score_encrypt}, score in decrypt {score_decrypt}"
    )
