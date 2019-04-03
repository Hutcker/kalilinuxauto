import os 

while True:
 print("[1]Установить линукс")
 print("[2]Выход")
 inp = int(input("[*]Выбор: "))
 if inp == 1:
  print("[*]Установка...")
  print("[*]VNC сервер будет запущен на : 127.0.0.1:5901")
  os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Kali/kali.sh && bash kali.sh")
  os.system("bash start-kali.sh")
  os.system("wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/DesktopEnvironment/Apt/Xfce4/de-apt-xfce4.sh && bash de-apt-xfce4.sh")
 elif inp == 2:
  print("[*]Досвидания!")
  break
 else:
  print("[*]Неизвестная команда")