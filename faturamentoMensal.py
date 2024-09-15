def calcularPercentualFaturamento():
    faturamentoEstados = {
        'SP': 67836.43,
        'RJ': 36678.66,
        'MG': 29229.88,
        'ES': 27165.48,
        'Outros': 19849.53
    }
    
    totalFaturamento = sum(faturamentoEstados.values())
    
    for estado, valor in faturamentoEstados.items():
        percentual = (valor / totalFaturamento) * 100
        print(f'{estado}: Obteve {percentual:.2f}% do faturamento total da distribuidora.')

calcularPercentualFaturamento()
