#猜數字遊戲

secrt_num = 80
guess = None
guess_count = 0
guess_limit = 3
oout_of_linit = False 
while secrt_num != guess and not(oout_of_linit): 
    guess_count += 1
    if guess_count <= guess_limit:   
     guess = int(input("請輸入數字: "))
     if guess > secrt_num:
         print("小一點")
     elif guess < secrt_num:
         print("大一點")
    else:
        out_of_linit = True 

if out_of_linit:
    print("you lose")
else:                
    print("you win")
