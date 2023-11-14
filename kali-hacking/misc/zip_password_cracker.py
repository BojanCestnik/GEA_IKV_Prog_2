import zipfile

encrypted_filename= "secret_file.zip"
zFile = zipfile.ZipFile(encrypted_filename, "r")

passFile = open("stored_passwords.txt", "r") # read file with stored passwords

for line in passFile.readlines():
    test_password = line.strip("\n").encode('utf-8') # preprocess the input line
    try:
        print(test_password.decode("utf-8"))
        zFile.extractall(pwd=test_password)
        print("Matching password found:", test_password.decode("utf-8"))
        break
    except Exception as err:
        pass
