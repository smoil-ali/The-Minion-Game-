def minion_game(string):
    length=len(string)
    vow=["A","I","O","U","E"]
    Stuart=0
    Kevin=0
    char=string[0]
    value=string.count(char)
    if value==length:
        if char in vow:
            ans=int(length*(length+1)/2)
            print("Kevin",ans)
        else:
            ans=int(length*(length+1)/2)
            print("Stuart",ans)
    else:
        Kevin=0
        Stuart=0
        for x in range(len(string)):
            if string[x] in vow:
                Kevin+=length
                length-=1
            else:
                Stuart+=length
                length-=1
        if Stuart>Kevin:
            print("Stuart",Stuart)
        elif Kevin>Stuart:
            print("Kevin",Kevin)
        else:
            print("Draw")



if __name__ == '__main__':
    s = input()
    minion_game(s)