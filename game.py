import numpy as np
import matplotlib.pyplot as plt

#L= int(input('L'))
L=30
#N= int(input('N'))
N=700
#T= int(input('T'))
T=100
counter=0
p=0
base=np.zeros((L,L))
base4=np.zeros((L,L))
base2=0
base3=np.zeros(T+1)
size = (L, L)
test=0
randmake =np.random.randint(L, size=(2, N))
for i in range (N):#random maker
    base[randmake[0][i]][randmake[1][i]]=1
  #  if base[randmake[0][i]][randmake[1][i]]==0:
   #     base[randmake[0][i]][randmake[1][i]]=1
    #else:
     #   randmake[0][i]=np.random.randint(L)
      #  randmake[1][i]=np.random.randint(L)
       # i=i-1
    
for x in range (L):
       for y in range (L):
           if base[x][y]==1:
               test=test+1
print(test)
base3[0]=test
for H in range (T):
 #####################################################################random walk    
   for x in range (1,L-1):#base base 
        for y in range (1,L-1):
            
                
                p=base[x][y]
                if base[x-1][y]==1 :
                    counter=counter+1
                if base[x+1][y]==1 :
                    counter=counter+1
                if base[x][y-1]==1 :
                    counter=counter+1
                if base[x][y+1]==1 :
                    counter=counter+1
                
                if counter ==3:
                    base4[x][y]= 1
                elif counter==2:
                    base4[x][y] =p
                elif counter>3 or counter<2 :
                     base4[x][y]= 0
                counter=0
   for y in range (1,L-1):#base up 
            p = base[0][y] 
            counter=0
            if base[1][y]==1 :
                counter=counter+1
            if base[0][y-1]==1:
                counter=counter+1
            if base[0][y+1]==1 :
                counter=counter+1
            if counter ==3:
                    base4[0][y]= 1
            elif counter==2:
                    base4[0][y] =p
            elif counter>3 or counter<2 :
                     base4[0][y]= 0
            counter=0
   for y in range (1,L-1):#base down 
            counter=0
            p=base[L-1][y]
                
                
            if base[L-2][y]==1:
                counter=counter+1
            if base[L-1][y-1]==1:
                counter=counter+1
            if base[L-1][y+1]==1 :
                counter=counter+1
            if counter ==3 :
                    base4[L-1][y]= 1
            elif counter==2:
                    base4[L-1][y] =p
            elif counter>3 or counter<2 :
                     base4[L-1][y]= 0
            counter=0
   for x in range (1,L-1):#base left 
            p= base[x][0]
            counter=0    
            
            if base[x][1]==1 :
                counter=counter+1
            if base[x-1][0]==1:
                counter=counter+1
            if base[x+1][0]==1 :
                counter=counter+1
            if counter ==3 :
                    base4[x][0]= 1
            elif counter==2:
                    base4[x][0] =p
            elif counter>3 or counter<2  :
                 base4[x][0]= 0
            counter=0
   for x in range (1,L-1):#base right 
            p=base[x][L-1]
            counter=0    
        
            if base[x][L-1]==1:
                counter=counter+1
            if base[x-1][L-1]==1 :
                counter=counter+1
            if base[x+1][L-1]==1 :
                counter=counter+1
            if counter ==3:
                    base4[x][L-1]= 1
            elif counter==2:
                    base4[x][L-1] =p
            elif counter>3 or counter<2 :
                     base4[x][L-1]= 0
            counter=0
            
   p= base[0][0]#corner LU
   counter=0
   if base[0][1]==1:
        counter=counter+1
   if base[1][0]==1 :
                counter=counter+1
                
   if counter==2:
                    base4[0][0] =p
   elif counter>3 or counter<2 :
                     base4[0][0]= 0
   counter=0
    
   p=base[L-1][0] #corner LD
   counter=0
   if base[L-2][0]==1  :
                counter=counter+1
   if base[L-1][1]==1 :
        counter=counter+1
   if counter==2:
                    base4[L-1][0] =p
   elif counter>3 or counter<2 :
                     base4[L-1][0]= 0
   counter=0
   
   p=base[0][L-1]#cornr RU
   counter=0
   if base[0][L-2]==1 :
        counter=counter+1
   if base[1][L-1]==1 :
        counter=counter+1
   if counter==2:
                    base4[0][L-1] =p
   elif counter>3 or counter<2 :
                     base4[0][L-1]= 0
   counter=0
   
   p= base[L-1][L-1] #corner RD
   if base[L-1][L-1]==1:
        counter=counter+1
   if base[L-1][L-2]==1 :
        counter=counter+1
   if counter==2:
                    base4[L-1][L-1] =p
   elif counter>3 or counter<2 :
                     base4[L-1][L-1]= 0
   counter=0
   for x in range (L):
       for y in range (L):
           if base[x][y]==1:
               base2=base2+1
   base3[H+1]=base2
   print(base2)
   base2=counter=0
   base=base4
   base4=np.zeros((L,L))
   x,y = np.argwhere(base == 1).T

   plt.scatter(x,y)
   plt.show()
plt.plot(base3)
plt.show()  
 
