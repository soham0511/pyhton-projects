import string
import random
if __name__ == "__main__":

    s1=string.ascii_lowercase
    s2=string.ascii_uppercase
    s3=string.digits
    s4=string.punctuation

    len=int(input("Enter the length of password"))
    if len==str:
        print("Wrong Entry")
    else:
         len = int(len)
    s=[]

    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    # print(s)
    # first alternative
    # random.shuffle(s)
    # print("".join(s[0:len]))
    #second alternative
    print("".join(random.sample(s,len)))
    