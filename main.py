from hash import Hash
import os
from data import dados
class Main:
    hash = Hash(tam=13)

    def opcao(self):
        repete = True
        while repete:
            opc = self.hash.menu()
            if(opc>0 & opc<7):
                if (opc == 1):
                    os.system("clear") or None
                    print("Opção selecionada: 1. Exibir Dados\n")
                    self.hash.exibirDados()
                elif (opc == 2):
                    os.system("clear") or None
                    print("Opção selecionada: 2. Exibir lista")
                    self.hash.exibir()
                elif (opc == 3):
                    os.system("clear") or None
                    print("Opção selecionada: 3. Inserir")
                    self.hash.inserir()
                elif (opc == 4):
                    os.system("clear") or None
                    print("Opção selecionada: 4. Taxa de ocupação")
                    taxa,num = self.hash.taxaOcupacao()
                    print("Taxa de ocupação: ",taxa,"%")
                    self.hash.taxaOcupacao()
                elif (opc==5):
                    os.system("clear") or None
                    print("Opção selecionada: 5. Adicionar todos de uma lapada só")
                    self.hash.addAll()
                elif (opc==6):
                    os.system("clear") or None
                    print("Opção selecionada: 6. Mostrar saída dos hash")
                    list= [0,1,2,3,4,5,6,7,8,9]
                    for item in list:
                        self.hash.returnPos(nome=dados[item]['Nome'], idade=dados[item]['Idade'], departamento=dados[item]['Departamento'], salario=dados[item]['Salário'], telefone = dados[item]['Telefone'])
            if(opc>7 or opc<0):
                print('aqui')
                os.system("clear") or None
                print("ERROR: OPÇÃO DIGITADA INVÁLIDA!\n")
                repete = True
            if(opc==0): 
                print("Fim da execução.")
                repete = False

main_hash = Main()
main_hash.opcao()