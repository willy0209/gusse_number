import random
r = random.randint(1,100)

while True:
	num = input('請猜數字1~100: ')	
	num = int(num)
	if num == r :
		print('恭喜你答對了')
		break
	elif num < r :
		print('再大一點')
	elif num > r :
		print('再小一點')


