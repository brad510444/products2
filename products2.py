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

with open('products2.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品名稱,商品價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')