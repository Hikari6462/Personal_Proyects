# Descripccion 
El proyecto Cifrado y descifrado en Python requiere que implemente una clase TranspositionCipher que incorpore los siguientes elementos:
* Una función constructora que acepta la clave de cifrado como argumento.
* Un método designado para cifrar un mensaje que requiere un único parámetro: el mensaje de texto plano que se va a cifrar.
* Un método dedicado a descifrar un mensaje que requiere un argumento: el mensaje previamente cifrado en formato de texto cifrado.

## Explicación del código
1.	Clase TranspositionCipher:
* Atributo key: una clase que se utiliza para determinar el número de columnas en la cuadrícula utilizada para el cifrado y descifrado.

2.	Método encrypt_message:
*	 Elimina los espacios del mensaje.
*	 Calcula el número de filas necesarias para la cuadrícula. Si el mensaje no se divide exactamente entre el número de columnas, se añade una fila adicional.
*	 Llena la cuadrícula con los caracteres del mensaje.
*	 Cifra el mensaje leyendo los caracteres de la cuadrícula por columnas.

3.	Método decrypt_message:
* Calcula el número de columnas y filas necesarias para la cuadrícula. Si el mensaje cifrado no se divide exactamente entre el número de columnas, se añade una fila adicional.
* Calcula el número de celdas vacías en la última fila.
* Llena la cuadrícula con los caracteres del mensaje cifrado por columnas.
* Descifra el mensaje leyendo los caracteres de la cuadrícula por filas.

4.	Método process_message:
*	Solicita al usuario elegir entre cifrar o descifrar un mensaje.
*	muestra el resultado segun haya selecionado el usuario.

Example
El ejemplo crea una instancia de TranspositionCipher con una clave de 5 y permite al usuario elegir entre cifrar o descifrar un mensaje.

