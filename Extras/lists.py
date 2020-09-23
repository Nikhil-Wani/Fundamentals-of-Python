a='y'
while(a=='y' and 'Y'):
    
    num=[1,2,5,7]

    print(' Starting values',num)
    print('\n Main menu')
    print(' 1.Add \n 2.Update \n 3.Delete \n 4.Insert \n 5.Search')

    num1=int(input('\n\t Enter the section. ='))

    if(num1==1):

            val1=int(input('\n\t Enter the value for add ='))
            print('\n\t Added value is =',num+[val1])
        
    elif(num1==2):
        
        b='y'
        while(b=='y'):
            val1=int(input('\n\t Enter the positon to update(0 to 3) ='))
            
            if(val1>len(num)-1):
                print('\n\t The Position is out of range')
            else:
                break
            
        val2=int(input('\n\t Enter the values to update ='))
        num[val1]=val2
        print('\n\t Updated value is ',num)

    elif(num1==3):

        b='y'
        while(b=='y'):
            val1=int(input('\n\t Enter the positon to delete(0 to 3) ='))

            if(val1>len(num)-1):
                print('\n\t The position is out of range')
            else:
                break
            
        del num[val1]
        print('\n\t Deleted value is ',num)

    elif(num1==4):

        b='y'
        while(b=='y'):
            val1=int(input('\n\t Enter the positon to insert (0 to 3) ='))

            if(val1>len(num)-1):
                print('\n\t The position is out of range')
            else:
                break
                     
        val2=int(input('\n\t Enter the values to insert ='))
        num.insert(val1,val2)
        print('\n\t Inserted value is ',num)


    elif(num1==5):
        z=0
        n=int(input('\n\t Enter the value ='))
        for pos in range(0,len(num)):
         
            if(n==num[pos]):
                print ('\n\t Value exist at position',z)    
            else:
                print('\n\t Value dont exist at position',z)
            z+=1


    a=input('\n Do you want to continue(y/n) =')
    print('\n-------------------------------------------------')
    