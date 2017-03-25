from helpers import rotate_character
    
def encrypt(text, rot):
    newString = ""
#    for char in text:
#        newString += rotate_character(char, rot)
#    return newString
    return newString.join(rotate_character(char, rot) for char in text)

def main():
    from sys import argv, exit
    
    if len(argv) != 2 or not argv[1].isdigit():
        print("usage: python3 caesar.py n")
        exit()

    msg = input("Type a message:")

    rot = int(argv[1])
    print(encrypt(msg, rot))

    
if __name__ == "__main__":
    main()