k,j=0,0
email=input("enter your email: ")
if len(email) >=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1): # check point 1
            if (email[-4]==".") ^ (email[-3]=="."):  # check point 2
                for i in email:
                    if i .isspace():   # check point 3
                        k=1
                    elif i.isalpha():   # check point 4
                        if i==i.upper():
                            j=1 
                    elif i.isdigit():   # check point 5
                        continue     
                    elif i== "_" or i=="." or i=="@":  # check point 6
                        continue
                    else:
                        print("email must contain only letters,digits,underscores,@ etc")   
                if k==1:
                    print(" email must not contain spaces")
                if j==1:
                    print("email must not contain uppercase letters")

                else:
                    print("email is valid")

            else:
                print("email must end with .com or .in")
        else:
            print("email must contain exactly one @ symbol")  
    else:
        print("email must start with a letter")

else:
    print("email must be 6  characters long")
