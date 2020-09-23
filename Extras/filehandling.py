import os
import re

fh=open(r'C:\hello.txt','a')

a='y'
while(a=='y'):
    print('Main menu')
    print(' 1.Add \n 2.Show \n 3.Delete \n 4.Search \n 5.Update')
    num=int(input('\n\t Enter the section ='))
    print('\n')

    if(num==1):

        b='y'
        while(b=='y'):

            rollno=int(input('\n\t Student Rollno ='))
            name=input('\n\t Student Name =')
            add=input('\n\t Student Address =')
            cont=input('\n Do you want save(y/n) ')

            if(cont=='y'):
                
                fh=open(r'C:\hello.txt','a')
                fh.write(str(rollno)+':'+name+':'+add+'.\n')
                fh.close()


            else:
                fh.close()

            b=input('\n Do you want add more data(y/n) ')

        fh=open(r'C:\hello.txt','r')
        data=fh.readlines()

        numb=re.findall(r'\d{1,3}',str(data))

        f=open(r'C:\temp.txt','w')

        n = len(numb)
        for i in range(n):
            for j in range(0, n-i-1):
                    if numb[j] > numb[j+1]:
                        data[j],data[j+1] = data[j+1], data[j]
                        numb[j], numb[j+1] = numb[j+1], numb[j]
                            

        for i in range(len(numb)):
            f.write(data[i])

        f.close()
        fh.close()
        os.remove(r'C:\hello.txt')
        os.rename(r'C:\temp.txt',
                  r'C:\hello.txt')

        
    elif(num==2):

            fh=open(r'C:\hello.txt','r')
            data=fh.readlines()
            
            for line in data:
                line=line.replace(':','\t')
                line=line.replace('.','\t')
                print(line)


    elif(num==3):

        fh=open(r'C:\hello.txt','r')
        rollno=input('\n\t Enter the rollno you want to delete the data=')
        data=fh.readlines()

        numb=re.findall(r'\d{1,3}',str(data))
        
        f=open(r'C:\temp.txt','w')
        m=0
        for n in numb:
            if(rollno==n):
                m+=1
                
            else:
                  
                l=data[m]
                line=l.replace(':','\t')

                print('\n\t',line)
                f.write(data[m])
                m+=1

                
        f.close()
        fh.close()
        os.remove(r'C:\hello.txt')
        os.rename(r'C:\temp.txt',
                  r'C:\hello.txt')

            
    elif(num==4):

        fh=open(r'C:\hello.txt','r')
        rollno=input('\n\t Enter the rollno you want to search=')
        data=fh.readlines()

        numb=re.findall(r'\d{1,3}',str(data))
        k=numb.sort()
        print(k)

        
        m=0
        for n in numb:
            if(rollno==n):
                
                l=data[m]
                line=l.replace(':','\t')
                print('\n\t',line)
                m+=1
            else:
                m+=1

        fh.close()

                
    elif(num==5):
        
        fh=open(r'C:\hello.txt','r')
        rollno=input('\n\t Enter the rollno you want update =')
        data=fh.readlines()

        numb=re.findall(r'\d{1,3}',str(data))

        f=open(r'C:\temp.txt','w') 
        m=0
        
        for n in numb:
            if(rollno==n):
                
                rollno=input('\n\t Student Rollno =')
                name=input('\n\t Student Name =')
                add=input('\n\t Student Address =')
               
                f.write(rollno+':'+name+':'+add+'.\n')
                m+=1
                
            else:
                f.write(data[m]) 
                m+=1

        f.close()
        fh.close()
        os.remove(r'C:\hello.txt')
        os.rename(r'C:\temp.txt',
                  r'C:\hello.txt')


    a=input('\n Do you want to continue the program(y/n) ')
    print('\n=============================================')