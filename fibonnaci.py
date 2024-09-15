def fibonnaci(numero):
    sequenciaFibonnaci = [0, 1]

    while sequenciaFibonnaci[-1] < numero:
        ultimoNumero = sequenciaFibonnaci[-1]
        penultimoNumero = sequenciaFibonnaci[-2]
        
        novoValor = ultimoNumero + penultimoNumero
        sequenciaFibonnaci.append(novoValor)
    
    if numero in sequenciaFibonnaci:
        print(f'O número {numero} pertence à sequência de Fibonacci.')
    else:
        print(f'O número {numero} não pertence à sequência de Fibonacci.')

numeroEscolhido = int(input("Digite o numero:"))
fibonnaci(numeroEscolhido)