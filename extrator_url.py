import re
#criando a variável endereço
endereco = input("Digite seu endereço aqui: ")

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")

#verificando se o padrão foi encontrado

busca = padrao.search(endereco)

if busca:
    cep = busca.group()
    print(f"O Cep é: {cep}")
elif not busca:
    print("O endereço não tem cep")