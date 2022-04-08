from urllib.request import urlopen #URLLIB
from bs4 import BeautifulSoup #BEAUTIFULSOUP 4
from threading import Thread
from time import sleep
from os import system

def connection(): #BUSCA O VALOR DENTRO DO SITE PARA VERIFICAÇÃO
    while True:
        try:
            powerURL = "https://emthd2f5eg.blogspot.com/2022/01/power.html" #LINK DO POST BLOGGER PARA VERIFICAÇÃO
            page = urlopen(powerURL)
            soup = BeautifulSoup(page, "html.parser")
            global info
            info = soup.find("div", {"class": "post-body entry-content float-container"}).getText()
            info.replace("\n", "")
            info.strip()
            global lun
            lun = len(info)
            sleep(10)
        except:
            pass

def verify():
    sleep(2)
    on = 4
    off = 3
    while True:
        sleep(10)
        if(lun == on):
            print("Your PC is Online") # SE = 11 // PC PODE FICAR ONLINE // ESTA ONLINE.
        elif(lun == off):
            print("Your PC is Offline")# SE = 1 // PC VAI DESLIGAR // ESTA DESLIGADO.
            system("shutdown /s /t60")
            break
        else:
            print("Operação nao identificada.") # SE ! 11 / 1 // Sem Operacao

def main():
        t1 = Thread(target=verify).start()
        t2 = Thread(target=connection).start()
main()

#By Julio Melo @juliomelo259
