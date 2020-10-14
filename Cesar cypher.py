alphabet = 'abcdefghijklmnopqrstuvwxyz'
cypher  = 5

message = input("Enter your message\n>>>")
encrypted_msg   = ""

message = message.lower()

# Encryption
for letter in message:

    if letter in alphabet:
        # Calculate the index of the letter
        ix = 0
        for l in alphabet:
            if l == letter:
                break
            ix += 1

        encrypted_ix = ix + cypher

        if encrypted_ix > 26:
            encrypted_ix -= 27

        encrypted_letter = alphabet[encrypted_ix]
        encrypted_msg += encrypted_letter

    else:
        encrypted_msg += letter

print("Encrypted message:", encrypted_msg)

decrypted_msg = ""

# Decryption
for letter in encrypted_msg:

    if letter in alphabet:
        # Calculate the index of the letter
        ix = 0
        for l in alphabet:
            if l == letter:
                break
            ix += 1

        decrypted_ix = ix - cypher

        if encrypted_ix < 0:
            encrypted_ix += 27

        decrypted_letter = alphabet[decrypted_ix]
        decrypted_msg += decrypted_letter

    else:
        decrypted_msg += letter


print("Decrypted:", decrypted_msg)