           # RUG         EMOJI PISHNAHADI(🥰🤢🥶👾🤬 / 🖤🤎💜💙💚💛🧡❤🤍/⚫🟤🟣🔵🟢🟡🟠🔴⚪/⬛🟫🟪🟦🟩🟨🟧🟥⬜ )

print (" RUG ")
print (" If your entered number is ODD , a rug will be printed ")

def rug ( size ) :
    Emoji_list = []
    Rug = []

    number_of_emojis = ( int ( size / 2 )) + 1                                #daryaftemoji b tedad morede niaz 
    for i in range ( number_of_emojis ) :
        emoji = input (" Please enter an emoji : ")
        Emoji_list.append ( emoji )
    
    for row in range ( size ) :
        Rug_line = []
        for column in range ( size ) :
            Rug_line.append ("_")
        Rug.append ( Rug_line )

    center = int ( ( size - 1 ) / 2 )
    Rug [ center ][ center ] = Emoji_list [ 0 ]                               #markaz qali

    for n in range ( 1 , center + 1 ) :                                       #sakht qali
        for i in range ( -n , n + 1 ) :
            for j in range ( -n , n + 1 ) :
                if Rug [ center + i ][ center + j ] == "_" :
                    Rug [ center + i ][ center + j ] = Emoji_list [ n ]


    for row in Rug :                                                          #chap qali
        for column in row :
            print ( column , end = " ")
        print ("")
    







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