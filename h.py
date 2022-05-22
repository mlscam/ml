def isprime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3,int(num ** 0.5) + 2,2):
        if num % n == 0:
            return False
    return True

# p=7
# q=17
# a=6
# b=4
p = int(input("Enter initial Prime number for User1 "))
a = int(input("Enter private key for user1 "))

q = int(input("Enter prime number for User2 "))
b = int(input("Enter private key for User2 "))

R = pow(p,a) % q
S = pow(q,b) % p

print(R," ",S)

print(pow(R,a) % p , pow(S,b) % q)
if pow(R,a) % p == pow(S,b) % q:
    print("Keys are accepted")
else:
    print("Keys are not accepted")
