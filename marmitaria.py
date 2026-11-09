E
pedidos = []              
qtd_pedidos = 0           
total_marmitas = 0        
total_g = 0               
faturamento = 0.0         
maior_pedido = 0.0        


PRECO_P = 15.00
PRECO_M = 18.00
PRECO_G = 22.00
1
print("=== MARMITARIA - SISTEMA DE PEDIDOS ===")

while True:
    
    print("\n--- CAIXA ---")
    print("1 - Registrar pedido")
    print("2 - Fechar o dia")
    opcao = input("Escolha uma opção: ").strip() 

    
    if opcao == "1":

        
        while True:
            entrada = input("Quantas marmitas no pedido (1 a 10)? ").strip()
            
            if entrada in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
                quantidade = int(entrada)  
                break                      
            print("Quantidade inválida! Digite um número de 1 a 10.")

        valor_marmitas = 0.0    
        qtd_g_pedido = 0        
        print("\nTamanhos disponíveis:")
        print(f"  P - R$ {PRECO_P:.2f}")
        print(f"  M - R$ {PRECO_M:.2f}")
        print(f"  G - R$ {PRECO_G:.2f}")

        
        for i in range(quantidade):
            
            while True:
                
                tamanho = input(f"Tamanho da marmita {i + 1} (P/M/G): ").strip().upper()
                if tamanho == "P" or tamanho == "M" or tamanho == "G":
                    break  
                print("Tamanho inválido! Digite P, M ou G.")

            
            if tamanho == "P":
                valor_marmitas += PRECO_P
            elif tamanho == "M":
                valor_marmitas += PRECO_M
            else:  
                valor_marmitas += PRECO_G
                qtd_g_pedido += 1  

        print("\nTaxa de entrega por distância:")
        print(" Até 2 km: grátis")
        print(" Acima de 2 até 5 km: R$ 5,00")
        print(" Acima de 5 até 8 km: R$ 8,00")
        print(" Acima de 8 km: sem entrega (retirada no local, sem taxa)")
        
        print("Frete grátis: pedidos de R$ 80,00 ou mais em marmitas, dentro da área de entrega.")  


        while True:
            entrada = input("Distância da entrega em km: ").strip()
            
            entrada = entrada.replace(",", ".")

            negativo = False
            texto = entrada
            if texto[:1] == "-":
                negativo = True
                texto = texto[1:]

            valido = True
            pontos = 0
            for letra in texto:
                if letra == ".":
                    pontos += 1
                elif letra not in "0123456789":
                    valido = False  
            if pontos > 1 or texto == "" or texto == ".":
                valido = False      

            if valido and negativo:
                print("A distância não pode ser negativa!")
            elif valido:
                distancia = float(texto)  
                break                     
            else:
                print("Valor inválido! Digite um número (ex.: 3 ou 2,5).")

       
        if distancia <= 2:
            taxa = 0.0          
            entrega = True
        elif distancia <= 5:
            taxa = 5.00         
            entrega = True
        elif distancia <= 8:
            taxa = 8.00         
            entrega = True
        else:
            taxa = 0.0          
            entrega = False

        
        if valor_marmitas >= 80 and entrega:
            taxa = 0.0

        
        total_pedido = valor_marmitas + taxa

        qtd_pedidos += 1                    
        total_marmitas += quantidade        
        total_g += qtd_g_pedido             
        faturamento += total_pedido         

        
        if total_pedido > maior_pedido:
            maior_pedido = total_pedido

        
        if entrega:
            tipo = f"entrega a {distancia} km"
        else:
            tipo = f"retirada no local ({distancia} km)"
        registro = (f"Pedido {qtd_pedidos}: {quantidade} marmita(s), {tipo} | "
                    f"Marmitas: R$ {valor_marmitas:.2f} | Taxa: R$ {taxa:.2f} | "
                    f"Total: R$ {total_pedido:.2f}")
        pedidos.append(registro)  

       
        print("\n--- RESUMO DO PEDIDO ---")
        print(f"Valor das marmitas: R$ {valor_marmitas:.2f}")
        print(f"Taxa de entrega:    R$ {taxa:.2f}")
        print(f"Total do pedido:    R$ {total_pedido:.2f}")


    elif opcao == "2":
        print("\n=== FECHAMENTO DO DIA ===")

        if qtd_pedidos == 0:
            print("Nenhum pedido registrado hoje.")
        else:
            print("Pedidos do dia:")
            for registro in pedidos:
                print(" -", registro)

            media = faturamento / qtd_pedidos

            print("\n--- TOTAIS ---")
            print(f"Quantidade de pedidos: {qtd_pedidos}")
            print(f"Total de marmitas vendidas: {total_marmitas}")
            print(f"Marmitas G vendidas: {total_g}")
            print(f"Faturamento (marmitas + taxas): R$ {faturamento:.2f}")
            print(f"Média por pedido: R$ {media:.2f}")
            print(f"Maior pedido: R$ {maior_pedido:.2f}")
        break 

    else:
        print("Opção inválida! Digite 1 ou 2.")

print("\nSistema encerrado. Bom descanso!")
