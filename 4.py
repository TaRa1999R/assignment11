                       # RUG

print (" RUG ")
print (" If your entered number is ODD , a rug will be printed ")

def rug ( size ) :
    Emoji_list = []
    Rug_line = []
    Rug = []
    varity = 1

    number_of_emojis = ( int ( size / 2 )) + 1
    for i in range ( number_of_emojis ) :
        emoji = input (" Please enter an emoji : ")
        Emoji_list.append ( emoji )
    







while True :
    size = int ( input (" Please enter a number : "))

    if size % 2 == 0 :
        print (" your entered number is even ❌❌ ")
        print (" to see a rug please enter an odd number ")

    elif size % 2 != 0 :
        print (" your entered number is odd ✔✔ ")
        print (" here is the rug 🙂 ")
        rug ( size )
        break