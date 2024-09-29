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
    Apply a Caesar cipher to text (only for english letters, other will be ignored)
    
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
            encrypted_alpha = chr(start + (char_ord - start + shift) % SIZE_OF_ALPHABET)
        else:
            encrypted_alpha = char
        
        raw_ciphertext.append(encrypted_alpha)
                
    return ''.join(raw_ciphertext)


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    '''
    Decrypt a Caesar cipher to text (only for english letters, other will be ignored)
    
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

    return encrypt_caesar(ciphertext, shift= -shift)


if __name__ == '__main__':
    shift = 3
    plain_texts = ['PYTHON', 'python', 'Python3.6', '', 'abc', 'zaz', 'Prodam garazh']
    cipher_texts = ['SBWKRQ', 'sbwkrq', 'Sbwkrq3.6', '', 'def', 'cdc', 'Surgdp jdudck']

    errors_encrypt = 0
    errors_decrypt = 0

    for i in range(len(plain_texts)):
        encrypted = encrypt_caesar(plain_texts[i], shift)
        decrypted = decrypt_caesar(cipher_texts[i], shift)

        if encrypted != cipher_texts[i]:
            print(encrypted, cipher_texts[i])
            errors_encrypt += 1
        if decrypted != plain_texts[i]:
            print(decrypted, plain_texts[i])
            errors_decrypt += 1

    print(f'Passed {len(plain_texts) - errors_encrypt}/{len(plain_texts)} tests in encrypt')
    print(f'Passed {len(plain_texts) - errors_decrypt}/{len(plain_texts)} tests in decrypt')