from os import system as s
print("Enter the options\n1.Nearest Server\n2.US\n3.UK\n4.Taiwan\n5.Select Others\n6.Disconnect")
print("7.OtherCommands")
while(True):
    try:
        n=int(input())
        src="nordvpn"
        if(n==1):
            s(src,"c")
        elif(n==2):
            s(src,"c us")
        elif(n==3):
            s(src,"c uk")
        elif(n==4):
            s(src,"c taiwan")
        elif(n==5):
            s(src)
            s(src,input())
        elif(n==6):
            s(src,"d")
        elif(n==7):
            s(src,"h")
            s(src,input())
        exit(0)
    except:
        pass

