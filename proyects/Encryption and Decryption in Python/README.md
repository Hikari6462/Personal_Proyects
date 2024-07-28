## Description
The Encryption and Decryption in Python project requires implementing a 

# TranspositionCipher class that incorporates the following elements:

* A constructor function that accepts the encryption key as an argument.
* A method designated to encrypt a message that requires a single parameter: the plaintext message to be encrypted.
* A method dedicated to decrypting a message that requires one argument: the previously encrypted message in ciphertext format.

## Code explanation
1- TranspositionCipher Class:
* Attribute key: A class used to determine the number of columns in the grid used for encryption and decryption.

2- Encrypt_message Method:
* Removes spaces from the message.
* Calculates the number of rows needed for the grid. If the message doesn’t divide evenly by the number of columns, an additional row is added.
* Fills the grid with characters from the message.
* Encrypts the message by reading the characters from the grid column-wise.

3- Decrypt_message Method:
* Calculates the number of columns and rows needed for the grid. If the encrypted message doesn’t divide evenly by the number of columns, an additional row is added.
* Determines the number of empty cells in the last row.
* Fills the grid with characters from the encrypted message column-wise.
* Decrypts the message by reading the characters from the grid row-wise.

4- Process_message Method:

* Asks the user to choose between encrypting or decrypting a message.
* Displays the result based on the user’s selection.

Example

The example creates a Transposition Cipher instance with a key of 5 and allows the user to choose between encrypting or decrypting a message.

