#I declare that my work contains no examples of misconduct, such as plagarism, or collusion.
#Any code taken from other sources is referenced within my code solution.
#Student ID-20221574(W1999471)
#Date-20/04/2023

#validations
passs=0
defer=0
fail=0
count_1=0
count_2=0
count_3=0
count_4=0
star_1=0
star_2=0
star_3=0
star_4=0
list_m=[]
file=open('Progression Details.txt','w')

while True:
    while True:
        try:
            passs=int(input('Please enter your credit at pass: '))
        except ValueError:
            print('Integer required.')
            continue
        
        if passs<=120 and passs>=0:
            if passs!=0 and passs%20!=0:
                print('Out of range.')
                continue    
        else:
            print('Out of range.')
            continue    
        
        break


    while True:   
        try:
            defer=int(input('Please enter your credit at defer: '))
        except ValueError:
            print('Integer required.')
            continue
        
        if defer<=120 and defer>=0:
            if defer!=0 and defer%20!=0:
                print('Out of range.')
                continue
        else:
            print('Out of range.')
            continue    
        
        break

    while True:
        try:
            fail=int(input('Please enter your credit at fail: '))
        except ValueError:
            print('Integer required.')
            continue
        
        if fail<=120 and fail>=0:
            if fail!=0 and fail%20!=0:
                print('Out of range.')
                continue
        else:
            print('Out of range.')
            continue
        break

    total=passs+defer+fail        
    while True:
        if total!=120:
            print('Total incorrect')
        break

    total=passs+defer+fail
    if total==120:
        if passs==120 and defer==0 and fail==0  :
            print('Progression Outcome-Progress')
            list_m.append('progress'+' '+'-'+' '+str(passs)+','+' '+str(defer)+','+' '+str(fail))
            file.write('\n progress'+' '+'-'+' '+str(passs)+','+' '+str(defer)+','+' '+str(fail))
            count_1=count_1+1
            star_1='*'*count_1
        elif passs==100 and (defer==20 or defer==0) and (fail==0 or fail==20) :
            print('Progression Outcome-progress(module trailer)')
            list_m.append('progress (module trailer)'+' '+'-'+' '+str(passs)+','+' '+str(defer)+','+' '+str(fail))
            file.write('\n progress (module trailer)'+' '+'-'+' '+str(passs)+','+' '+str(defer)+','+' '+str(fail))
            count_2=count_2+1
            star_2='*'*count_2
        elif (passs==40 or passs==20 or passs==0) and (defer==0 or defer==20 or defer==40) and (fail==80 or fail==100 or fail==120):
            print('Progression Outcome-Exclude')
            list_m.append('exclude'+' '+'-'+' '+str(passs)+','+' '+str(defer)+','+' '+str(fail))
            file.write('\n exclude'+' '+'-'+' '+str(passs)+','+' '+str(defer)+','+' '+str(fail))
            count_3=count_3+1
            star_3='*'*count_3
        else:
            print('Progression Outcome-Do Not Progress-module retriever')
            list_m.append('module retriever'+' '+'-'+' '+str(passs)+','+' '+str(defer)+','+' '+str(fail))
            file.write('\n module retriever'+' '+'-'+' '+str(passs)+','+' '+str(defer)+','+' '+str(fail))
            count_4=count_4+1
            star_4='*'*count_4
        print('\n')    
        print('Would you like to enter another set of data?')
    yes=input('Enter "y" for yes or "q" to quit and view results:' )
    if yes.lower()=='q':
        break
    print('\n')

print('--------------------------------------------------------------------------------')
print('Histogram')
print('progress                ',count_1,':',star_1)
print('progress(module trailer)',count_2,':',star_2)
print('exclude                 ',count_3,':',star_3)
print('module retriever        ',count_4,':',star_4)
total_outcomes=count_1+count_2+count_3+count_4
print(total_outcomes,'outcomes in total.')
print('--------------------------------------------------------------------------------')



for item in list_m:
    print(item)
    
file.close()


print('\n')

dict1={}
dict2={}

#student id =n


      

while True:
    try:
        n=(input('Enter student ID(8 characters required):'))
        p=(n[0]+','+n[1]+','+n[2]+','+n[3]+','+n[4]+','+n[5]+','+n[6]+','+n[7])
        if len(p)!=15:
            print('Enter correct student ID')
    except ValueError:
        ('Integer Required.')
        
        break

    while True:
        try:
            passs=int(input('Please enter your credit at pass: '))
        except ValueError:
            print('Integer required.')
            continue
        
        if passs<=120 and passs>=0:
            if passs!=0 and passs%20!=0:
                print('Out of range.')
                continue    
        else:
            print('Out of range.')
            continue    
        
        break


    while True:   
        try:
            defer=int(input('Please enter your credit at defer: '))
        except ValueError:
            print('Integer required.')
            continue
        
        if defer<=120 and defer>=0:
            if defer!=0 and defer%20!=0:
                print('Out of range.')
                continue
        else:
            print('Out of range.')
            continue    
        
        break

    while True:
        try:
            fail=int(input('Please enter your credit at fail: '))
        except ValueError:
            print('Integer required.')
            continue
        
        if fail<=120 and fail>=0:
            if fail!=0 and fail%20!=0:
                print('Out of range.')
                continue
        else:
            print('Out of range.')
            continue
        break

    total=passs+defer+fail        
    while True:
        if total!=120:
            print('Total incorrect')
        else:
        
            if passs==120 and defer==0 and fail==0 :
                dict2[n]=('progress'+' '+'-'+' '+str(passs)+','+' '+str(defer)+','+' '+str(fail))
                
            elif passs==100 and (defer==20 or defer==0) and (fail==0 or fail==20) :
                dict2[n]=('progress (module trailer)'+' '+'-'+' '+str(passs)+','+' '+str(defer)+','+' '+str(fail))
            elif(passs==40 or passs==20 or passs==0) and (defer==0 or defer==20 or defer==40) and (fail==80 or fail==100 or fail==120) :
                
                dict2[n]=('exclude'+' '+'-'+' '+str(passs)+','+' '+str(defer)+','+' '+str(fail)) 
            else:
                dict2[n]=('do not progress (module retriever)'+' '+'-'+' '+str(passs)+','+' '+str(defer)+','+' '+str(fail))

        break
    print('\n')
    yes=input('would you like to enter another set of data? \nEnter enter y for yes or q to quit and view results: ')

    if yes=='y':
        print('\n')
        continue
    elif yes=='q':
       break
    else:
        print('please enter y or q')
for m,total_outcomes in dict2.items():
    print( m,':',total_outcomes)
