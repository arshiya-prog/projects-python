import logo
print(logo.logo)

def take_msg():
    message = input("Type your message: ").lower()
    return message

def encode(msg):
    shift_no = int(input("Type the shift number: "))
    encoded_msg = ""

    for m in msg:
        if m.isalpha():
            shifted = ord(m) - 97 + shift_no
            new = chr((shifted % 26) + 97)
            encoded_msg += new
        else:
            encoded_msg += m

    print(encoded_msg)
    
def decode(msg):
    shift_no = int(input("Type the shift number: "))
    decoded_msg = ""
    
    for m in msg:
        if m.isalpha(): # checks whether the char is an alphabet or not
            shifted = ord(m) - 97 - shift_no # if m=a and shift_no=5; shifted=97-97-5 = -5
            new = chr((shifted % 26) + 97) # new=(-5%26)+97 = 21+97 = 118 --> new=chr(118) = v
            decoded_msg += new
        else:
            decoded_msg += m

    print(decoded_msg)

action = input("Type 'encode' to encrypt or 'decode' to decrypt: ")

if action == "encode":
    msg = take_msg()
    encode(msg)
elif action == "decode":
    msg = take_msg()
    decode(msg)