import random
r = random.randint(1,100)
count = 0

while True:
	count = count + 1
	num = input('請猜數字1~100: ')	
	num = int(num)
	if num == r :
		print('恭喜你答對了')
		print('這是你你猜的第', count, '次')
		break
	elif num < r :
		print('再大一點')
	elif num > r :
		print('再小一點')
	print('這是你你猜的第', count, '次')


