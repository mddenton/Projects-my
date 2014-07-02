#Global constants for menu choices

SHIFT_ONE = 1
SHIFT_TWO = 2
def caesar(plaintext, shift):
    alphabet=["a","b","c","d","e","f","g","h","i","j","k","l",
    "m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B",
    "C","D""E","F","G","H","I","J","K","L","M","N","O","P",
    "Q","R","S","T","U","V","W","X","Y","Z"]

    #Create our substitution dictionary
    dic={}
    for i in range(0,len(alphabet)):
        dic[alphabet[i]]=alphabet[(i+shift)%len(alphabet)]

    #Convert each letter of plaintext to the corresponding
    #encrypted letter in our dictionary creating the cryptext
    caesartext=""
    for l in plaintext:
        if plaintext.isupper():
            uppercase = True
        else:
            uppercase = False
        for l in plaintext:
            if uppercase:
                l = l.upper()
                l=dic[l]
            elif l in dic:
                l=dic[l]
            caesartext+=l

        return caesartext

#Get choice


def main():
    user = 0
    user = get_menu_choice ()
    if user == SHIFT_ONE:
        plaintext=input("Enter your text to be coded: ")
        print ("Plaintext:", plaintext )
        print ("Caesartext:",caesar(plaintext,1))
    elif user ==SHIFT_TWO:
        plaintext=input("Enter your text to be coded: ")
        print ("Plaintext:", plaintext )
        print ("Caesartext:",caesar(plaintext,2))

def get_menu_choice():
    user=int(input("For one positive shift, enter 1; for two positive shifts enter 2: "))
    return user

#"Now is the time for all good men to come to the aid of their country"
#"The quick brown fox jumps over the lazy dog"

main()
