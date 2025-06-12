import hashlib

password_file = "Ashley_Madison.txt"

password = "elizabeth"

encode_pass = password.encode("utf-8")

password_hash = hashlib.sha1(encode_pass.strip()).hexdigest()
# print(password_hash)
pass_file = open(password_file, "r")

for word in pass_file:
    enc_word = word.encode("utf-8")
    enc_hash = hashlib.sha1(enc_word.strip()).hexdigest()

    if enc_hash == password_hash:
        print("we get it, the password is: " + word)
        quit()

print("strong Password bruh")