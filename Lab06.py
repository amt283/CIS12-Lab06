def main():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = 'YIPPEE'
    message = 'They mostly come at night. Mostly.'

    #vigenere_header(alphabet)
    #vigenere_sq(alphabet)
    print(encrypt_vigenere(key, message, alphabet))

def vigenere_header(alphabet):
    alpha_len = len(alphabet)
    for i in range(alpha_len):
        alpha_shift = alphabet[i % alpha_len]
        if i == 0:
            print(f"|   | {alpha_shift}", end=' ')
        else:
            print(f"| {alpha_shift}", end=' ')
    print("|")
    print(f"{'|---'*(alpha_len + 1)}|")

def vigenere_sq(alphabet):
    alpha_len = len(alphabet)
    for shift in range(26):
        for i in range(alpha_len):
            if i == 0:
                alpha_shift = alphabet[(i + shift) % alpha_len]
                print(f"| {alpha_shift}", end = ' ')
                print(f"| {alpha_shift}", end=' ')
            else:
                print(f"| {alphabet[(i + shift) % alpha_len]}", end = ' ')
        print("|")

def letter_to_index(letter, alphabet:str):
    return alphabet.lower().index(letter.lower())

def index_to_letter(index, alphabet):
    if 0 <= index < len(alphabet):
        return alphabet[index]
    return ''

def vigenere_index(key_letter, plaintext_letter, alphabet):
    return (letter_to_index(key_letter,alphabet) +
            letter_to_index(plaintext_letter,alphabet)) % len(alphabet)

def encrypt_vigenere(key, plaintext, alphabet):
    cipher_text = ''
    counter = 0
    for i, c in enumerate(plaintext):
        if c == ' ':
            cipher_text += ' '
        elif c.upper() in alphabet:
            cipher_text += index_to_letter(vigenere_index(key[i%len(key)], c, alphabet),alphabet)
            counter += 1
    return cipher_text

if __name__ == "__main__":
    main()