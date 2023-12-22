import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Hash import SHA256
random_generator = Random.new().read


def main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host,port))

    s.listen(1)
    c, addr = s.accept()
    print ("Connection from: ",addr)
    while True:
		#data is in bytes format, use decode() to transform it into a string
        data = c.recv(1024)
        if not data:
            break
        print ("from connected user: ",data.decode())
        if data == 'hello':
            print ("Start the SSL handshake...")
            input ("Press Enter to generate the key pair.")
            key = RSA.generate(1024, random_generator)
            public_key = key.publickey()
            print ("Key pair generated.")
            input ("Press Enter to send the public key to the client.")
            print ("Sending the public key...")
            c.send(public_key.exportkey())
            print ("Public key sent.")
            print ("Waiting for the secret list...")


            if c.recv(1024):
                print ("List received.")
            input ("Press Enter to check the information from the list.")
            info_to_be_encrypted = "It seems all secure. Let's talk!"
            aes = AES.new(decrypted_info, AES.MODE_ECB)
            cipher_text = aes.encrypt(info_to_be_encrypted)
            print ("Sending the cipher text...")
            #data = str(data).upper()
            print ("sending: ",data.decode())
            c.send(data.decode().upper().encode())
            print ("Cipher text sent")

if __name__ == '__main__':
    main()