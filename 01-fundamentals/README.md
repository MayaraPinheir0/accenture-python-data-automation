

## 🧠 Arquitetura do Conhecimento (Fundamentals)

A estrutura abaixo reflete uma progressão lógica de aprendizado, organizada para garantir a compreensão da **Carga Cognitiva** necessária para dominar o Python.

### 📍 Fase 01: Os Pilares

| Módulo | Conceito Chave | Arquivo | Conteúdo Técnico |
| :--- | :--- | :--- | :--- |
| **I. Atoms** | Armazenamento de Info | `01_syntax_and_variables.py` | Sintaxe, semântica de variáveis, `print()` e `input()`. |
| **II. Data Types** | Natureza do Dado | `02_data_types.py` | Casting de tipos, Strings, Integers e Floats. |
| **III. Collections** | Agrupamento | `03_lists_and_sequences.py` | Listas, manipulação de índices e métodos (append/remove). |
| **IV. Decision** | Lógica Booleana | `04_conditionals.py` | Estruturas `if/elif/else` e operadores lógicos. |
| **V. Automation** | Eficiência/Ciclos | `05_loops_and_iteration.py` | Laços de repetição `for` e `while`. |
| **VI. Modularization** | Reuso de Código | `06_functions_and_scope.py` | Definição de funções, argumentos e escopo de variáveis. |

---

## 🗺️ Mapa Mental de Fundamentos

Para visualizar como esses conceitos se conectam na construção de um software, utilizamos a seguinte lógica:

```
flowchart TD
    A[Python Fundamentals]

    A --> B[Variables and Types]
    A --> C[Control Flow]
    A --> D[Modularization]
    A --> E[Execution]

    %% Variables and Types
    B --> B1[Primitive Types]
    B1 --> B1a[int]
    B1 --> B1b[float]
    B1 --> B1c[str]
    B1 --> B1d[bool]

    B --> B2[Collections]
    B2 --> B2a[lists]
    B2 --> B2b[dicts]

    B --> B3[Examples]
    B3 --> B3a[Names → strings]
    B3 --> B3b[Age → integers]
    B3 --> B3c[List of dictionaries]

    %% Control Flow
    C --> C1[Conditionals]
    C1 --> C1a[if / elif / else]
    C1 --> C1b[Validation: isdigit()]

    C --> C2[Loops]
    C2 --> C2a[while → interface]
    C2 --> C2b[for → report]

    %% Modularization
    D --> D1[Functions]
    D1 --> D1a[def]
    D1 --> D1b[arguments]
    D1 --> D1c[return]
    D1 --> D1d[Encapsulation: Add Entry]

    D --> D2[Scope]
    D2 --> D2a[local]
    D2 --> D2b[global]

    %% Execution
    E --> E1[Input/Output]
    E1 --> E1a[input()]
    E1 --> E1b[print()]

    E --> E2[Logic Operators]
    E2 --> E2a[and]
    E2 --> E2b[or]
    E2 --> E2c[not]
```

---
