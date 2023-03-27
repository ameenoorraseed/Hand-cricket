import random

def w_score(pn,score):
    with open('score.txt','a') as f:
        f.write(pn+'\t'+str(score)+'\n')
        
def r_score():
    with open('score.txt','r') as f:
        for i in f.readlines():
            print(i)
        
def play():
    score = 0
    pn = str(input("enter your name: "))
    while True:
        cpu_r = random.randint(1,6)
        while True:
            p_r = int(input('enter your run: '))
            if p_r >6 or p_r<0:
                print("invalid run, try again")
            else:
                break
        if p_r == cpu_r:
            print('cpu run is',cpu_r)
            print("\nyour out!!!\nyour score is:",score)
            w_score(pn,score)
            break
        else:
            print('cpu run is',cpu_r)
            score = score + p_r

while True:
    print('welcome to game')
    c = int(input('1.play\n2.highscore\nexit\nenter your choice: '))
    if c == 1:
        play()
    elif c==2:
        r_score()
    elif c==3:
        break
    
            
    

    
    
    
    
