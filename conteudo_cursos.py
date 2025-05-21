"""
Conteúdo para os cursos da Plataforma de Educação Digital
"""

# Conteúdo para o curso "Introdução ao Pensamento Computacional"
CONTEUDO_PENSAMENTO_COMPUTACIONAL = {
    "topico1": {
        "titulo": "O que é Pensamento Computacional",
        "conteudo": """O Pensamento Computacional é uma abordagem para resolver problemas que se baseia em conceitos fundamentais da ciência da computação. Ele envolve formular problemas de uma maneira que permita usar um computador e outras ferramentas para ajudar a resolvê-los.

Os quatro pilares do Pensamento Computacional são:

1. Decomposição: Dividir um problema complexo em partes menores e mais gerenciáveis.
2. Reconhecimento de padrões: Identificar similaridades ou padrões entre problemas.
3. Abstração: Focar apenas nos detalhes importantes, ignorando informações irrelevantes.
4. Algoritmos: Desenvolver uma solução passo a passo para o problema.

O Pensamento Computacional não é apenas para programadores ou cientistas da computação. É uma habilidade útil para todos, pois ajuda a abordar problemas de forma sistemática e lógica."""
    },
    "topico2": {
        "titulo": "Decomposição de Problemas",
        "conteudo": """A decomposição é o processo de dividir um problema complexo em partes menores e mais gerenciáveis. Isso torna o problema mais fácil de entender e resolver.

Exemplo prático:
Imagine que você precisa organizar uma festa de aniversário. Em vez de pensar em tudo de uma vez, você pode decompor o problema em tarefas menores:
- Criar uma lista de convidados
- Escolher o local
- Planejar o cardápio
- Preparar decorações
- Enviar convites

Ao decompor o problema, você pode trabalhar em cada parte separadamente, tornando o processo mais organizado e eficiente.

Exercício mental: Pense em uma tarefa complexa do seu dia a dia e tente decompô-la em partes menores."""
    },
    "topico3": {
        "titulo": "Reconhecimento de Padrões",
        "conteudo": """O reconhecimento de padrões envolve identificar similaridades ou características comuns entre problemas. Ao reconhecer padrões, podemos aplicar soluções conhecidas a novos problemas.

Exemplos de padrões:
- Sequências numéricas: 2, 4, 6, 8, ... (números pares)
- Padrões em textos: palavras que seguem regras gramaticais semelhantes
- Padrões em comportamentos: como pessoas reagem em situações similares

Na computação, o reconhecimento de padrões é fundamental para:
- Inteligência artificial e aprendizado de máquina
- Processamento de imagens
- Análise de dados
- Compressão de dados

Quando identificamos um padrão, podemos criar regras ou modelos que descrevem esse padrão, permitindo prever ou gerar novos exemplos."""
    },
    "topico4": {
        "titulo": "Abstração",
        "conteudo": """A abstração é o processo de focar apenas nos detalhes importantes de um problema, ignorando informações irrelevantes. Isso nos ajuda a criar modelos simplificados da realidade.

Exemplos de abstração:
- Um mapa é uma abstração do mundo real, mostrando apenas as informações relevantes para navegação
- Uma receita de bolo é uma abstração que captura apenas os passos essenciais para fazer um bolo
- Um modelo de dados é uma abstração que representa apenas as características relevantes dos dados

Na programação, usamos abstração constantemente:
- Variáveis abstraem valores
- Funções abstraem sequências de operações
- Classes abstraem objetos e comportamentos

A abstração nos permite lidar com a complexidade, focando apenas no que é importante para resolver um problema específico."""
    },
    "topico5": {
        "titulo": "Algoritmos",
        "conteudo": """Um algoritmo é uma sequência finita de instruções bem definidas para resolver um problema ou realizar uma tarefa. É como uma receita que descreve exatamente o que fazer, passo a passo.

Características de um bom algoritmo:
- Precisão: cada passo deve ser claro e não ambíguo
- Finitude: deve terminar após um número finito de passos
- Eficácia: deve resolver o problema proposto
- Generalidade: deve funcionar para todos os casos válidos do problema

Exemplo simples de algoritmo:
Como fazer um sanduíche:
1. Pegue duas fatias de pão
2. Espalhe manteiga em uma face de cada fatia
3. Adicione os ingredientes desejados entre as fatias
4. Junte as fatias com os ingredientes no meio

Na programação, os algoritmos são expressos em linguagens de programação, mas o conceito de algoritmo é mais amplo e pode ser aplicado a qualquer processo sistemático."""
    }
}

# Exercícios para o curso "Introdução ao Pensamento Computacional"
EXERCICIOS_PENSAMENTO_COMPUTACIONAL = [
    {
        "pergunta": "Qual dos seguintes NÃO é um dos quatro pilares do Pensamento Computacional?",
        "opcoes": [
            "Decomposição",
            "Programação",
            "Abstração",
            "Algoritmos"
        ],
        "resposta_correta": 1
    },
    {
        "pergunta": "O que é a decomposição no contexto do Pensamento Computacional?",
        "opcoes": [
            "O processo de identificar padrões em problemas",
            "O processo de dividir um problema complexo em partes menores",
            "O processo de criar uma sequência de passos para resolver um problema",
            "O processo de focar apenas nos detalhes importantes de um problema"
        ],
        "resposta_correta": 1
    },
    {
        "pergunta": "Qual é o principal benefício da abstração?",
        "opcoes": [
            "Permite dividir problemas em partes menores",
            "Permite identificar similaridades entre problemas",
            "Permite focar apenas nos detalhes importantes, ignorando informações irrelevantes",
            "Permite criar sequências de passos para resolver problemas"
        ],
        "resposta_correta": 2
    },
    {
        "pergunta": "O que é um algoritmo?",
        "opcoes": [
            "Um tipo de computador",
            "Uma linguagem de programação",
            "Uma sequência finita de instruções bem definidas para resolver um problema",
            "Um método para identificar padrões em dados"
        ],
        "resposta_correta": 2
    },
    {
        "pergunta": "Qual das seguintes afirmações sobre o Pensamento Computacional é FALSA?",
        "opcoes": [
            "É útil apenas para programadores e cientistas da computação",
            "Ajuda a resolver problemas de forma sistemática e lógica",
            "Envolve a identificação de padrões",
            "Inclui a criação de algoritmos"
        ],
        "resposta_correta": 0
    }
]

# Conteúdo para o curso "Segurança Digital para Iniciantes"
CONTEUDO_SEGURANCA_DIGITAL = {
    "topico1": {
        "titulo": "Princípios Básicos de Segurança Digital",
        "conteudo": """A segurança digital refere-se às práticas, tecnologias e políticas projetadas para proteger dispositivos, redes e dados contra acesso não autorizado, uso indevido ou danos.

Princípios fundamentais de segurança digital:

1. Confidencialidade: Garantir que as informações sejam acessíveis apenas para pessoas autorizadas.
2. Integridade: Manter a precisão e completude dos dados, evitando alterações não autorizadas.
3. Disponibilidade: Garantir que os sistemas e dados estejam disponíveis quando necessário.
4. Autenticação: Verificar a identidade de usuários ou sistemas.
5. Autorização: Determinar quais ações um usuário ou sistema pode realizar.

Estes princípios formam a base para práticas de segurança digital eficazes, tanto para indivíduos quanto para organizações."""
    },
    "topico2": {
        "titulo": "Senhas Seguras",
        "conteudo": """Senhas são a primeira linha de defesa para proteger suas contas online. Uma senha forte é essencial para manter seus dados seguros.

Características de uma senha forte:
- Comprimento: No mínimo 12 caracteres
- Complexidade: Combinação de letras maiúsculas e minúsculas, números e símbolos
- Unicidade: Diferente para cada conta
- Não óbvia: Evitar informações pessoais facilmente descobertas

Dicas para gerenciar senhas:
1. Use um gerenciador de senhas para armazenar suas senhas de forma segura
2. Ative a autenticação de dois fatores (2FA) sempre que possível
3. Troque suas senhas regularmente, especialmente após violações de dados
4. Nunca compartilhe suas senhas com outras pessoas
5. Evite anotar senhas em papel ou em arquivos não criptografados

Exemplo de senha fraca: "senha123"
Exemplo de senha forte: "T7%pL9@zX2&qR5!"

Lembre-se: A segurança de suas contas é tão forte quanto sua senha mais fraca."""
    },
    "topico3": {
        "titulo": "Proteção contra Malware",
        "conteudo": """Malware (software malicioso) é qualquer programa ou código projetado para danificar, invadir ou comprometer sistemas. Tipos comuns incluem vírus, worms, trojans, ransomware e spyware.

Como se proteger contra malware:

1. Mantenha seu sistema operacional e aplicativos atualizados
   - As atualizações frequentemente corrigem vulnerabilidades de segurança

2. Use software antivírus/antimalware confiável
   - Mantenha-o atualizado e faça verificações regulares

3. Tenha cuidado ao baixar arquivos
   - Baixe apenas de fontes confiáveis
   - Verifique extensões de arquivo suspeitas (.exe, .bat, .vbs)

4. Seja cauteloso com anexos de e-mail
   - Não abra anexos de remetentes desconhecidos
   - Verifique se o e-mail parece legítimo, mesmo de remetentes conhecidos

5. Use um firewall
   - Bloqueia conexões não autorizadas

6. Faça backup regularmente
   - Em caso de infecção por ransomware, você não perderá seus dados

Sinais de possível infecção por malware:
- Computador lento ou travando com frequência
- Pop-ups estranhos ou anúncios inesperados
- Programas iniciando ou fechando sozinhos
- Arquivos ou configurações alterados sem sua ação"""
    },
    "topico4": {
        "titulo": "Navegação Segura na Internet",
        "conteudo": """A internet oferece inúmeros recursos, mas também apresenta riscos. Adotar práticas de navegação segura é essencial para proteger seus dados e privacidade.

Dicas para navegação segura:

1. Verifique a segurança do site
   - Procure por "https://" e o ícone de cadeado na barra de endereços
   - Sites seguros usam criptografia para proteger dados transmitidos

2. Tenha cuidado com phishing
   - Phishing são tentativas de obter informações sensíveis se passando por entidades confiáveis
   - Verifique o endereço de e-mail do remetente e URLs antes de clicar
   - Desconfie de mensagens urgentes pedindo informações pessoais

3. Use navegação privada ou VPN
   - Navegação privada não salva histórico, cookies ou dados de formulários
   - VPNs (Redes Virtuais Privadas) criptografam sua conexão e ocultam seu IP

4. Gerencie cookies e permissões
   - Revise regularmente as configurações de cookies do seu navegador
   - Conceda permissões (localização, câmera, microfone) apenas quando necessário

5. Evite redes Wi-Fi públicas para atividades sensíveis
   - Se precisar usar, conecte-se através de uma VPN

6. Mantenha seu navegador atualizado
   - Atualizações corrigem vulnerabilidades de segurança

7. Use extensões de segurança
   - Bloqueadores de anúncios e rastreadores podem aumentar sua privacidade"""
    }
}

# Exercícios para o curso "Segurança Digital para Iniciantes"
EXERCICIOS_SEGURANCA_DIGITAL = [
    {
        "pergunta": "Qual dos seguintes NÃO é um princípio fundamental de segurança digital?",
        "opcoes": [
            "Confidencialidade",
            "Integridade",
            "Disponibilidade",
            "Complexidade"
        ],
        "resposta_correta": 3
    },
    {
        "pergunta": "Qual das seguintes senhas é mais segura?",
        "opcoes": [
            "senha123",
            "nomeDaMinhaFilha",
            "12345678",
            "P@55w0rd!2023"
        ],
        "resposta_correta": 3
    },
    {
        "pergunta": "O que é phishing?",
        "opcoes": [
            "Um tipo de vírus que danifica arquivos",
            "Uma técnica para obter informações sensíveis se passando por entidades confiáveis",
            "Um software que bloqueia anúncios",
            "Um método para criptografar dados"
        ],
        "resposta_correta": 1
    },
    {
        "pergunta": "Qual é a melhor maneira de se proteger contra ransomware?",
        "opcoes": [
            "Nunca usar a internet",
            "Usar apenas redes Wi-Fi públicas",
            "Fazer backups regulares dos seus dados",
            "Compartilhar suas senhas com amigos de confiança"
        ],
        "resposta_correta": 2
    },
    {
        "pergunta": "Como você pode identificar se um site é seguro?",
        "opcoes": [
            "Ele tem muitas imagens e cores",
            "O endereço começa com 'https://' e mostra um ícone de cadeado",
            "O site carrega rapidamente",
            "O site tem muitos anúncios"
        ],
        "resposta_correta": 1
    }
]

# Conteúdo para o curso "Introdução ao Python"
CONTEUDO_PYTHON = {
    "topico1": {
        "titulo": "O que é Python",
        "conteudo": """Python é uma linguagem de programação de alto nível, interpretada, de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991.

Características principais do Python:
- Sintaxe clara e legível
- Fácil de aprender e usar
- Multiplataforma (funciona em Windows, Mac, Linux, etc.)
- Grande comunidade e muitas bibliotecas
- Versátil, usada em desenvolvimento web, ciência de dados, automação, IA, etc.

Python é conhecido por sua filosofia de design que enfatiza a legibilidade do código com o uso significativo de espaçamento em branco. Seu lema é "Simples é melhor que complexo".

Por que aprender Python:
1. É uma das linguagens mais populares e em crescimento
2. Tem uma curva de aprendizado suave
3. É amplamente utilizada em áreas emergentes como ciência de dados e IA
4. Oferece excelentes oportunidades de carreira"""
    },
    "topico2": {
        "titulo": "Variáveis e Tipos de Dados",
        "conteudo": """Em Python, variáveis são usadas para armazenar dados que podem ser usados e manipulados em um programa. Python é uma linguagem de tipagem dinâmica, o que significa que você não precisa declarar o tipo de uma variável ao criá-la.

Criando variáveis:
```python
nome = "Maria"
idade = 25
altura = 1.65
```

Principais tipos de dados em Python:

1. Números:
   - Inteiros (int): 1, 2, -5, 1000
   - Ponto flutuante (float): 3.14, -0.001, 2.0

2. Texto:
   - Strings (str): "Olá", 'Python', \"\"\"Texto de múltiplas linhas\"\"\"

3. Booleanos:
   - bool: True, False

4. Coleções:
   - Listas (list): [1, 2, 3], ["a", "b", "c"]
   - Tuplas (tuple): (1, 2, 3), ("a", "b", "c")
   - Dicionários (dict): {"nome": "João", "idade": 30}
   - Conjuntos (set): {1, 2, 3}

Verificando o tipo de uma variável:
```python
x = 10
print(type(x))  # Saída: <class 'int'>
```

Conversão entre tipos:
```python
# Convertendo string para inteiro
numero_str = "10"
numero_int = int(numero_str)

# Convertendo inteiro para string
idade = 25
idade_str = str(idade)
```

Python também permite atribuição múltipla:
```python
x, y, z = 1, 2, 3
```

Lembre-se: em Python, as variáveis são referências a objetos na memória, não "caixas" que contêm valores."""
    },
    "topico3": {
        "titulo": "Entrada e Saída Básicas",
        "conteudo": """A interação com o usuário é uma parte fundamental da programação. Em Python, podemos facilmente obter entrada do usuário e exibir saída.

**Função print() - Exibindo informações**

A função `print()` é usada para exibir texto ou valores de variáveis na tela:

```python
print("Olá, mundo!")

nome = "Ana"
idade = 30
print("Nome:", nome, "Idade:", idade)
```

Formatando strings com f-strings (Python 3.6+):
```python
nome = "Carlos"
idade = 25
print(f"Olá, meu nome é {nome} e tenho {idade} anos.")
```

Outros métodos de formatação:
```python
# Método format()
print("Olá, meu nome é {} e tenho {} anos.".format(nome, idade))

# Formatação antiga com %
print("Olá, meu nome é %s e tenho %d anos." % (nome, idade))
```

**Função input() - Obtendo entrada do usuário**

A função `input()` permite que o programa receba dados do usuário:

```python
nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")
```

A função `input()` sempre retorna uma string. Se você precisar de um número, deve converter o valor:

```python
# Convertendo para inteiro
idade = int(input("Digite sua idade: "))
print(f"Daqui a 5 anos você terá {idade + 5} anos.")

# Convertendo para float
altura = float(input("Digite sua altura em metros: "))
print(f"Sua altura é {altura} metros.")
```

Tratando erros de entrada:
```python
try:
    numero = int(input("Digite um número: "))
    print(f"O dobro de {numero} é {numero * 2}")
except ValueError:
    print("Entrada inválida. Por favor, digite um número.")
```

Estas funções básicas de entrada e saída são fundamentais para criar programas interativos em Python."""
    },
    "topico4": {
        "titulo": "Estruturas Condicionais",
        "conteudo": """Estruturas condicionais permitem que seu programa tome decisões baseadas em condições. Em Python, usamos principalmente as instruções `if`, `elif` e `else`.

**Instrução if**

A estrutura básica de uma condição `if`:

```python
if condição:
    # código a ser executado se a condição for verdadeira
```

Exemplo:
```python
idade = 18
if idade >= 18:
    print("Você é maior de idade.")
```

**Instrução if-else**

Para executar um código alternativo quando a condição for falsa:

```python
if condição:
    # código a ser executado se a condição for verdadeira
else:
    # código a ser executado se a condição for falsa
```

Exemplo:
```python
idade = 16
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
```

**Instrução if-elif-else**

Para verificar múltiplas condições:

```python
if condição1:
    # código a ser executado se condição1 for verdadeira
elif condição2:
    # código a ser executado se condição1 for falsa e condição2 for verdadeira
else:
    # código a ser executado se todas as condições anteriores forem falsas
```

Exemplo:
```python
nota = 85
if nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
elif nota >= 70:
    print("C")
elif nota >= 60:
    print("D")
else:
    print("F")
```

**Operadores de comparação**

- `==`: igual a
- `!=`: diferente de
- `>`: maior que
- `<`: menor que
- `>=`: maior ou igual a
- `<=`: menor ou igual a

**Operadores lógicos**

- `and`: ambas as condições devem ser verdadeiras
- `or`: pelo menos uma condição deve ser verdadeira
- `not`: inverte o valor da condição

Exemplo com operadores lógicos:
```python
idade = 25
tem_carteira = True

if idade >= 18 and tem_carteira:
    print("Pode dirigir.")
elif idade >= 18 and not tem_carteira:
    print("Precisa tirar a carteira de motorista.")
else:
    print("Não pode dirigir.")
```

**Condições aninhadas**

Você pode ter condições dentro de outras condições:

```python
temperatura = 28
if temperatura > 30:
    print("Está muito quente!")
    if temperatura > 40:
        print("Perigo de insolação!")
elif temperatura > 20:
    print("Está agradável.")
else:
    print("Está frio.")
```

As estruturas condicionais são fundamentais para criar programas que tomam decisões baseadas em diferentes situações."""
    },
    "topico5": {
        "titulo": "Estruturas de Repetição",
        "conteudo": """Estruturas de repetição (loops) permitem executar um bloco de código várias vezes. Python oferece principalmente dois tipos de loops: `for` e `while`.

**Loop for**

O loop `for` é usado para iterar sobre uma sequência (como lista, tupla, dicionário, conjunto ou string):

```python
for item in sequência:
    # código a ser executado para cada item
```

Exemplos:

Iterando sobre uma lista:
```python
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)
```

Iterando sobre uma string:
```python
nome = "Python"
for letra in nome:
    print(letra)
```

Usando a função `range()`:
```python
# range(5) gera números de 0 a 4
for i in range(5):
    print(i)

# range(2, 8) gera números de 2 a 7
for i in range(2, 8):
    print(i)

# range(1, 10, 2) gera números de 1 a 9, pulando de 2 em 2
for i in range(1, 10, 2):
    print(i)
```

**Loop while**

O loop `while` executa um bloco de código enquanto uma condição for verdadeira:

```python
while condição:
    # código a ser executado enquanto a condição for verdadeira
```

Exemplo:
```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

**Controle de loops**

- `break`: sai completamente do loop
- `continue`: pula para a próxima iteração do loop
- `else`: bloco executado quando o loop termina normalmente (sem break)

Exemplos:

Usando `break`:
```python
for i in range(10):
    if i == 5:
        break
    print(i)  # Imprime 0, 1, 2, 3, 4
```

Usando `continue`:
```python
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # Imprime apenas números ímpares: 1, 3, 5, 7, 9
```

Usando `else`:
```python
for i in range(5):
    print(i)
else:
    print("Loop concluído!")
```

**Loops aninhados**

Você pode ter um loop dentro de outro:

```python
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")
```

**Compreensão de lista**

Uma forma concisa de criar listas baseadas em loops:

```python
# Cria uma lista com os quadrados dos números de 0 a 9
quadrados = [x**2 for x in range(10)]
print(quadrados)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Com condição
pares = [x for x in range(20) if x % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

As estruturas de repetição são essenciais para automatizar tarefas repetitivas e processar coleções de dados em Python."""
    }
}

# Exercícios para o curso "Introdução ao Python"
EXERCICIOS_PYTHON = [
    {
        "pergunta": "Qual função é usada para obter entrada do usuário em Python?",
        "opcoes": [
            "get()",
            "input()",
            "read()",
            "scanf()"
        ],
        "resposta_correta": 1
    },
    {
        "pergunta": "Como você imprime a mensagem 'Olá, mundo!' em Python?",
        "opcoes": [
            "console.log('Olá, mundo!')",
            "echo 'Olá, mundo!'",
            "print('Olá, mundo!')",
            "System.out.println('Olá, mundo!')"
        ],
        "resposta_correta": 2
    },
    {
        "pergunta": "Qual é o resultado da expressão 3 * 2 ** 2 em Python?",
        "opcoes": [
            "12",
            "36",
            "9",
            "6"
        ],
        "resposta_correta": 0
    },
    {
        "pergunta": "Qual das seguintes opções é uma estrutura de repetição em Python?",
        "opcoes": [
            "if-else",
            "for",
            "switch",
            "try-except"
        ],
        "resposta_correta": 1
    },
    {
        "pergunta": "Como você define uma variável em Python?",
        "opcoes": [
            "var nome = 'João'",
            "let nome = 'João'",
            "nome = 'João'",
            "string nome = 'João'"
        ],
        "resposta_correta": 2
    }
]

# Mapeamento de cursos para conteúdos e exercícios
MAPEAMENTO_CURSOS = {
    "1": {
        "conteudo": CONTEUDO_PENSAMENTO_COMPUTACIONAL,
        "exercicios": EXERCICIOS_PENSAMENTO_COMPUTACIONAL
    },
    "2": {
        "conteudo": CONTEUDO_SEGURANCA_DIGITAL,
        "exercicios": EXERCICIOS_SEGURANCA_DIGITAL
    },
    "3": {
        "conteudo": CONTEUDO_PYTHON,
        "exercicios": EXERCICIOS_PYTHON
    }
}
