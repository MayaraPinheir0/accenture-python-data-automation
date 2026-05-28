# Sistema Bancário em Python: Modelagem Orientada a Objetos

> **Nota Arquitetural:** Este projeto consolida a transição de um paradigma procedural (baseado em dicionários) para uma arquitetura de software modular, orientada a objetos.

## 📖 Descrição do Projeto

Este repositório contém a implementação de um sistema bancário em Python, focado na aplicação rigorosa dos princípios de Programação Orientada a Objetos (POO). O sistema gerencia o estado e os comportamentos de Clientes e Contas Bancárias, encapsulando transações financeiras para garantir a integridade e coesão dos dados.

## 🏛️ Arquitetura e Entidades do Domínio

O sistema isola as lógicas de negócios por meio das seguintes entidades ontológicas:

* **`ContaBancaria`:** Classe que define a estrutura de dados e as interfaces (métodos) para operações financeiras fundamentais.
* **`Cliente`:** Entidade autônoma que se relaciona com as contas bancárias por meio de *composição*, associando os titulares aos seus respectivos ativos.
* **`PessoaFisica`:** Especialização (subclasse) de `Cliente`, que estende a entidade base com atributos específicos e formalmente validados (ex.: CPF).
* **`Transacoes`:** Abstração das operações de negócio, como depósitos e saques, que asseguram a consistência lógica e a rastreabilidade das movimentações.

## 🎯 Objetivos e Resolução do Desafio

O desenvolvimento deste sistema responde a um desafio prático do bootcamp da Accenture, modelagem de um sistema bancario, cumprindo as seguintes premissas:

1. **Refatoração de Estado:** Substituição do armazenamento de dados estáticos em memória (dicionários) por um gerenciamento de estado polimórfico encapsulado em objetos.

2. **Modelagem de Relacionamentos:** Aplicação ortogonal dos conceitos de herança, abstração e composição entre clientes, contas e as respectivas operações.

3. **Encapsulamento de Comportamento:** Implementação de operações de depósito e saque como métodos de instância, protegendo o estado interno (saldo) contra mutações algorítmicas indevidas.

## 🚀 Execução do Projeto

Para instanciar o sistema e executar os testes de validação das transações, utilize o interpretador Python no seu terminal:

```bash
# Clone o repositório
git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)

# Acesse o diretório
cd SEU_REPOSITORIO

# Execute o script principal
python sistema-bancario-poo.py
