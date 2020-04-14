"""
This problem was asked by Square.

In front of you is a row of N coins, with values v1, v1, ..., vn.

You are asked to play the following game. You and an opponent take turns 
choosing either the first or last coin from the row, removing it from the row, 
and receiving the value of the coin.

Write a program that returns the maximum amount of money you can win with certainty, 
if you move first, assuming your opponent plays optimally.
"""


#Assume that opponent select coin only based on the instant comparision of the two 
#outer coins. Besides, assume that no dupulicate value occurs
def maxMoney(Ncoins):
    if Ncoins==None or Ncoins==[]:
        return 0
    n=len(Ncoins)
    max_amount=0
    if n<=2:
        for i in range(n):
            max_amount=max(Ncoins[i],max_amount) 
        return max_amount

    left_result=result_optimal_opponent(Ncoins[1:])
    left_choice=maxMoney(left_result)

    right_result=result_optimal_opponent(Ncoins[:-1])
    right_choice=maxMoney(right_result)


    return max(left_choice+Ncoins[0],right_choice+Ncoins[-1])
    

def result_optimal_opponent(coins_list):
    if coins_list[0]>coins_list[-1]:
        return coins_list[1:]
    else:
        return coins_list[:-1]
    


if __name__=="__main__":
    N=[2,4,1,3,5]
  
    print(maxMoney(N))