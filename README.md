# Calculadora gráfica simples:

- data 📅-> agosto 2022
- numeros de desenvolvedores 😀-> 1
- linguagem e frameworks 🖥->
	- Math engine -> __python 3.10__
	- GUI -> __Javascript, HTML e CSS__
	- Framework -> __Electron, NodeJS 16.16.0__

## Objetivos ✅:
A ideia implusinadora da criação deste código foi a necessidade de uma calculadora minimalisca capaz de efetuar uma representação gráfica de funções matemáticas simples, assim como de efetuar calculos matemáticos e transmitir ao utilizador a resolução passo a passo dos mesmo.

## Como esta organizado o projeto 🗂:
É utilizado o __Electron Framework__ para ser possivél a criação de __desktop apps__ utilizando __Javascript, HTML e CSS__. A janela mostrada ao utilizador nada mais é doque a exibição de uma página __HTML__ decorrada com __CSS__. 

O __Javascript__ é responsável por três papeis:
- Funcionamento dos botões da Tittle Bar;
- Criar e manipular eventos. Por exemplo quando o utilizador pressa __ENTER__ a conta ser calculada ou o gráfico exibido, etc...;
- Passar para o código em __Python__ o valor do input e pegar o output do código em __Python__ e mostrar na interface gráfica.

O código escrito em __Python__ é responsável pelas contas em si. Para que seja possivél a comunicação em __Javascript__ e __Python__ foi utilizado o __python-shell__, modulo do __NodeJS__.

## Como executar o código:
No ficheiro __package.json__ dentro do objeto __"scripts"__ crei uma instrução chamada __"calc"__. 
```json
"scripts": {
	"calc": "electron ."
}
```
Depois disso para executar basta fazer:

	npm run calc

## Sistema de calculo 🧮:
Para a criação do sistema de calculo presente nesta calculadora basieu-me no __CAS -> Computer Algebra System__, presente em várias marcas de calculadoras gráficas e softwares de calculo algebrico, como por exemplo: Texas Instrument, Casio, Microsoft Math Solver, etc...

Basicamente tentei fazer uma cópia á minha maneira desse sistema. Para tal foi utilizado o __Python 3.10 padrão mais o sys__. O sys foi apenas utilizado para identificar o número de bytes de uma estrutura de dados.

### Como funciona o sistema:
São utilizadas árvores binárias 🌳 para fazer o resolução da equação. Para tal é necessário saber quais os sinais e onde se encontram. A procura dos sinais na string é feita do fim da string para o inicio.
A procura de sinais é feita primeiramente fora de funções matemáticas e () e só caso não exista nenhum fora das funções é que a procura é feita dentro das funções ou ().
Primeiro são procurados os sinais de __+, -__ depois os de __*, /, ^__ e finalmente __!__.
__Os números preferêncialmente vão para a esquedra e as expressões para a direita caso não afetar a ordem da expressão.__ Funções matemártica são considerados números mas têm menor prioridade que número como: "5, 4.909, 2, -7.8"

Para mais informação pode ver o seguinte tutorial: https://youtu.be/mB4GZP8YmKU

## Funcionamento do programa 🧑‍💻:
O utilizador escreve a expressão na input box, para efetuar o calculo basta clicar no ENTER. Quaso haja algum x na expressão matemática ela desanha o gráfico 📈. __O gráfico tem o intrevalo [-10.00, 10.00] nos dois eixos.__
Se a expressão tiver algum problema, como por exemplo um parêntices mal posto a calculadora escreve erro no local do resultado. Quando o utilizador coloca o rato por cima da label que contém o resultado é exibido ao utilizador a resuloção passo a passo.

### Operações e funções matemática suportadas ➕ ➖ ➗ ✖️:
- somas -> +
- subtrações -> -
- multiplicações -> *
- divisões -> /
- fatorial -> !
- exponencial -> ^
- modulo -> | |
- parêntices -> ()
- funções trignométricas -> sen(), cos() e tan()
- logaritmos -> ln() e log()

### Imagens que ilustam o programa a funcionar 📷:

## Como são desenhados os gráficos 📈:
Se a string contiver algum __x__, existe um ciclo for no código em Python que vai subestituindo o x por valores começando por -10.00 até 10.00 indo 0.01 em 0.01. Efetua o calculo com o valor de x alterado e guarda esse valor numa lista, no fim imprime a lista e o JavaScipt desanha o gráfico, utilizando essa lista, num canvas.

## Dark mode e Light mode 🔅 🌙:
A calculadora também possuir um mode dark e light. A trocar de modo alterar todas as cores da interface. A trocar entre esse dois modos é feita com uma pequena animação. A troca de modos é feita através de JavaScript, as animações foram programadas em CSS. As imagens em baixo mostram esse dois modos.

## Problemas no código ❌:
O programa possuir algumas falhas:
- Não é possivél fazer calculos com funções trignométricas inversas;
- O logaritmo é sempre logaritmo na base 2;
- A função x^x é mal representada;
- A raiz quadrada não existe em si, para fazer uma raiz quadrado é necessário elevar a base a 0.5, exemplo: raiz(4) -> 4^(0.5);
- As funções trignometricas só conseguem calcular valores até a 7º casa decimal;
- Só é possivél mostrar o gráfico de uma função de cada vez;
- Não é possivél alterar o intrevalo do gráfico;
- Não existe histórico das operações anteriormente realizadas;
- Acho que há zonas do código que estam um pouco complicas e existe alguns if a mais.
- O tema de cores não se mantém depois do utilizador fechar a aplicação, ou seja se o utilizador colocar modo light da próxima vez que voltar a abrir a aplicação ela vai iniciar no modo dark pardão.

## Como fazer se quiser calcular log() de base diferente de 2:
Como mencionado em cima a calculadora não possibelita a troca de base do logaritmo. No entanto da matemática sabemos que:

__log(a,b) = ln(a)/ln(b)__


## Features que não foram implementadas:
Houve várias features que inicialmente foram pensadas mas depois acabaram por não ver a luz do dia🌞. Algumas por serem complicadas de mais e outras por não haver tempo ⌛️ nem recursos humanos suficientes 👨‍💻.

Tinha em mente criar um __histórico de operações__ realizadas, acabei por não implementar pois não sabia como implentar isso na interface sem perder o minimalismo dela.

Tinha em mente implementar alguma forma de o utilizador poder fazer __operações simples com matrizes__. A parte de calculos não era algo muito dificél de ser feita. O problema seria mais uma vez como implementar isso na interface gráfica sem ela perder o minimalismo dela. E como o utilizador poderia escerver uma matriz de tamanho n x n de forma simples.

Outra ideia que não foi possivél ser implementada, era quando o utilizador passar o rato por cima do gráfico, quaso exista algum gráfico representado, o programa mostrava ao utilizador os  __zeros da função, máximo e minimo__ caso existissem.

Também tinha ideias de tornar possivél a __resolução de polimónios de grau n__ na calculadora.

__Representação gráfica de conjuntos.__

Premetir com que o utilizador podesse __resolver equações com incognitas passo a passo__.
