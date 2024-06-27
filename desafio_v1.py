from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas= []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
        pass

    def adicionar_conta(self,conta):
        self.contas.append(conta)
    

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

    

class Conta:
    def __init__(self, numero, cliente):
        self.saldo = 0
        self.numero = numero
        self.cliente = cliente
        self.historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n*****Operação falhou! Saldo insuficiente.*****")
        
        elif valor > 0:
            self._saldo -= valor
            print("\n*****Saque realizado com sucesso!*****")
            return True
        
        else:
            print("\n*****Operação falhou! O valor informado é inválido.*****")
            return False
        
        def depositar(self, valor):
            pass


class ContaCorrente(Conta):
    pass

class Historico():
    pass

class Transacao(ABC):
    pass

class Saque(Transacao):
    pass

class Deposito(Transacao):
    pass