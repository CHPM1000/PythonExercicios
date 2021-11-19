produto=float(input('preço ?$'))
novo=float(produto -(produto*30/100))
print('Aqui na black fraude o que custava ${:.5}\nsai com 30% de desconto ${:.5}'.format(produto,novo))