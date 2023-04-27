from data import dados

class Hash:
    def __init__(self,tam) -> None:
        self.tabHash = [None]*tam
        self.tam_max = tam

    # função responsável por exibir um menu
    def menu(self):
        print("\nEscolha uma das opções abaixo: ")
        print("1. Exibir dados da base de dados")
        print("2. Exibir dados da lista")
        print("3. Inserir")
        print("4. Taxa de ocupação")
        print("5. Adicionar todos de uma lapada só")
        print("6. Mostrar saída dos hash")
        print("0. SAIR")
        opc = int(input("Digite a opção: "))
        return opc

    # Função que exibe somente os dados que ainda não foram cadastrados
    def exibirDados2(self):
        for chave, valor in dados.items():
                if(valor['Inserido']==False):
                    self.dados(chave=chave,valor=valor)

    # Função que mostra os dados cadastrados na base de dados e com opção de filtragem
    def exibirDados(self):
        print("Escolha uma opção: ")
        print("0. Todos os dados cadastrados na base de dados")
        print("1. Apenas os que já foram inseridos a lista")
        print("2. Apenas os que ainda não foram inseridos")
        opc = int(input("Digite a opção: "))
        if(opc == 0):
            for chave, valor in dados.items():
                self.dados(chave=chave,valor=valor)
        elif(opc == 1):
            for chave, valor in dados.items():
                if(valor['Inserido']==True):
                    self.dados(chave=chave,valor=valor)
        elif(opc == 2):
            self.exibirDados2()
        else:
            print("Opção Inválida!")
    
    # Função responsável por exibir os dados de forma classificatória
    def dados(self,chave,valor):
        print(f"Funcionário {chave}: ")
        print(f"Nome: {valor['Nome']}")
        print(f"Idade: {valor['Idade']}")
        print(f"Departamento: {valor['Departamento']}")
        print(f"Salário: {valor['Salário']}")
        print(f"Telefone: {valor['Telefone']}")
        print("--------------------")
    
    # Função responsável por exibir a tabela hash
    def exibir(self):
        for i in range(0,self.tam_max):
            print("Hash[",i,"]: ",self.tabHash[i])

    # Função responsável por inserir os valores na tabela hash
    def inserir(self):
        self.exibirDados2()
        valor = int(input("Digite o número do funcionário: "))
        if(valor>=0 and valor <=9):
            self.insert(valor=valor)
        else:
            print("Funcionário não consta na base de dados")

    # Função responsável por retornar a taxa de ocupação e a quantidade de elementos da tabela hash 
    def taxaOcupacao(self):
        num_elementos = len(list(filter(lambda x: x is not None, self.tabHash)))
        taxa = round((num_elementos/self.tam_max)*100,2)
        return taxa,num_elementos
    
    # Função hash simples que pega o valor passado e cálcula o resto da divisão
    def funHash(self,valor):
        pos = valor % self.tam_max
        return pos
    
    # Função hash
    def funHash2(self, valor):
        pos2 = 1 + (valor % (self.tam_max-1))
        return pos2
    
    # Junção das duas funções hash anteriores
    def doubleHash(self,valor1, valor2):
        v1 = self.funHash(valor1)
        v2 = self.funHash2(valor2)
        dh = (v1+v2) % self.tam_max
        return dh,v1,v2
    
    #Função recursiva utilizada para inserir valores
    def insercao(self,valor, dh, valor1, valor2):
        if (self.tabHash[dh]==None):
            self.tabHash[dh] = dados[valor]
            dados[valor]['Inserido'] = True
        else:
            v1 = self.funHash(valor1)
            v2 = self.funHash2(valor2)
            dh2 = (v1+v2) % self.tam_max
            return self.insercao(valor, dh2, v1, v2)
        
    # inseri um valor na tabela hash
    def insert(self,valor):
        if(dados[valor]['Inserido'] == True):
                print('Funcionário já inserido!')
        else: 
            pos = self.returnPos(nome=dados[valor]['Nome'], idade=dados[valor]['Idade'], departamento=dados[valor]['Departamento'], salario=dados[valor]['Salário'], telefone = dados[valor]['Telefone'])
            tel = int(dados[valor]['Telefone'].split("-")[1])
            if (self.tabHash[pos] == None):
                self.tabHash[pos] = dados[valor]
                dados[valor]['Inserido'] = True
            else:
                idade = dados[valor]['Idade']
                rh,v1,v2 = self.doubleHash(valor1=tel, valor2=idade)
                self.insercao(valor=valor,dh=rh,valor1=v1,valor2=v2)
            taxa, num_el = self.taxaOcupacao() 
            if(taxa>=70):
                self.tam_max += 10
                self.tabHash += [None]*10

    # adiciona todos os valores da base de dados de uma vez
    def addAll(self):
        list = [0,1,2,3,4,5,6,7,8,9]
        for item in list:
            self.insert(item)

    # responsável por retornar o valor hash
    def returnPos(self,nome,idade,departamento,salario,telefone,tam=29):
        tamNome = len(nome)
        if departamento == 'Vendas':
            valdep = 2
        elif departamento == 'Administração':
            valdep = 17
        elif departamento == 'Recursos Humanos':
            valdep = 29
        elif departamento == 'Diretoria':
            valdep = 31
        else:
            valdep = 5
        valTel = int(telefone.split("-")[1])
        val_hash1 = tamNome + idade + valdep + salario + valTel
        hash1 = val_hash1 % tam

        str_info = nome + str(idade) + departamento + str(salario) + telefone
        val_hash2 = sum(ord(char) for char in str_info)
        hash2 = 1 + (val_hash2 % tam-1)

        hash_final = (hash1+hash2) % tam

        return hash_final