import string
import secrets
alphabet = string.ascii_letters + string.digits + string.punctuation
password = ''.join(secrets.choice(alphabet)for i in range (16))
print("Your randomly generated password is: " + password)
