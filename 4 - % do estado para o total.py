#4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
#• SP – R$67.836,43
#• RJ – R$36.678,66
#• MG – R$29.229,88
#• ES – R$27.165,48
#• Outros – R$19.849,53
#Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.  

import json

faturamento_mensal_por_estado = '''
{
    "setembro": [
        {"estado": "SP", "faturamento": 67836.43},
        {"estado": "RJ", "faturamento": 36678.66},
        {"estado": "MG", "faturamento": 29229.88},
        {"estado": "ES", "faturamento": 27165.48},
        {"estado": "Outros", "faturamento": 19849.53}
    ]
}
'''

def porcentagemEstado(json_fat):
  
  fat_state = json_fat['setembro']
  
  soma = sum([estado['faturamento'] for estado in fat_state])
  response = {}
  
  for valor in fat_state:
    state = valor['estado']
    mean = valor['faturamento']*100/soma
    response[f'{state}'] = round(mean,2)
  
  return response

json_fat = json.loads(faturamento_mensal_por_estado)
dados_faturamento = porcentagemEstado(json_fat)
                                             
for key in dados_faturamento:
  keyy = str(key)
  print(f'Estado: {key}, porcentagem em relação ao faturamento total:',dados_faturamento[f'{keyy}'],'%')          