idade= int(input('digite a sua idade:'))
sexo= input('digite o sexo m ou f:').lower()


if idade <18 and sexo == "m":
  print('homem menor de idade')

elif idade >=18 and sexo =='m':
  print ('homem maior de idade')

elif idade < 18 and sexo =='f':
  print('mulher menor de idade')

elif idade >=18 and sexo=='f':
  print('mulher maior de idade')

else:
      print('erro na entrada de dados')