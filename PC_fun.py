'''Modules of function needs to be imported'''
import webbrowser
import os
import sys
import subprocess

def zomato():
    webbrowser.open_new_tab('www.zomato.com')
def facebook():
    webbrowser.open_new_tab('www.facebook.com')
def psiterp():
    webbrowser.open_new_tab('https://erp.psit.in/')
def weather():
    webbrowser.open_new_tab('https://www.google.com/search?q=live+weather&oq=live+weather&aqs=chrome..69i57j0l5.7259j1j7&sourceid=chrome&ie=UTF-8')
def cricket():
    webbrowser.open_new_tab('www.cricbuzz.com')
def geeksforgeeks():
    webbrowser.open_new_tab('https://www.geeksforgeeks.org/')
def linkedin():
    webbrowser.open_new_tab('https://www.linkedin.com/home/?originalSubdomain=in')
def github():
    webbrowser.open_new_tab('https://github.com/')
def youtube():
    webbrowser.open_new_tab('www.youtube.com')
def shut():
    s=input("Do you really want to shut down[y/n]:")
    if s=='y':
        os.system("shutdown /s /t 1")
def restart():
    s=input("Do you really want to restart[y/n]:")
    if s=='y':
        os.system("shutdown /r /t 1")
def notepad():
    os.startfile("notepad.exe")
def dev():
    os.startfile('D:/Dev-Cpp/devcpp.exe')
def hackerrank():
    webbrowser.open_new_tab('www.hackerrank.com')
    
def news():
    webbrowser.open_new_tab('https://www.indiatoday.in/news.html')
def webcam():
    os.startfile("C:/Program Files (x86)/ManyCam/ManyCam.exe")
def vlc():
    os.startfile("C:/Program Files/VideoLAN/VLC/vlc.exe")
def power():
    os.startfile("C:/Users/KL/AppData/Local/Kingsoft/WPS Office/ksolauncher.exe")
def visual():
    os.startfile('C:/Users/KL/AppData/Local/Programs/Microsoft VS Code/Code.exe')
def codeforces():
    webbrowser.open_new_tab('https://codeforces.com/profile/_aadiupadhyay_')

di={'power':power,
    'news':news,
    'psit':psiterp,
    'facebook':facebook,
    'weather':weather,
    'cricket':cricket,
    'food':zomato,
    'geeksforgeeks':geeksforgeeks,
    'linkedin':linkedin,
    'github':github,
    'youtube':youtube,
    'shut':shut,
    'restart':restart,
    'notepad':notepad,
    'dev':dev,
    'webcam':webcam,
    'vlc':vlc,
    'hackerrank':hackerrank,
    'visual':visual,
    'codeforces':codeforces
    }
