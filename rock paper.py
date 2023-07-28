import random
l=['rock','scissor','paper']

'''
rock vs paper-> paper wins

rock vs scissor-> rock wins

paper vs scissor-> scissor wins.
'''


while True:
    ccount=0
    ucount=0
    uc=int(input('''
Game Start...
1 Yes
2 No | exit    
    '''))

    if uc==1:
        for a in range(1,6):
            userInput=int(input('''
1 rock
2 scissor
3 paper            
 '''))
            if userInput==1:
                uchoise= 'rock'
            elif userInput==2:
                uchoise= 'scssior'
            elif userInput==3:
                uchoise= 'paper'

            Cchoise=random.choice(l)
            if Cchoise==uchoise:
               print('computer value', Cchoise)
               print('user value',uchoise)
               print('drew')
               ucount=ucount+1
               ccount=ccount+1
            elif (uchoise=='rock' and Cchoise=='scissor') or (uchoise=='paper' and Cchoise=='rock') or (uchoise=='scissor' and Cchoise=='paper'):
                print('computer value', Cchoise)
                print('user value', uchoise)
                print('you win lfg')
                ucount=ucount+1
            else:
                print('computer value', Cchoise)
                print('user value', uchoise)
                print('computer won')
                ccount=ccount+1

        if ucount==ccount:
            print('final game draw..')
            print('user score',ucount)
            print('computer score',ccount)
        elif ucount>ccount:
            print('final you win lfg..')
            print('user score', ucount)
            print('computer score', ccount)
        else:
            print('final computer win..')
            print('user score', ucount)
            print('computer score', ccount)
    else:
        break




