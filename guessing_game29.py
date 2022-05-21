#猜數字遊戲

secrt_num = 80
guess = None
guess_count = 0
guess_limit = 3
oout_of_linit = False 
while secrt_num != guess and not(oout_of_linit): 
    guess_count += 1
    if guess_count <= guess_limit:   
     guess = int(input("Please enter the number: "))
     if guess > secrt_num:
         print("smaller")
     elif guess < secrt_num:
         print("bigger")
    else:
        out_of_linit = True 

if out_of_linit:
    print("you lose")
else:                
    print("you win")
