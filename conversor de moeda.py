real=float(input('Conversor de moeda, valores: $'))
Dólar= real/5.50
Euro= real/6.22
Dólar_Canadense= real/4.38
print('Com ${} você pode comprar\nUS$ {:.4}\nEURO {:.4}\nC$ {:.4}'.format(real,Dólar,Euro,Dólar_Canadense))
#Coloco a descrição da moeda que quero e logo após coloco o valor de quanto custa o valor da nossa moeda,na moeda deles
#exemplo 1dolar;5.50 nunca colocar virgula, já {:.3} é quantos digitos quero ter no valor!!!
