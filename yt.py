# -*-coding:utf-8-*-
import os
import sys
from time import sleep
from os import system

#colors
r='\033[91m' #red
g='\033[92m' #green
y='\033[93m' #yellow
b='\033[94m' #blue
p='\033[95m' #magenta/purple
c='\033[96m' #cyan
w='\033[97m' #white

#download
def anime(x):
        for content in x+'\n':
                sys.stdout.write(content)
                sys.stdout.flush()
                sleep(0.05)

#clear
def cls():
	system('clear')
cls()

"""
#Requirements
down=y+'Checking Requirements.Please wait.......'
anime(down)
system('pkg install ffmpeg -y>/dev/null 2>&1')
system('pip install -U youtube-dl>/dev/null 2>&1')
system('pip install --upgrade pip youtube-dl>/dev/null 2>&1')
"""
cls()

#baner
def logo(p):
	for word in p+'\n':
		sys.stdout.write(word)
		sys.stdout.flush()
		sleep(0.003)
banner='''

\033[96m   __________    __  ________                                  
  / ____/ __ )   \ \/ /_  __/                                  
 / / __/ __  |____\  / / /                                     
/ /_/ / /_/ /_____/ / / /                                      
\____/_____/     /_/ /_/      __                __             
   / __ \____ _      ______  / /___  ____ _____/ /__  _____    
  / / / / __ \ | /| / / __ \/ / __ \/ __ `/ __  / _ \/ ___/    
 / /_/ / /_/ / |/ |/ / / / / / /_/ / /_/ / /_/ /  __/ /        
/_____/\____/|__/|__/_/ /_/_/\____/\__,_/\__,_/\___/_/         
                                                               

▀▄▀▄▀▄ [ ============================ ] ▄▀▄▀▄▀
Author  : Guti Baba
Channel	: https://youtube.com/channel/UCNgDON6Y_VhCdCk1fc7o2lA
Page    : https://www.facebook.com/Guti-Baba-115116477282480
Version : 1.0
Tool    : YouTube Downloader
▀▄▀▄▀▄ [ ============================ ] ▄▀▄▀▄▀


'''
logo(banner)
link=raw_input(r+'[+] '+y+'Paste Your Video Link: ')
path=' "/sdcard/YT-Downloads/%(title)s.%(ext)s" '
#path=raw_input(r+'[+] '+y+'Input Your Location: ')
note=r+'[+] If your Desired Quality can\'t be Found, Then a Compatible Quality will be Downloaded!'
down=c+'[+] '+p+'Download Starting.............'
done=g+'[✓] Content Downloaded Successfully!'
knock=p+'Knock! Knock! Check Your Internal YTD-Downloads Folder!'
inv=r+'[+] Invalid Choice!'
sleep(1)
cls()
print(banner)

#Option
op='''
\033[93mWhat do you Want to Downlaod?
[1] Video
[2] Audio

'''
logo(op)
inp1=input(g+"[✓] "+y+"Choose Option: ")
if inp1==1:
	list1='''
Video Formats:
[1] mp4		[4] webm
[2] flv		[5] mkv
[3] ogg		[6] avi

'''
	logo(list1)
	inp2=input(g+'[✓] '+y+'Choose Option: ')
	size='''
Resolution Quality:
[1] Best	[5] 480p
[2] 4k		[6] 360p
[3] 1080p	[7] 244p
[4] 720p	[8] 144p

'''
	if inp2==1:
		logo(size)
		inp3=input(g+'[✓] '+y+'Choose Quality: ')
		anime(note)
                anime(down)
		if inp3==1:
			system('youtube-dl -o "/sdcard/YT-Downloads/%(title)s[Best].%(ext)s" -f bestvideo+bestaudio --audio-format "mp3" '+link)
			anime(done)
			print knock
		elif inp3==2:
			system('youtube-dl -o "/sdcard/YT-Downloads/%(title)s[4k].%(ext)s" -f "(bestvideo[ext=mp4,height<=2160])+(bestaudio)" --audio-format "mp3" '+link)
			anime(done)
			print knock
		elif inp3==3:
			system('youtube-dl -o "/sdcard/YT-Downloads/%(title)s[1080p].%(ext)s" -f "(bestvideo[ext=mp4,height<=1080])+(bestaudio)" --audio-format "mp3" '+link)
			anime(done)
                        print knock
		elif inp3==4:
                        system('youtube-dl -o "/sdcard/YT-Downloads/%(title)s[720p].%(ext)s" -f "(bestvideo[ext=mp4,height<=720])+(bestaudio)" --audio-format "mp3" '+link)
			anime(done)
                        print knock
		elif inp3==5:
                       	system('youtube-dl -o "/sdcard/YT-Downloads/%(title)s[480p].%(ext)s" -f "(bestvideo[ext=mp4,height<=480])+(bestaudio)" --audio-format "mp3" '+link)
			anime(done)
                        print knock
		elif inp3==6:
        	        system('youtube-dl -o "/sdcard/YT-Downloads/%(title)s[360p].%(ext)s" -f "(bestvideo[ext=mp4,height<=360])+(bestaudio)" --audio-format "mp3" '+link)
			anime(done)
                        print knock
		elif inp3==7:
                       	system('youtube-dl -o "/sdcard/YT-Downloads/%(title)s[240p].%(ext)s" -f "(bestvideo[ext=mp4,height<=240])+(bestaudio)" --audio-format "mp3" '+link)
			anime(done)
                        print knock
		elif inp3==8:
			system('youtube-dl -o "/sdcard/YT-Downloads/%(title)s[144p].%(ext)s" -f "(bestvideo[ext=mp4,height<=144])+(bestaudio)" --audio-format "mp3" '+link)
			anime(done)
                        print knock
		else:
			anime(inv)
	elif inp2==2:
		anime(note)
		anime(down)
		system('youtube-dl -o'+path+'--audio-format "mp3" --recode-video flv '+link)
	elif inp2==3:
		anime(note)
		anime(down)
                system('youtube-dl -o'+path+'--audio-format "mp3" --recode-video ogg '+link)
	elif inp2==4:
		logo(size)
		inp3=input(g+'[✓] '+y+'Choose Quality: ')
		anime(note)
                anime(down)
		if inp3==1:
			system('youtube-dl -o "/sdcard/YT-Downloads/%(title)s[Best].%(ext)s" -f "(bestvideo[ext=webm])+(bestaudio)" --audio-format "mp3" '+link)
			anime(done)
                        print knock
		elif inp3==2:
			system('youtube-dl -o "/sdcard/YT-Downloads/%(title)s[4k].%(ext)s" -f "(bestvideo[ext=webm,height<=2160])+(bestaudio)" --audio-format "mp3" '+link)
			anime(done)
                        print knock
		elif inp3==3:
			system('youtube-dl -o "/sdcard/YT-Downloads/%(title)s[1080p].%(ext)s" -f "(bestvideo[ext=webm,height<=1080])+(bestaudio)" --audio-format "mp3" '+link)
			anime(done)
                        print knock
		elif inp3==4:
			system('youtube-dl -o "/sdcard/YT-Downloads/%(title)s[720p].%(ext)s" -f "(bestvideo[ext=webm,height<=720])+(bestaudio)" --audio-format "mp3" '+link)
			anime(done)
                        print knock
		elif inp3==5:
                       	system('youtube-dl -o "/sdcard/YT-Downloads/%(title)s[480p].%(ext)s" -f "(bestvideo[ext=webm,height<=480])+(bestaudio)" --audio-format "mp3" '+link)
			anime(done)
                        print knock
		elif inp3==6:
        	        system('youtube-dl -o "/sdcard/YT-Downloads/%(title)s[360p].%(ext)s" -f "(bestvideo[ext=webm,height<=360])+(bestaudio)" --audio-format "mp3" '+link)
			anime(done)
                        print knock
		elif inp3==7:
                       	system('youtube-dl -o "/sdcard/YT-Downloads/%(title)s[240p].%(ext)s" -f "(bestvideo[ext=webm,height<=240])+(bestaudio)" --audio-format "mp3" '+link)
			anime(done)
                        print knock
		elif inp3==8:
       	                system('youtube-dl -o "/sdcard/YT-Downloads/%(title)s[144p].%(ext)s" -f "(bestvideo[ext=webm,heightt<=144])+(bestaudio)" --audio-format "mp3" '+link)
			anime(done)
                        print knock
		else:
			anime(inv)
	elif inp2==5:
		anime(note)
		anime(down)
                system('youtube-dl -o'+path+'--audio-format "mp3" --recode-video mkv '+link)
	elif inp2==6:
		anime(note)
		anime(down)
                system('youtube-dl -o'+path+'--audio-format "mp3" --recode-video avi '+link)
	else:
		print r+'Invalid Input!'
	system('xdg-open https://youtube.com/channel/UCNgDON6Y_VhCdCk1fc7o2lA')

elif inp1==2:
	list2='''
Audio Formats:
[1] best	[5] m4a
[2] aac		[6] opus
[3] flac	[7] vorbis
[4] mp3		[8] wav

'''
	logo(list2)
        inp2=input(g+'[✓] '+y+'Choose Option: ')
	anime(note)
        anime(down)
	if inp2==1:
		system('youtube-dl -o'+path+'-x --audio-format "best" '+link)
		anime(done)
                print knock
	elif inp2==2:
                system('youtube-dl -o'+path+'-x --audio-format "aac" '+link)
                anime(done)
                print knock
	elif inp2==3:
                system('youtube-dl -o'+path+'-x --audio-format "flac" '+link)
                anime(done)
                print knock
	elif inp2==4:
                system('youtube-dl -o'+path+'-x --audio-format "mp3" '+link)
                anime(done)
                print knock
	elif inp2==5:
                system('youtube-dl -o'+path+'-x --audio-format "m4a" '+link)
                anime(done)
                print knock
	elif inp2==6:
                system('youtube-dl -o'+path+'-x --audio-format "opus" '+link)
                anime(done)
                print knock
	elif inp2==7:
                system('youtube-dl -o'+path+'-x --audio-format "vorbis" '+link)
                anime(done)
                print knock
	elif inp2==8:
                system('youtube-dl -o'+path+'-x --audio-format "wav" '+link)
                anime(done)
                print knock
	else:
		anime(inv)
	system('xdg-open https://youtube.com/channel/UCNgDON6Y_VhCdCk1fc7o2lA')

else:
	print r+'Invalid Input!'
