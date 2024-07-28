#A class to implement transposition encryption and decryption.
class TranspositionCipher:
    
    def __init__(self, key):
     
        self.key = key

        #Encrypts a message using the transposition cipher method.

    def encrypt_message(self, message):
        
        # Remove spaces from the message
        message = message.replace(" ", "")
        
        # Calculate the number of rows needed for the grid
        num_rows = len(message) // self.key
        if len(message) % self.key != 0:
            num_rows += 1
        
        # Create an empty grid
        grid = [['' for _ in range(self.key)] for _ in range(num_rows)]
        
        # Fill the grid with the user's message
        index = 0
        for row in range(num_rows):
            for col in range(self.key):
                if index < len(message):
                    grid[row][col] = message[index]
                    index += 1
        
        # Encrypt the message by reading the grid by column
        encrypted_message = ''
        for col in range(self.key):
            for row in range(num_rows):
                if grid[row][col] != '':
                    encrypted_message += grid[row][col]
        
        return encrypted_message
    
        # Decrypts an encrypted message using the transposition cipher method.
    def decrypt_message(self, encrypted_message):
        
        # Calculate the number of columns and rows needed for the grid
        num_cols = self.key
        num_rows = len(encrypted_message) // num_cols
        if len(encrypted_message) % num_cols != 0:
            num_rows += 1
        
        # Calculate the number of empty cells in the last row
        num_empty_cells = (num_cols * num_rows) - len(encrypted_message)
        
        # Create an empty grid
        grid = [['' for _ in range(num_cols)] for _ in range(num_rows)]
        
        # Fill the grid with the encrypted message by columns
        index = 0
        for col in range(num_cols):
            for row in range(num_rows):
                if row == num_rows - 1 and col >= num_cols - num_empty_cells:
                    continue
                if index < len(encrypted_message):
                    grid[row][col] = encrypted_message[index]
                    index += 1
        
        # Decipher the message by reading the grid by rows
        decrypted_message = ''
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] != '':
                    decrypted_message += grid[row][col]
        
        return decrypted_message
        
    def process_message(self):
        
       # creates a menu for the user to choose whether to encrypt or decrypt a message.
        
        choice = input("¿Quieres cifrar o descifrar un mensaje? (cifrar/descifrar): ").lower()
        
        if choice == 'cifrar':
            message = input("Introduce el mensaje a cifrar: ")
            encrypted_message = self.encrypt_message(message)
            print("Mensaje cifrado:", encrypted_message)
        
        elif choice == 'descifrar':
            message = input("Introduce el mensaje a descifrar: ")
            decrypted_message = self.decrypt_message(message)
            print("Mensaje descifrado:", decrypted_message)
        
        else:
            print("Opción no válida. Debes elegir 'cifrar' o 'descifrar'.")

# example 
key = 5  
cipher = TranspositionCipher(key)
cipher.process_message()

