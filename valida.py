#multipliaca os 9 primeiros digitos pelos numeros de 10 a 2
#soma o resultado, multiplicapor 10 e divide por 11
#verifica o resto da divisão - deve ser igual ao primeiro digito verificador

#multipliaca os 9 primeiros digitos e o primeiro digito verificado pelos numeros de 11 a 2
#soma o resultado, multiplicapor 10 e divide por 11
#verifica o resto da divisão - deve ser igual ao segundo digito verificador

#CPFs com todos os digitos iguais entram na regra de cima mas são invalidos


#crianção função pra validar o CPF
def valida_cpf(cpf):
  #Transformando a String recebida em Interios com a função map() e jogando em uma lista
  num_cpf = list(map(int,cpf[:9]))
  #calculo do primeiro dígito verificador 
  resto = ((sum(x * (10-i) for i, x in enumerate(num_cpf)))*10)%11

  #se o resto da divisão for igual a 10 o numero será zero
  if resto == 10:
    resto = 0
  print(resto)
  #adicionando o digito verificar à lista
  num_cpf.append(resto)

  #calculo do segundo dígito verificador
  resto2 = ((sum(x * (11-i) for i, x in enumerate(num_cpf)))*10)%11
  if resto2 == 10:
    resto2 = 0
  print(resto2)

def verifica_digitos(cpf):
  if len(cpf) < 11 or len(cpf) > 11:
    print ('Quantidade de digitos incorreta, digite somente números.')
  else:
    digitos_cpf = cpf[0] * len(cpf)
    #print(digitos_cpf)
    if digitos_cpf == cpf:
      print('CPF invalido')
      #return false

