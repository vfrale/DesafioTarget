#3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, 
#faça um programa, na linguagem que desejar, que calcule e retorne:
#• O menor valor de faturamento ocorrido em um dia do mês;
#• O maior valor de faturamento ocorrido em um dia do mês;
#• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
#IMPORTANTE:
#a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
#b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json

def calcular_metricas(json_fat):
    fat_diario = json_fat['setembro']
    fats = [dia for dia in fat_diario if dia['faturamento'] > 0]

    if not fats:
        return "Não há dados de faturamento"

    valores_fat = [dia['faturamento'] for dia in fats]
    datas_acima_media = [dia['dia'] for dia in fats if dia['faturamento'] > sum(valores_fat) / len(valores_fat)]

    menor_fat = min(valores_fat)
    maior_fat = max(valores_fat)
    dias_acima_media = len(datas_acima_media)

    return {
        "menor_faturamento": menor_fat,
        "maior_faturamento": maior_fat,
        "dias_acima_media": dias_acima_media,
        "datas_acima_media": datas_acima_media
    }


# JSON com dados de faturamento
faturamento_2024 = '''
{
    "setembro": [
        {"dia": "2024-09-01", "faturamento": 0},
        {"dia": "2024-09-02", "faturamento": 4567.23},
        {"dia": "2024-09-03", "faturamento": 2043.45},
        {"dia": "2024-09-04", "faturamento": 4567.89},
        {"dia": "2024-09-05", "faturamento": 1289.21},
        {"dia": "2024-09-06", "faturamento": 2345.76},
        {"dia": "2024-09-07", "faturamento": 0.00}
    ]
}
'''

json_fat = json.loads(faturamento_2024)
dados_faturamento = calcular_metricas(json_fat)

print(f"Menor faturamento: R${dados_faturamento['menor_faturamento']:.2f}")
print(f"Maior faturamento: R${dados_faturamento['maior_faturamento']:.2f}")
print(f"Número de dias acima da média: {dados_faturamento['dias_acima_media']}")
print(f"Datas com faturamento acima da média mensal: {', '.join(dados_faturamento['datas_acima_media'])}")

