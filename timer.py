from os import name, system
from pyfiglet import Figlet , figlet_format
from colorama import Fore, Style
from time import sleep
import winsound

def style():
    figlet = Figlet(font='big')
    system('cls' if name=="nt" else "clear")
    
    print(Fore.BLUE + figlet_format("Timer", font = "avatar") )
    sleep(0.5)
    print(Fore.CYAN + "# " + Fore.RED + "enter 1 to start" + Fore.GREEN + " :", )
    sleep(0.5)
    print(Fore.CYAN + "# " + Fore.RED + "enter 0 to exit" + Fore.GREEN + " : " , )
    sleep(1)
    
def select():
    try:
        return input(Fore.BLUE + "[1] " + Fore.YELLOW + "please enter your time " + Fore.BLUE + ">>" + Fore.YELLOW + "(hh:mm:ss)" + Fore.BLUE + " >>")
        system('cls' if name=="nt" else "clear")
    except:
        return -1
def wrong():
    print(Fore.RED + "[!]" + Fore.GREEN + "invalid sytax. please look at guidance")
    
    

    
def countdown(data):
    figlet = Figlet(font='big')
    t = 0
    time = data.split(":")
    hour = int(time[0])
    min = int(time[1])
    second = int(time[2])
    
    t = hour*3600 + min*60 + second
    

    try:
    
        while t > 0:
            system('cls' if name=="'nt'" else "clear")
            hour = t // 3600 
            min = (t-(hour*3600))//60
            second = t-(hour*3600)-(min*60)
            text = "{:02d}:{:02d}:{:02d}".format(hour,min,second)
            if hour == 0 and min == 0 and second <= 10:
                print(Fore.RED + Style.BRIGHT, figlet.renderText(text))
                hz = 440
                winsound.Beep(hz,500)
                
                sleep(1)
            else:
                print(Fore.CYAN + figlet.renderText(text))
                sleep(1)
            
            t -= 1
    except:
        wrong()
        style()
    print(figlet_format("tamam!!", font='avatar'))
    winsound.Beep(1000,670)
    
def main():
    style()
    countdown(select())
    
    
main()
