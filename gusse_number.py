import random
start = input('請決定隨機數字的範圍開始值: ')
end = input('請決定隨機數字的範圍結束值: ')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0

while True:
	count = count + 1
	num = input('請猜數字' + str(start) + '到'+ str(end) + ':')	
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


