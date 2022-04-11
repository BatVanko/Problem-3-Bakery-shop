# Problem-3-Bakery-shop
Maria is opening a bakery shop , and she needs your help to keep track of the stock availability.
Create a program that keeps the information about the stock at the shop. You will be receiving lines with commands until you receive the “ Complete” command. The possible commands are:
o	"Receive {quantity} {food}"
Add the quantity to the given food.
If the food doesn’t exist, add it to your record. If the quantity is not valid (<=0), ignore the command.
o	"Sell {quantity} {food}":
If the food is not in your record print:
"You do not have any {food}."
                     If there is not enough quantity of the wanted food, you should sell (decrese) what you have in stok and then remove the food from your report . Print :
o	"There aren't enough {food}. You sold the last {sold quantity} of them."
o	Otherwise decrease the quantity of the given food and print : 
o	"You sold {quantity} {food}."
If,  after redusing the quantity, there is 0 amount of this food , you should remove it from your record. You must keep track of all sold food quantities! In the end , you should print the stock availability in the format:
o	"{food1}: {quantity}
{food2}: {quantity}
…
{foodN}: {quantity}
All sold: {count of all sold food quantity} goods"
  
Input
Receive 105 cookies
Receive 10 donuts
Sell 10 donuts
Sell 1 bread
Complete
Output
You sold 10 donuts.
You do not have any bread.
cookies: 105
All sold: 10 goods


 
