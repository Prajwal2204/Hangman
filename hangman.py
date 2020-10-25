import random
from threading import Thread
from bs4 import BeautifulSoup
import urllib.request
import requests
from time import sleep
import sys

def countdown(a):

    len_arr = [] 
    words=['moon','goat','malayalam','tomato','pumpkin']
    for i in words:
        len_arr.append(len(i))
    #print(len(len_arr))
    word_len = len(a)
    if word_len > 0 and word_len <= 5:
        t = 60    # 60 secs for a word of length between 0 and 5 
    elif word_len > 5 and word_len <= 10:
        t = 120     # 120 secs for a word of length between 5 and 10 
    else:
        t = 300     # 300 secs for a word of length more than 10
    # YOU CAN CHECK WITH LESSER TIME LIMIT AS WELL FOR SIMPLICITY

    print('You have ' + str(t) + ' seconds')

    for i in range(t):
        sleep(1)   
    
    print('Time up!!')
    print('Your word was '+a)
    sys.exit()    


def hangman(tally):

    words=['moon','goat','malayalam','tomato','pumpkin']
    x=random.randint(0,len(words)-1)
    a=random.choice(words)
    #a=a.decode('utf-8')
    a=a.lower()
    b=str()
    print('Your word is: ', end= ' ')
    for i in range (0, len(a)):
        b= b+'_'
        print(b[i] ,end= ' ')
    print('\n')
    guess=[]
    count=tally[0]
    points=tally[1]
    
    t1 = Thread(target=countdown, args=(a,))
    t1.start()

    while(count>0):
        print('\n\nYou have ' +str(count)+' chances to guess the word')
        x=input("Enter an alphabet: ")[0]
        if(x.isalpha()==False):
            print("Enter a valid alphabet")
            break
        x= x.lower()
        buffer=0
        buffer1=0
        for i in range (0,len(a)):
            if(a[i]==x):
                buffer=1
                b=list(b)
                b[i]=x
                b="".join(b)
                points=points+1
        if(buffer==1):
            for j in range (0, len(b)):
                print(b[j] ,end= ' ')
        if(buffer==0):
            for i in range (0,len(guess)):
                if(guess[i]==x):
                    buffer1=1
            if(buffer1==0):
                count=count-1
                guess.append(x)
        buf=0
        for i in range(0, len(b)):
            if(b[i]=='_'):
                buf=1
        if(buf==0):
            print('\nYou have guessed the word with ' + str(count) +' chances left \n'+ str(points)+' points\n\n')
            tally[0]=count
            tally[1]=points
            return tally
    if(count==0):
        print('You lost. Better luck next time! \n Your word was: '+a+'\nYour points are: '+str(points))
        tally[0]=0
        tally[1]=points
        return tally

 

print('HANGMAN')
tally=[7,0]
print(type(tally[0]))

while(1):
    x=input('Press:\n 1.To play a new game \n 2. Continue existing game \n 3. Exit\n')
    x=int(x)
    if(x==1):
        tally=[7,0]
        tally= hangman(tally)
    if(x==2):
        if(tally[0]==0):
            tally[0]=7
            tally[1]=0
        tally=hangman(tally)
        
    if(x==3):
        exit()
    else:
        print("Enter a valid response ")
