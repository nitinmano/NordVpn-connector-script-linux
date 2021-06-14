from os import system as s
print("Enter the options\n1.Nearest Server\n2.US\n3.UK\n4.Taiwan\n5.Select Other Countries\n6.Disconnect")
print("7.OtherCommands\n8.Exit")
src="nordvpn "
while(True):
    try:
        n=int(input())
        if(n==1):
            s(src+"c")
        elif(n==2):
            s(src+"c us")
        elif(n==3):
            s(src+"c uk")
        elif(n==4):
            s(src+"c taiwan")
        elif(n==5):
            s(src+"countries")
            print("Type the Country name:")
            s(src+"c "+input())
        elif(n==6):
            s(src+"d")
        elif(n==7):
            s(src+"h")
            print("nordvpn",end=" ")
            s(src+input())
        else:
            break
        break
    except:
        print("Try Again")