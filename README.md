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
A procura de sinais é feita primeiramente fora de funções matemáticas e (), caso não se encontre nada é que se começa a procurar dentro das funções ou ().
Primeiro são procurados os sinais de __+, -__ depois os de __*, /, ^__ e finalmente __!__.
__Os números preferêncialmente vão para a esquedra e as expressões para a direita caso não afetar a ordem da expressão.__ Funções matemártica são considerados números mas têm menor prioridade que número como: "5, 4.909, 2, -7.8"

As imagens seguintes ilustram melhor a ideia:

<p align="center">
<img src="https://user-images.githubusercontent.com/91985039/187802346-fa25b6cf-8a2a-4850-8fff-762d4160e1db.jpeg" width="60%">
<img src="https://user-images.githubusercontent.com/91985039/187802349-0a613e83-929c-4422-b5c4-915cef2b3c28.jpeg" width="60%">
<img src="https://user-images.githubusercontent.com/91985039/187802353-b536b31a-bc80-400e-97e0-5173e4f4adfb.jpeg" width="60%">
<img src="https://user-images.githubusercontent.com/91985039/187802354-536e1d00-73fc-48ce-8253-378ec8a4082b.jpeg" width="60%">
</p>

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

<table>
  	<tr valign="middle">
		<th>Normal: 🧮</th>	  
		<th>Passo a passo: 👟</th>
	</tr>
	<tr>
		<td valign="middle"><img src="https://user-images.githubusercontent.com/91985039/187807476-8941a2e7-c127-427c-8bf1-34727d42d202.png"></td>
    		<td valign="middle"><img src="https://user-images.githubusercontent.com/91985039/187807478-67c5cab6-715b-4a58-9eee-435571f5bb3d.jpg"></td>
	</tr>
	<tr>
		<td valign="middle"><img src="https://user-images.githubusercontent.com/91985039/187807481-f157eeb8-0dff-496d-ad2e-7632df4267c3.png"></td>
    		<td valign="middle"><img src="https://user-images.githubusercontent.com/91985039/187807482-93f7e4ba-e712-453c-95cd-47e7c361df50.jpg"></td>
	</tr>
	<tr>
		<td valign="middle"><img src="https://user-images.githubusercontent.com/91985039/187807484-2e49f20b-25e6-4035-b6f7-e189505065ae.png"></td>
    		<td valign="middle"><img src="https://user-images.githubusercontent.com/91985039/187807487-90a4fa7c-2911-4fdd-89b7-a8e901878c0a.jpg"></td>
	</tr>
	<tr>
		<td valign="middle"><img src="https://user-images.githubusercontent.com/91985039/187807489-3ef5067e-b40a-40a9-a4f7-fc29914ca8e1.png"></td>
    		<td valign="middle"><img src="https://user-images.githubusercontent.com/91985039/187807490-32ca284b-f24a-4567-ab44-fb05a8542ca5.jpg"></td>
	</tr>
	<tr>
		<td valign="middle"><img src="https://user-images.githubusercontent.com/91985039/187807491-362dd23b-d95a-4190-b86a-d9e333d019e6.png"></td>
    		<td valign="middle"><img src="https://user-images.githubusercontent.com/91985039/187807493-2677c76c-a9f9-4354-b8e6-c8cc78f11af3.jpg"></td>
	</tr>
	<tr>
		<td valign="middle"><img src="https://user-images.githubusercontent.com/91985039/187807495-d6d79c3b-e71d-4b61-98e3-662525d97943.png"></td>
    		<td valign="middle"><img src="https://user-images.githubusercontent.com/91985039/187807496-2d7113c1-f166-46c7-a363-8eb17f345c1a.jpg"></td>
	</tr>
</table>

### Gráficos:

<table>
	<tr>
		<td valign="middle"><img src="https://user-images.githubusercontent.com/91985039/187805545-a6b51dd6-d86e-4e11-bea9-76190db42e9d.png"></td>
    		<td valign="middle"><img src="https://user-images.githubusercontent.com/91985039/187805556-386dade5-41ca-42a5-9c43-f01eee832895.png"></td>
	</tr>
	<tr>
		<td valign="middle"><img src="https://user-images.githubusercontent.com/91985039/187805557-ea533fa3-fe0b-465d-a5fc-55d0c82e7a70.png"></td>
    		<td valign="middle"><img src="https://user-images.githubusercontent.com/91985039/187805558-f22ce032-f432-462b-9d6a-0e7fcf43e079.png"></td>
	</tr>
	<tr>
		<td valign="middle"><img src="https://user-images.githubusercontent.com/91985039/187805560-a39e9fb8-9883-46c9-a411-18c7ebbff9d9.png"></td>
    		<td valign="middle"><img src="https://user-images.githubusercontent.com/91985039/187805562-00d4d023-2c7f-4beb-a3d8-6e80b9601149.png"></td>
	</tr>
	<tr>
		<td valign="middle"><img src="https://user-images.githubusercontent.com/91985039/187805563-e32b3d0f-fc4f-4815-952a-0294b4e5f877.png"></td>
    		<td valign="middle"><img src="https://user-images.githubusercontent.com/91985039/187805566-17f41739-6d44-4a2e-a1ec-77578ceb3ea9.png"></td>
	</tr>
	<tr>
		<td valign="middle"><img src="https://user-images.githubusercontent.com/91985039/187805567-e6f884c4-2db6-452e-a825-375defc1bfae.png"></td>
    		<td valign="middle"><img src="https://user-images.githubusercontent.com/91985039/187805568-303e1156-3dbd-469d-b811-96e014cb999a.png"></td>
	</tr>
</table>

## Como são desenhados os gráficos 📈:
Se a string contiver algum __x__, existe um ciclo for no código em Python que vai subestituindo o x por valores começando por -10.00 até 10.00 indo 0.01 em 0.01. Efetua o calculo com o valor de x alterado e guarda esse valor numa lista, no fim imprime a lista e o JavaScipt desanha o gráfico, utilizando essa lista, num canvas.

## Dark mode e Light mode 🔅 🌙:
A calculadora também possuir um mode dark e light. A trocar de modo alterar todas as cores da interface. A trocar entre esse dois modos é feita com uma pequena animação. A troca de modos é feita através de JavaScript, as animações foram programadas em CSS. As imagens em baixo mostram esse dois modos.

<table>
  <tr valign="middle">
    <th>🌙Dark Mode:</th>
    <th>🔅Light Mode:</th>
  </tr>
  <tr>
    <td valign="middle"><img src="https://user-images.githubusercontent.com/91985039/187801647-387851f0-d275-4bf3-bdd0-402c60d35dcd.png"></td>
    <td valign="middle"><img src="https://user-images.githubusercontent.com/91985039/187801589-ad9baf2d-411e-4704-9eda-da0196ebccb4.png"></td>
  </tr>
  <tr>
    <td valign="middle"><img src="https://user-images.githubusercontent.com/91985039/187801656-cf54f9b1-b878-4969-b612-eb1399129daf.png"></td>
    <td valign="middle"><img src="https://user-images.githubusercontent.com/91985039/187801603-9e3e928e-2724-4fc1-aac4-bc294b4b1ec7.png"></td>
  </tr>
  <tr>
    <td valign="middle"><img src="https://user-images.githubusercontent.com/91985039/187801669-a5b8748d-6294-4d7c-a785-b6261922865b.jpg"></td>
    <td valign="middle"><img src="https://user-images.githubusercontent.com/91985039/187801635-2cd14209-7f53-4e64-bab1-ab35c7f0cddb.jpg"></td>
  </tr>
</table>

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
