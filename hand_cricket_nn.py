import random
from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure.modules import LSTMLayer
from pybrain.supervised import RPropMinusTrainer
from pybrain.datasets import SequentialDataSet
import random
from itertools import cycle

data=[]
for i in range(100):
    data.append(random.randrange(6)+1)
ds=SequentialDataSet(1,1)
net = buildNetwork(1, 300, 1, hiddenclass=LSTMLayer, outputbias=False, recurrent=True)
trainer = RPropMinusTrainer(net, dataset=ds)
for sample, next_sample in zip(data, cycle(data[1:])):
    ds.addSample( sample ,next_sample)
def predict():
    ds.addSample(cycle(data[len(data)-2:len(data)-1]).next(),data[len(data)-1])
    trainer.trainEpochs(50)
    return net.activate(data[len(data)-1])

def bowl(score=1,f=1):
    comp_runs=1
    usr_inp=score_count=0
    print " computer is batting "
    while True :
       
        try:
            comp_runs=random.randrange(6)+1
            print "ball : "
            usr_inp=int(raw_input())
            
        except:
            print "please enter a number !!!"
            continue
        
        print "batt :", comp_runs
        if usr_inp>6 :
            print "im warning you no numbers greater than 6 *_* "
            continue
        if comp_runs!=usr_inp :
            score_count=score_count+comp_runs
        else :
	    break
        if f==0:
                score=score-comp_runs
                print "runs needed :",score
                if score <=0 : 
                    break
        show(score_count)
    print "computer score is" , score_count
    return score_count

def bat(score=1,f=1):
    comp_ball=1
    usr_inp=score_count=0
    print " you are batting"
    while True : 
                 
            #comp_ball=random.randrange(6)+1
            comp_ball=int(predict())
            print "batt : "
            try: 
                usr_inp=int(raw_input())
                data.append(usr_inp)
            except:
                print "please enter a number !!!"
                continue
            print "ball :" ,comp_ball
               
            if usr_inp>6 :
                print "im warning you no numbers greater than 6 *_* "
                continue
            if comp_ball!=usr_inp:
                score_count=usr_inp+score_count
            else :
 		break
	    if f==0:
                score=score-usr_inp
                print "runs needed :",score
                if score<=0 : 
                        break
            show(score_count)
    print "your score is :",score_count 
    return score_count

def batball(ch):
    c=c1=0
    if ch==1 :
        c=bat()
                
        if c<bowl(c,0) :
               print "print you lose 0~0 "
        else :  
               print "you win (^V^) "          
    else:
        c1=bowl() 
        if c1>bat(c1,0) :
              print "print you lose 0~0 "  
        else :
              print "you win (^V^) "

def show(z) :
	   a=a1=0
           if z>=50 and z<=56 and a==0 :
                  print \
            """
                    55555     000                                                     
                    55       0   0                                            
                    55555    0   0    half century  ^0^ .                                       
                       55    0   0                                             
                    55555     000                                   
                                                                    
            """
		  a=1
           if z>=100 and a1==0 :
                   print \
            """
               11   000      000                                                     
               11  0   0    0   0                                            
               11  0   0    0   0     century  ^0^ .                                       
               11  0   0    0   0                                             
               11   000      000                                   
                                                                    
            """	   
		   a1=1


print \
"""    \n
                                          /_ /
    .....                              __/_ /_
   .  || .     /\    |\  |  |**       / \ /  /
  .   ||  .   /__\   | \ |  |  @     /      /
   .  || .   /    \  |  \|  |@@     /      /
    .....                          /      /
                                  /      /
                                  
"""
print \
      """\n\n
                WELCOME TO BALL AND BAT

ball and bat is a fun guess game . the objective is to beat the computer and to take
a higher total score

rules :
->a toss will decide who goes first to bat or bowl.
->wheter batting or bolling you highest possible choise is always 6.
->have fun ^o^ """

while True:
        print "TOSS : enter the your choice (H for heads and any other key for tails)"

        d=raw_input()
        if d=="H" or d=="h" :
                      print "\nyou chose heads"
                      f1=1
        else :
            print "\nyou chose tails"
            f1=2
        e=random.randrange(2)+1
        try:
            if f1==e :
                print "you won the toss chose to 1.bat or 2.bowl (1/2) "
                ch=int(raw_input())
                batball(ch)
            else :
                    v=random.randrange(2)+1     
                    print "you lose the toss"
                    batball(v)
        except: continue  
        print "\n\n....play again...(Y/N)\n\n"
        c=raw_input()
        if c=="y" or c=="Y": continue
        else : break
