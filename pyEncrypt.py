import os
from cryptography.fernet import Fernet

os.system("clear")
encryptOrDecrypt = input("\nEncrypt or Decrypt?\n1) Encrypt\n2) Decrypt\n\n")

    
# Functions
def write_key():
    # Generate key
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    # Loads existing key
    return open("key.key", "rb").read()



# User interaction
if(encryptOrDecrypt == "1"):

    os.system("clear")
    createOrLoad = input("\nCreate or load existing key?\n1) Create\n2) Load\n\n")

    os.system("clear")
    fileName = "files/" + input("\nWhat's the file called?\n\n")

    if(createOrLoad == "1"):
        write_key() # writing a key

    key = load_key() # loading the newly created key

    file = open(fileName, 'r') # opening text file
    fileContent = file.read().encode("utf-8") # saving text as utf-8 encoding to var
    file.close()

    fernet = Fernet(key) # initializing the Fernet class
    encrypted = fernet.encrypt(fileContent) # encrypting the text

    if fileName.startswith("files/"):
        fileName = fileName[len("files/"):]


    # Writing encrypted file to output file
    outputFile = open("files/(e) " + fileName, "w")
    outputFile.write(encrypted.decode("utf-8"))
    outputFile.close()

    os.system("clear")
    print("\nDone!\n")



elif(encryptOrDecrypt == "2"):

    os.system("clear")
    fileName = "files/" + input("\nWhat's the file called?\n\n")
    key = load_key() # loading existing key

    file = open(fileName, 'r') # opening (encrypted) text file
    fileContent = file.read().encode("utf-8") # saving the text to var

    fernet = Fernet(key)
    decrypted = fernet.decrypt(fileContent)

    # Writing decrypted file to output file
    if fileName.startswith("files/(e) "):
        fileName = fileName[len("files/(e) "):] # trimming output fileName

    outputFile = open("files/" + fileName, "w")
    outputFile.write(decrypted.decode("utf-8"))
    outputFile.close()

    os.system("clear")
    print("\nDone!\n")


