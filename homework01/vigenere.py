from caesar import SIZE_OF_ALPHABET, get_start_ord
from testing import test


def decrypt_key(key: str) -> list[int]:
    """
    Generate a list of integer shifts from a given key for the Vigenere cipher.
    Args:
        key (str): The key used for encryption/decryption,
        consisting only of English letters.
    Returns:
        list[int]: A list of integer shifts
        corresponding to each character in the key.
    Raises:
        ValueError: If the key contains characters that are not
        English letters.
    Example:
        >>> decrypt_key("ABC")
        [0, 1, 2]
        >>> decrypt_key("xyz")
        [23, 24, 25]
        >>> decrypt_key("A1C")
        Traceback (most recent call last):
            ...
        ValueError: Char 1 is not English letter
    """
    assert key and key.isalpha()

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
    Apply a Vigenere cipher to the given text.
    This function supports both encryption and decryption.

    Args:
        plaintext (str): The text to be encrypted or decrypted.
        key (str): The key used for the Vigenere cipher.
        It should be a string of letters.
        decrypt (bool, optional): If True,
        the function will decrypt the plaintext.
        Defaults to False.
        ignore_space (bool, optional): If True,
        non-English letters will be ignored in indexing. Defaults to False.

    Returns:
        str: The resulting encrypted or decrypted text.

    Examples:
        >>> encrypt_vigenere("LXFOPVEFRNHR", "LEMON", decrypt=True)
        'ATTACKATDAWN'
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
            encrypted_alpha = chr(
                start + (char_ord - start + shift) % SIZE_OF_ALPHABET
            )

            i += 1
        else:
            encrypted_alpha = char

            if ignore_space is False:
                i += 1

        raw_ciphertext.append(encrypted_alpha)

    return "".join(raw_ciphertext)


def decrypt_vigenere(
    plaintext: str, key: str, ignore_space: bool = False
) -> str:
    """
    Decrypt a Vigenere cipher to text.
    This function decrypts the given text using the provided key.

    Args:
        plaintext (str): The text to be decrypted.
        key (str): The key used for the Vigenere cipher.
        It should be a string of letters.
        ignore_space (bool, optional): If True,
        non-English letters will be ignored in indexing. Defaults to False.

    Returns:
        str: The decrypted text.

    Examples:
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
        list(zip(plain_texts, keys)),
        cipher_texts,
        encrypt_vigenere,
        {"ignore_space": True},
        True,
    )

    score_decrypt = test(
        list(zip(cipher_texts, keys)),
        plain_texts,
        decrypt_vigenere,
        {"ignore_space": True},
        True,
    )

    print(
        f"Score in encrypt: {score_encrypt}, score in decrypt {score_decrypt}"
    )
