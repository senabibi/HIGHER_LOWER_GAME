import random
from art import logo,vs
from game_data import data
import os
#Display first logo

def format_data(account):
    account_name=account["name"]
    account_description=account["description"] 
    account_counrty=account["country"]
    return f"{account_name}, a {account_description},from {account_counrty} "
def check_answer(guess,a_follower_count,b_follower_count):
    score=0
    if max(a_follower_count,b_follower_count)==guess:
        return guess=="a"
        
    else:
        return guess=="b"



print(logo)
score=0
ll_continue=True
account_b=random.choice(data)
while ll_continue:
    account_a=account_b
    account_b=random.choice(data)
    while account_a==account_b:
        account_b=random.choice(data)
    print(f"Compare A:{format_data(account_a)}")
    print(vs)
    print(f"Compare B:{format_data(account_b)}")
    guess=input("Who has more follower?Type 'A' or 'B':").lower()
    a_follower_count=account_a["follower_count"]
    b_follower_count=account_b["follower_count"]
    is_correct=check_answer(guess,a_follower_count,b_follower_count)
    os.system("cls")
    if is_correct:
        score+=1
        print(f"You're right!.Current score is {score}")
    else:
        ll_continue=False
        print(f"Sorry,that's wrong!Final score is {score}")
       