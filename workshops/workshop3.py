print("-----------------currency-----------------")
import random

MAX_INCREASE = 0.1	# 10%
MAX_DECREASE = 0.05	# 5%
MIN_PRICE = 0.01
MAX_PRICE = 1000.0
INITIAL_PRICE = 10.0
count=0
price = INITIAL_PRICE
print("starting price ${:,.2f}".format(price))

while price >= MIN_PRICE and price <= MAX_PRICE:
    priceChange = 0
    count=count+1

# generate a random integer of 1 or 2
# if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
# generate a random floating-­‐point number
# between 0 and MAX_INCREASE
        priceChange = random.uniform(0, MAX_INCREASE)
    else:
# generate a random floating-­‐point number
# between negative MAX_INCREASE and 0
        priceChange = random.uniform(---MAX_DECREASE, 0)

    price *= (1 + priceChange)
    print("on day {} prise is ${:,.2f}".format(count,price))

print("******************************************* exception ****************************************************")

finished = False
result = 0
while finished == False:
    try:
        result = int(input("Enter an integer: "))
        finished = True
    except ValueError:
        print("Invalid vlaue")
print("Valid result is: ", result)

print("********************************************* password **************************************************")

import string
def validate(password):
    length = False
    uppercase = False
    lowercase = False
    num = False
    spec = False

    if len(password) >= 5 and len(password) <= 15:
        length = True
    for i in string.ascii_uppercase:
        if i in password:
            uppercase = True
            break
    for i in string.ascii_lowercase:
        if i in password:
            lowercase = True
            break
    for i in string.digits:
        if i in password:
            num = True
            break
    for i in string.punctuation:
        if i in password:
            spec = True
            break
    if not length:
        print("Password showld be between 5 and 15 characters long")
    if not uppercase:
        print("The password should contain atleast 1 uppercase letter")
    if not lowercase:
        print("The password should contain atleast 1 lowercase letter")
    if not num:
        print("The password should contain atleast 1 number")
    if not spec:
        print("The password should contain atleast 1 special character")
    if length and uppercase and lowercase and num and spec:
        return True
    else:
        return False


def main():
    while True:
        password = str(input("Enter password: "))
        valid = validate(password)
        if valid:
            print("Your password")
            break

main()

print("***************************************************************************************************")

