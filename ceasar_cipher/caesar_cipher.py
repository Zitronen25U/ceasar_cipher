from ceasar_cipher.corpus_loader import word_list, name_list


from ntlk import words, names

def encrypt(plain, key):

    encrypted = ""

    for char in plain:
        if (char.isalpha()):
            if (char.isupper()):
                encrypted += chr(((ord(char) + key - 65) % 26) + 65)

            else: 
                encrypted += chr(((ord(char) + key - 97) % 26) + 97)

        else:
            encrypted += char

    return encrypted.lower()


def decrypt(plain, key):
    decrypted = ""
    return encrypt(plain, -key)