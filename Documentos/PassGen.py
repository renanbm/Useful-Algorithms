import random

def PasswordGen(size):
    allowed_lc_letters = "abcdefghijklmnopqrstuvwxyz"
    allowed_uc_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    allowed_numbers = "0123456789"
    allowed_symbols = "?/!@#$%()[]&*"

    allowed = allowed_lc_letters + allowed_uc_letters + allowed_numbers + allowed_symbols

    password = ""

    for i in range(size):
        password += allowed[random.randrange(len(allowed))]

    symbolcount = 0

    for letter in password:
        if letter in allowed_symbols:
            symbolcount += 1

    if symbolcount > size//10 * 4:
        return password
    else:
        return PasswordGen(size)


if __name__ == "__main__":
    print(PasswordGen(16))