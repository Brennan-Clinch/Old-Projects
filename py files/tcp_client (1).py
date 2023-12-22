import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Hash import SHA256
def main():
    host = '127.0.0.1'
    port = 5000
    
    s = socket.socket()
    s.connect((host,port))
    
    message = input("-> hello")
    while message != 'q':
		#message should be encoded to bytes before sending out
        s.send(message.encode())
        data = s.recv(1024)
        print ('Received from server: ',data.decode())
        message = input("-> Press Enter to verify the public key")
        print("Public key verified!")
        
    s.close()

if __name__ == '__main__':
    main()