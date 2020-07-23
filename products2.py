products = []
while True:
	name = input('請問商品名稱')
	if name == 'q':
		break
	price = input('請輸入商品價格')
	#p = []
	#p.append(name)
	#p.append(price)
	#p = [name, price]
	products.append([name, price])

for f in products:
	print(f[0], '的價錢是', f[1], '元')

with open('products2.csv', 'w') as f:
	for p in products:
		f.write(p[0] + ',' + p[1])