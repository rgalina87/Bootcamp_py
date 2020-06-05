start = input("Would you like to encript (en) or decrypt (de)?\n>>>")
while True:
    if start == "en":

        text = input("Enter your text\n>>>")
        offset = 3

        key = 'abcdefghijklmnopqrstuvwxyz'

        def encrypt(n, plaintext):
          result = ''

          for l in plaintext.lower():
              try:
                  i = (key.index(l) + n) % 26
                  result += key[i]
              except ValueError:
                  result += l
          return result.lower()

        encrypted = encrypt(offset, text)
    print('Encrypted:', encrypted)
    break


while True:
  if start == "de":
    text = input("Enter your text\n>>>")
    offset = 5

    key = 'abcdefghijklmnopqrstuvwxyz'

    def decrypt(n, ciphertext):
        result = ''

        for l in ciphertext:
              try:
                  i = (key.index(l) - n) % 26
                  result += key[i]
              except ValueError:
                result += l
        return result
        decrypted = decrypt(offset, text)
    print('Decrypted:', decrypt)
  break