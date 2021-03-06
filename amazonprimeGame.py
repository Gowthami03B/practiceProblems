""" Amazon prime is designing a game. the player needs to pass n rounds sequentially in this game. rules for the palyer are:  
The player loses power[i] health to complete round i. the player's health must be greater than 0 at all times. the player can choose to use 
armor in any one round. the armor will prevent damage of min(armor,power[i]). Determine the minimum starting health for a player to with the game  
Example: Power = [1,2,6,7] armor = 5  Give the player 12 units of health at the begining of the game. one of the optimal strategies is to use the armor 
in the third round and only lose 1 unit instead of 6. The health of the player after each round is  
12 12 - Power[0] = 12 - 1 = 11 11 - Power[1] = 11 - 2 = 9 9 - Power[2] + armor = 9 - 6 + 5 = 8 8 - Power[3] = 8 - 7 = 1 
No lower starting health will allow a win.  Complete the function findMinHealth in the editor below. 
int Power[n]: health cost in each round int armor: the max amount of health that may be returnd one round only  
Returns: int: the minimum amount of health requiered at the beginig of the game """ 

def amazonprime(nums,armor):     
  return 1 + sum(nums) - min(armor, max(nums)) #We know we need total power and we only subtract      
  #min(armor, power[i]) at one point during the game, +1 is needed bcs power shouldn't be 0 at all times  print(amazonprime([1,2,6,7],5))
