# Roteiro

## Live de Python básico

### Sobre os objetivos gerais

- O objetivo geral que começamos aqui é aprender a programar em Python e desenvolver uma aplicação web 100% funcional desde o backend até o frontend.
  De modo que possamos auxiliar tanto aqueles que tenham tido alguma dificuldade com o PI quantos os que irão para uma nova etapa do projeto, ou até aqueles que ainda não tiverem nenhum contado com código. E no caso dos não alunos, daqueles que estão aqui para aprender python do zero, também pretendemos que possamos ajudar a comunidade.

### Live 0

- O objetivo desta live é nivelar o conhecimento sobre Python.
  Quem já tem algum conhecimento sobre Python, vou tentar ajudar com duvidas que possam já ter ou que venham a surgir no decorrer da live, então podem interagir comigo pelo chat (Youtube, Twitch ou Discord) e quem não tiver nenhum conhecimento também o importante é não ficarem dúvidas.

- Primeiro histórias, porque eu adora histórias.
- Python foi criado por Guido Van Rossum, um dos fundadores da linguagem, no final de 1989 e publicado em 1991.
- Foi feito com base na linguagem ABC mas possui uma série de recursos inspirados em diversas linguagens como C, Haskell, Perl entre outras.

  - Curiosidade:
    O nome Python teve a sua origem no grupo humorístico britânico Monty Python, embora muitas pessoas façam associação com o réptil do mesmo nome (em português, píton ou pitão).

> Fonte:<https://pt.wikipedia.org/wiki/Python>

### Vamos começar (finalmente)

- Vamos começar pelo site oficial do Python, que é o [Python.org](https://www.python.org/).

### Filosofia

- Sim, vamos falar de filosofia, a filosofia na qual o Python foi pensando.
- A história completa do Python já nós da algumas dicas dessa filosofia. Não essa que eu resumi, mas a que vocês podem encontrar na wikipédia.
- Mas vamos a filosofia e vamos começar a aprender Python, isso mesmo as duas coisas ao mesmo tempo.
- Abram o terminal e acessem o repl do Python.
- Repl é um ambiente de programação que permite que você escreva código Python e executa-o.
- Para isso basta abrir um terminal (em qualquer SO que você estiver) e digitar: python ou python3 ou talvez py no Windows.
- Mas se você não tem o Python instalado... Deveria ter. Mas tudo bem eu vou te ajudar.
- Abra o site do python `python.org` e, click no quadrado amarelho com `>_` e pronto. Agora você está acessando um repl online e pode escrever código Python. Tádah! Falei que iriamos começar pelo site oficial.
- E agora...Filosofia! E código.
- Digitem `import this` e vamos ver o que acontece.
- Primeiro vamos entender o que aconteceu:
  - Quando você digita python no terminal e abre o repl ele te dá um prompt para poder digitar seus comandos, antes de dar o prompt ele te fala a versão do Python que você está executando, qual o ramo dessa compilação, data de release essas coisas.
  - Ele te dá também uma ajuda dizendo coisas que você pode começar digitando, como `help`, mas nós ignoramos ele e corremos para os segredos do Python. Isso mesmo aqui é Top Secret tlg?
  - O `import` é o comando do Python que serve para "importar" alguma coisa para o nosso código, para que possamos usar.
  - Podemos importar várias coisas e essas coisas vamos geralmente chamar de módulos ou bibliotecas.
  - Mas e o `this`? Bem o `this` é um "poema".
  - Agora vocês devem estar bravos comigo por estar misturando programação filosofia e poesia...
  - Mas calma agora eu vou direto ao que importa.
  - Import this é um easter egg do Python, o segredo que eu falei, que exibe alguns preceitos da linguagem, ideias que norteiam tanto o desenvolvimento da linguagem como dos programadores que a usam.
  - Vão por mim, são boas ideias que vale a pena seguir quando programamos em Python.
  - Vou ler algumas e comentar as mais importantes ou complicadas, mas não vamos demorar muito nelas. Então se alguém tiver alguma dúvida pode me perguntar.
    - Leitura do [The Zen of Python](https://pt.wikipedia.org/wiki/Zen_of_Python)
      > Bonito é melhor que feio.
      > Explícito é melhor que implícito.
      > Simples é melhor que complexo.
      > Complexo é melhor que complicado.
      > Linear é melhor do que aninhado.
      > Esparso é melhor que denso.
      > Legibilidade conta.
      > Casos especiais não são especiais o bastante para quebrar as regras.
      > Ainda que praticidade vença a pureza.
      > Erros nunca devem passar silenciosamente.
      > A menos que sejam explicitamente silenciados.
      > Diante da ambiguidade, recuse a tentação de adivinhar.
      > Dever haver um — e preferencialmente apenas um — modo óbvio para fazer algo.
      > Embora esse modo possa não ser óbvio a princípio a menos que você seja holandês.
      > Agora é melhor que nunca.
      > Apesar de que nunca normalmente é melhor do que _exatamente_ agora
      > Se a implementação é difícil de explicar, é uma má ideia
      > Se a implementação é fácil de explicar, pode ser uma boa ideia
      > Namespaces são uma grande ideia — vamos ter mais dessas!
      > _-- Tim Peters_

### Hands on

- Não vamos fazer "Hellow World", porque se eu mostrar como faz um hellow world em Python... Vamos vão ficar descepcionados.

- Vamos voltar ao repl e brincar um pouco com Python;
  - Vamos fazer assim, vou passar um código, vocês executam e eu vou explicar o que aconteceu.
- Primeiro vamos importar o módulo `random` e usar o método `randint` para gerar um número aleatório entre 0 e 10.

  ```python
  import random
  random.randint(0, 10)
  ```

- Tudo mundo executou? Ótimo!
- Importamos a biblioteca `random` que é uma biblioteca que tem métodos para gerar números aleatórios, entre outras coisas.
- Podemos pedir ajuda ao Python digitando `help(random.randint)`.
- O método `randint` é um método da biblioteca `random` que recebe dois parâmetros, o primeiro é o número mínimo e o segundo é o número máximo. E retorna um número aleatório entre eles, incluindo ambos os parâmetros.
- Vamos complicar um pouquinho, vamos atribuir esse valor que geramos a uma váriavel:

  ```python
  numero = random.randint(0, 10)
  ```

- Poxa mas agora não aconteceu nada no terminal, por que séra?
- O repl executa o código que digitamos e mostra a saída ou retorno do último comando, nesse caso o que aconteceu foi que o número gerado foi armazenado na váriavel `numero` e isso não possui uma sáida.
- Vamos exibir esse váriavel

  ```python
  print(numero)
  ```

- "Ah, mas se eu digitar apenas `numero` também tenho o mesmo resultado". Sim e não.
- No repl você vai ter a sáida do valor da váriavel, mas quando estivermos escrevendo código em arquivos `.py` o que acontece é que o Python não mostra a saída do código, pra isso precisamos do print. Então vamos usar o `print` já para conseguir replicar esse código num arquivo posteriormente. Ok?

- Para o próximo exemplo o ideal seria que todos estivessem com o Python instalado. E essa vai ser a única live que vou usar o repl. Mas vamos fazer uma última brincadeira que da para fazer com o repl ou em um arquivo python.
- Digitem o código que eu vou postar

```python
import random

numero_aleatório = random.randint(0, 10)
numero_escolhido = int(input('Escolha um número: '))
```

- Quem estiver no repl vai digitar um número e depois continuar digitando o código

```python
if numero_escolhido == numero_aleatório:
  print('Parabéns você acertou!😁')
else:
  print('Que pena você errou!\N{crying face}')
  print('O número sortiado era {}'.format(numero_aleatório))
```

- Quem estiver no repl já deve ter visto o resultado ou ta nos três pontinhos, mas é só dar um enter e ver se acertou o número aleatório.

- Quem fez num arquivo vai salvar esse arquivo com o nome que quiser, pode ser joguinho.py ou algo assim, mas tem que salvar com a extensão `.py` no final do nome.
- Depoi vai no terminal e vai digitar `python` e o nome do arquivo que você criou. Eu tenho um aqui salvo e vou mostrar aqui.

  - Exemplo: `python joguinho.py`

- Curtiram?
- Mas eu não expliquei o if né?
- Que bom que vocês tão espertos

  - Explicar:

    - `if` avalia uma condição, ou seja, se a condição for verdadeira, o código dentro do if será executado.
    - emoji ctrl + c, ctrl + v
      - Python aceita emojis, MAGIA!
    - `else` é o que acontece se a condição for falsa.
    - emoji '\N{crying face}'
      - Python trabalha com unicodes e pode usar emojis a partir de uma base Unicode.
        > <https://www.unicode.org/Public/UNIDATA/UnicodeData.txt>
    - string formatada

      - Em Python podemos formatar strings com o metodo `format` que é muito útil e há outras formas de formatar strings.
        > <https://docs.python.org/3/library/string.html#format-string-syntax>
      - Exemplo com `f`:

        ```python
        print(f'O número sortiado era {numero_aleatório}')
        ```

    - Só mais um detalhe. Vocês se perguntaram de onde importamos o random?
    - Foi do próprio python, mas ele também é um código Python, podemos chegar no VS Code e em algumas IDE's. Vou mostrar.

### Dúvidas?

...

### Próximos passos

- Avaliar as dúvidas e dificuldades
- Verificar se as pessoas querem aprender mais sobre as nuancias do Python ou ir direto para classes e POO.
