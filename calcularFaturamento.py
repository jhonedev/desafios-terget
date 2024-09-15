import json

faturamentoJsonMensal = '''
{
    "faturamentoDiario": [1321, 1891, 421, 781, 328, 0, 4982, 7784, 749, 6512, 326, 8992, 4632, 0]
}
'''

dadosFaturamento = json.loads(faturamentoJsonMensal)

def calcularFaturamento(relatorioMensal):
    diasComFaturamento = [dia for dia in relatorioMensal if dia > 0]
    
    menorFaturamento = min(diasComFaturamento)
    maiorFaturamento = max(diasComFaturamento)
    mediaMensal = sum(diasComFaturamento) / len(diasComFaturamento)
    
    numeroDiasComValorDiarioAcimaMedia = len([dia for dia in diasComFaturamento if dia > mediaMensal])
    
    print(f"O menor faturamento do mês foi: R${menorFaturamento:.2f}")
    print(f"O maior faturamento do mês foi: R${maiorFaturamento:.2f}")
    print(f"Os dias com faturamento superior à média foram: {numeroDiasComValorDiarioAcimaMedia}")

calcularFaturamento(dadosFaturamento['faturamentoDiario'])
