import random

def w_score(pn,score):
    with open('score.txt','a') as f:
        f.write(pn+'\t'+str(score)+'\n')
        
def r_score():
    try:
        with open('score.txt','r') as f:
            for i in f.readlines():
                print(i)

    except:
        print('\n','*'*5+' '+'no scores to display'+' '+'*'*5,'\n')

def instruction():
    #print('='*70)
    print('\n\n\n'+'='*70+"\n\t\t\tABOUT GAME\n"+'='*70+"\n\nMODE\n\tIt is a single player game(a player vs a computer)\n\nGAME\n\tFirst the computer makes a move and then player can choose a number between 1 - 6.\n\tWhen a player and computer gives a same number then the player is out Each time player gives another number then the score is added ip.\n\nSCORE\n\tThe score is saved in scores.txt and it will be automatically updated each time the game is played.")
    print('\n'*5)

    
    
def play():
    score = 0
    pn = str(input("enter your name: "))
        
    print('welcome',pn)
    print('\n'*5)
    
    while True:
        cpu_r = random.randint(1,6)
        while True:
            p_r = int(input('enter your run: '))
            if p_r >6 or p_r<0:
                print("invalid run, try again")
            else:
                break
        if p_r == cpu_r:
            import os
            clear = lambda: os.system('cls')
            clear()
            print('cpu run is',cpu_r)
            print("\nyour out!!!\nyour score is:",score)
            w_score(pn,score)
            break
        else:
            print('cpu run is',cpu_r)
            score = score + p_r

while True:
    
    print('\t'*3,'''\n\n\n\n\t██╗  ██╗ █████╗ ███╗   ██╗██████╗      ██████╗██████╗ ██╗ ██████╗██╗  ██╗███████╗████████╗
\t██║  ██║██╔══██╗████╗  ██║██╔══██╗    ██╔════╝██╔══██╗██║██╔════╝██║ ██╔╝██╔════╝╚══██╔══╝
\t███████║███████║██╔██╗ ██║██║  ██║    ██║     ██████╔╝██║██║     █████╔╝ █████╗     ██║   
\t██╔══██║██╔══██║██║╚██╗██║██║  ██║    ██║     ██╔══██╗██║██║     ██╔═██╗ ██╔══╝     ██║   
\t██║  ██║██║  ██║██║ ╚████║██████╔╝    ╚██████╗██║  ██║██║╚██████╗██║  ██╗███████╗   ██║   
\t╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝      ╚═════╝╚═╝  ╚═╝╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝   ╚═╝   
                                                                                         ''')    #print('='*20)
    c = int(input('1.play\n2.score\n3.how to play\n4.exit\n\nenter your choice: '))
    if c == 1:
        play()
    elif c==2:
        r_score()
    elif c==3:
        instruction()
    elif c==4:
        break
    else:
        print('*'*5+"invalid choice!!!"+'*'*5)
    
            
    

    
    
    
    
