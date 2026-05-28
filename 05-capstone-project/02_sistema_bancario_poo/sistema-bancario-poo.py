# Sistema Bancário - Projeto de Programação Orientada a Objetos (POO)

from abc import ABC, abstractmethod
from datetime import datetime

#1. Classe para representar um cliente do banco
class Cliente: 

    def __init__(self, endereco): # O método __init__ é o construtor da classe Conta, responsável por inicializar os atributos da conta. Ele recebe o número da conta e o cliente como parâmetros e define os seguintes atributos:  
        self.endereco = endereco # Atributo para armazenar o endereço da conta
        self.contas = [] # Lista para armazenar as contas criadas        
        
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta) # Método para registrar uma transação em uma conta. O método recebe a conta e a transação como parâmetros e chama o método registrar da transação, passando a conta como argumento.
        
    def adicionar_conta(self, conta):
        self.contas.append(conta) # Método para adicionar uma conta à lista de contas do cliente. O método recebe a conta como parâmetro e a adiciona à lista de contas do cliente usando o método append.
        
#1.1. Classe para representar um cliente pessoa física, herda da classe Cliente
class PessoaFisica(Cliente): 

    def __init__(self, nome, data_nascimento,cpf, endereco):
        super().__init__(endereco) # Chama o construtor da classe pai para inicializar o atributo endereco
        self.nome = nome # Atributo para armazenar o nome do cliente
        self.data_nascimento = data_nascimento # Atributo para armazenar a data de nascimento do cliente
        self.cpf = cpf # Atributo para armazenar o CPF do cliente
     
        
#2. Classe para representar uma conta bancária
class Conta:

    def __init__(self, numero_conta, cliente):
        self._saldo = 0 # Atributo para armazenar o saldo da conta, com valor inicial definido como 0 por padrão
        self._numero_conta = numero_conta # Atributo para armazenar o número da conta
        self._agencia = "0001" # Atributo para armazenar a agência da conta, com valor padrão definido como "0001"
        self._cliente = cliente # Atributo para armazenar o cliente associado à conta
        self._historico = Historico() # Atributo para armazenar o histórico de transações da conta, inicializado como uma instância da classe Historico
        
    #2.1. Os métodos de classe e propriedades sao definidos para acessar os atributos da conta e realizar as operações de saque, depósito e transferência.
    @classmethod
    def nova_conta(cls, numero_conta, cliente):
        return cls(numero_conta, cliente) # Método de classe para criar uma nova conta. O método recebe o número da conta e o cliente como parâmetros e retorna uma nova instância da classe Conta usando o construtor da classe.
    @property
    def saldo(self):
        return self._saldo # Propriedade para acessar o saldo da conta. O método retorna o valor do atributo _saldo.
    @property
    def numero_conta(self):
        return self._numero_conta # Propriedade para acessar o número da conta. O método retorna o valor do atributo _numero_conta.
    @property
    def agencia(self):
        return self._agencia # Propriedade para acessar a agência da conta. O método retorna o valor do atributo _agencia.
    @property
    def cliente(self):
        return self._cliente # Propriedade para acessar o cliente associado à conta. O método retorna o valor do atributo _cliente.
    @property
    def historico(self):
        return self._historico # Propriedade para acessar o histórico de transações da conta. O método retorna o valor do atributo _historico.

    #2.2. Funcoes para realizar comportamento na classe, as operações de saque e depósito na conta (INTERFACE)
    #2.2.1. Função para realizar um saque na conta,
    # verifica se o valor do saque é válido e se o saldo é suficiente para realizar a operação.
    def sacar(self, valor):
        
        saldo = self.saldo # Obtém o saldo atual da conta usando a propriedade saldo
        excedeu_saldo = valor > saldo # Verifica se o valor do saque excede o saldo disponível
    
        if excedeu_saldo:
            print("\n@@@ Saldo insuficiente para realizar o saque. @@@") # Imprime uma mensagem de erro caso o saldo seja insuficiente
            
        elif valor > 0:
            self._saldo -= valor # Subtrai o valor do saque do saldo da conta
            print(f"\nSaque de R$ {valor:.2f} realizado com sucesso. Novo saldo: R$ {self.saldo:.2f}") # Imprime uma mensagem de sucesso com o valor do saque e o novo saldo da conta
            return True # Retorna True para indicar que o saque foi realizado com sucesso
        
        else:
            print("\n@@@ Operaçao falhou! Valor informado é inválido. @@@") 
            
        return False # Retorna False para indicar que o saque não foi realizado devido a um valor inválido
        
    #2.2.1. Função para realizar um depósito na conta, 
    # verifica se o valor do depósito é válido.
    def depositar(self, valor):
        
        if valor > 0:
            self._saldo += valor # Adiciona o valor do depósito ao saldo da conta
            print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso. Novo saldo: R$ {self.saldo:.2f}") # Imprime uma mensagem de sucesso com o valor do depósito e o novo saldo da conta    
        
        else:
            print("\n@@@ Operaçao falhou! Valor informado é inválido. @@@") 
            return False # Retorna False para indicar que o depósito não foi realizado devido a um valor inválido
        return True # Retorna True para indicar que o depósito foi realizado com sucesso

#2.3. Subclasse da classe Conta para representar uma conta corrente, com um limite de saque e um limite de crédito.
class ContaCorrente(Conta):
    def __init__(self, numero_conta, cliente, limite_saques=3, limite=500.00):
        super().__init__(numero_conta, cliente) # Chama o construtor da classe pai para inicializar os atributos da conta
        self._limite = limite # Atributo para armazenar o limite de saques da conta, com valor padrão definido como 3
        self._limite_saques = limite_saques # Atributo para armazenar o limite de saque da conta, com valor padrão definido como 500.00
        
    #2.3.1. Sobrescrita do método sacar para implementar a lógica de limite de saques e limite de crédito.
    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == "Saque"]) # Obtém o número de saques realizados na conta filtrando as transações do histórico e contando quantas são do tipo "Saque"
        
        excedeu_limite_saques = numero_saques >= self._limite_saques # Verifica se o número de saques realizados excede o limite de saques permitido
        excedeu_limite = valor > self._limite # Verifica se o valor do saque excede o limite de saque permitido
        
        if excedeu_limite_saques:
            print("\n@@@ Limite de saques diários excedido. @@@") # Imprime uma mensagem de erro caso o limite de saques diários seja excedido  
        
        elif excedeu_limite:
            print("\n@@@ Valor do saque excede o limite permitido. @@@") # Imprime uma mensagem de erro caso o valor do saque exceda o limite permitido
        
        else:
            return super().sacar(valor) # Chama o método sacar da classe pai para realizar o saque normalmente caso os limites não sejam excedidos 
        
        return False # Retorna False para indicar que o saque não foi realizado devido a um dos limites ter sido excedido   
    
    #2.3.2. Padronizar a saida de informações da conta corrente, sobrescrevendo o método __str__ para exibir as informações da conta de forma formatada.
    def __str__(self):
        return f"""
        Agência: \t\t {self.agencia}
        Número da Conta: \t {self.numero_conta}
        Titular: \t\t {self.cliente.nome}
        """
        
#3. Classe para representar o histórico de transações da conta
#3.1. A classe Historico é responsável por armazenar e exibir o histórico de transações da conta. Ela possui um atributo para armazenar as transações e um método para exibir o histórico de transações de forma formatada.
class Historico:

    def __init__(self):
        self._transacoes = [] # Atributo para armazenar as transações, inicializado como uma lista vazia
        
    @property
    def transacoes(self):
        return self._transacoes # Propriedade para acessar as transações. O método retorna o valor do atributo _transacoes.
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": type(transacao).__name__, # Adiciona o tipo da transação usando type(transacao).__name__ para obter o nome da classe da transação
                "valor": transacao.valor, # Adiciona o valor da transação usando transacao.valor, assumindo que a classe Transacao possui um atributo valor que armazena o valor da transação
                "data": datetime.now().strftime # Adiciona a data e hora da transação usando datetime.now() para obter a data e hora atual e strftime para formatar a data e hora em uma string no formato "dd-mm-aaaa hh:mm:ss"
                ("%d-%m-%Y %H:%M:%S"),
            }
        ) # Método para adicionar uma transação ao histórico. O método recebe a transação como parâmetro e a adiciona à lista de transações usando o método append.
        

#4. Classe para representar uma transação bancária
#4.1. A classe Transacao é uma classe abstrata que define a estrutura para as transações bancárias. Ela possui um método abstrato registrar, que deve ser implementado pelas subclasses para registrar a transação em uma conta. O método registrar recebe a conta como parâmetro e deve implementar a lógica para registrar a transação no histórico da conta.
class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass # Propriedade abstrata para acessar o valor da transação. O método é decorado com @abstractproperty para indicar que deve ser implementado pelas subclasses.
    
    @abstractmethod
    def registrar(self, conta):
        pass # Método abstrato para registrar a transação em uma conta. O método é decorado com @abstractclassmethod para indicar que deve ser implementado pelas subclasses e recebe a conta como parâmetro.
    
#4.2. A classe Saque é uma subclasse da classe Transacao que representa uma transação de saque. Ela possui um atributo para armazenar o valor do saque e implementa o método registrar para registrar a transação de saque em uma conta. O método registrar chama o método sacar da conta para realizar o saque e, se a transação for bem-sucedida, adiciona a transação ao histórico da conta usando o método adicionar_transacao do histórico da conta.
class Saque(Transacao):

    def __init__(self, valor):
        self._valor = valor # Atributo para armazenar o valor da transação, inicializado no construtor da classe
        
    @property
    def valor(self):
        return self._valor # Propriedade para acessar o valor da transação. O método retorna o valor do atributo _valor.
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self) # Se a transação for bem-sucedida, adiciona a transação ao histórico da conta usando o método adicionar_transacao do histórico da conta
           

#4.3. A classe Deposito é uma subclasse da classe Transacao que representa uma transação de depósito. Ela possui um atributo para armazenar o valor do depósito e implementa o método registrar para registrar a transação de depósito em uma conta. O método registrar chama o método depositar da conta para realizar o depósito e, se a transação for bem-sucedida, adiciona a transação ao histórico da conta usando o método adicionar_transacao do histórico da conta.
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor # Atributo para armazenar o valor da transação, inicializado no construtor da classe
        
    @property
    def valor(self):
        return self._valor # Propriedade para acessar o valor da transação. O método retorna o valor do atributo _valor.
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self) # Se a transação for bem-sucedida, adiciona a transação ao histórico da conta usando o método adicionar_transacao do histórico da conta   
            
            
#5. Instanciando objetos e realizando operações
if __name__ == "__main__":
    cliente1 = PessoaFisica("Mayara Pinheiro", "01/01/1990", "123.456.789-00", "Rua Exemplo, 123") # Cria um cliente do tipo PessoaFisica com os dados fornecidos
    
    conta1 = ContaCorrente.nova_conta("12345-6", cliente1) # Cria uma conta corrente para o cliente usando o método de classe criar_conta da classe ContaCorrente
    cliente1.adicionar_conta(conta1) # Adiciona a conta criada à lista de contas do cliente usando o método adicionar_conta do cliente
    print(conta1) # Imprime as informações da conta usando o método __str__ da classe ContaCorrente
    
    deposito1 = Deposito(500.00) # Cria uma transação de depósito com o valor de 500.00 usando a classe Deposito
    cliente1.realizar_transacao(conta1, deposito1) # Realiza a transação de depósito na conta do cliente usando o método realizar_transacao do cliente, passando a conta e a transação como parâmetros
    print(conta1) # Imprime as informações da conta novamente para verificar o saldo 
    
    saque1 = Saque(200.00) # Cria uma transação de saque com o valor de 200.00 usando a classe Saque
    cliente1.realizar_transacao(conta1, saque1) # Realiza a transação de saque na conta do cliente usando o método realizar_transacao do cliente, passando a conta e a transação como parâmetros
    print(conta1) # Imprime as informações da conta novamente para verificar o saldo após o saque