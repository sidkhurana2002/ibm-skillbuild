import cv2
import os
import hashlib
import time

# Encryption/Decryption functions
def encrypt_message(message):
    encrypted_msg = ""
    for char in message:
        encrypted_msg += chr(ord(char) + 1)
    return encrypted_msg

def decrypt_message(encrypted_msg):
    message = "" 
    for char in encrypted_msg:
        message += chr(ord(char) - 1)
    return message

# Password hashing 
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Main code
img = cv2.imread("Linux.jpg")

msg = input("Enter message: ")
encrypted_msg = encrypt_message(msg)  
password = input("Enter password: ")
hashed_password = hash_password(password)  

# Dictionary mappings    
d = {}
c = {}
for i in range(256):
    d[chr(i)] = i
    c[i] = chr(i)   

m = 0
n = 0

# Hide encrypted message  
for i in range(len(encrypted_msg)):
    img[n, m, 2] = d[encrypted_msg[i]]  
    n += 1
    m += 1

output_image_name = "stego_" + time.strftime("%Y%m%d%H%M%S") + ".jpg"

try:
    cv2.imwrite(output_image_name, img)
    os.startfile(output_image_name) 
except Exception as e:
    print(f"Error: {e}")   

# Retrieve and decrypt message
message = "" 
m = 0
n = 0

pas = input("Enter password: ") 

if hash_password(pas) == hashed_password:
    for i in range(len(encrypted_msg)):
        message += c[img[n, m, 2]]
        n += 1
        m += 1
        
    message = decrypt_message(message) 
    print("Hidden message:", message)
else:
    print("Wrong password")