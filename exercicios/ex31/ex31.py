from time import sleep
local = float(input('Qual distância para onde você vai viajar ? ')) # O Usuário digita a distância
print('Calculando, Aguarde..')
sleep(3)
if local <= 200: 
  local2 = local * 0.50 # Valor recebido caso a distância seja igual ou menor a 200
else:
  local2 = local * 0.45 # Valor recebido caso a distância seja maior que 200
print('O valor da sua viajem é de R$ {}'.format(local2)) # O usuário recebe o valor final