


class SimpleCrypt:

    def encrypt(self, message:str, key:int) -> bytes:
        message_bytes = message.encode('utf8')
        encrypted_bytes = bytearray()
        for byte in message_bytes:
            encrypted_bytes.append(byte ^ key) # operação XOR com a chave
        return bytes(encrypted_bytes)

    def decrypt(self, encrypted_message: bytes, key:int) -> str:
        decrypted_bytes = bytearray()
        for byte in encrypted_message:
            decrypted_bytes.append(byte ^ key)
        return decrypted_bytes.decode('utf8')

    def save_to_file(self, file_path:str, data:bytes) -> None :
        with open(file_path,'wb') as file:
            return file.write(data)

    def load_from_file(self,file_path:str) -> bytes:
        with open(file_path,'rb') as file:
            return file.read()
        

if __name__=='__main__':
    c = SimpleCrypt()

    # Chave de criptografia simples
    key = 123

    # Criptografando uma mensagem
    message = "Mensagem secreta"
    encrypted_message = c.encrypt(message,key)
    print(f'Mensagem criptografada: {encrypted_message}')

    # Salvando em um arquivo
    c.save_to_file('mensagem_secreta.bin',encrypted_message)

    # Lendo do arquivo e descriptografando
    loaded_message = c.load_from_file('mensagem_secreta.bin')
    decrypted_message = c.decrypt(loaded_message, key)
    print(f'Mensagem descriptografada: {decrypted_message}')