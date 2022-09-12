const canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");

//Função responsável por adicionar o passo a passo no elemento com id = "step" no HTML
function add_step_by_step(number_list){
    let painel = document.getElementById("step")
    while (painel.childElementCount > 0){
        painel.removeChild(painel.lastChild)
    }
    for(var i = 0; i < number_list.length; i++){
        let div = document.createElement("div")
        let label = document.createElement("label")
        let br = document.createElement("br")
        label.innerText = number_list[i]
        div.appendChild(label)
        div.appendChild(br)
        painel.appendChild(div)
    }
}

//Função responsável por desenhar o gráfico da função no canvas
function drawgraph(number_list){
    canvas.width = 2001
    canvas.height = 2001
    
    // draw axis on canvas:
    ctx.fillStyle = "#000000"
    for(var i = 0; i < 2001; i++){
        ctx.fillRect(i, 1001, 20, 20)
        ctx.fillRect(1001, i, 20, 20)
    }

    ctx.fillStyle = "#f23e02"
    for(var i = 0; i < 2001; i++){
        if (number_list[i] < 0){
            ctx.fillRect(i, ((-number_list[i]) * 100) + 1001, 20, 20);
            console.log(i + " --> " + (((-number_list[i]) * 100)+1001) + " --- " + number_list[i])
        }   else{
            ctx.fillRect(i, (1001 - ((number_list[i]) * 100)), 20, 20);
            console.log(i + " --> " + (1001 - ((number_list[i]) * 100)) + " --- " + number_list[i])
        }
    }
}

//guardar o output do código de python em uma lista.
//Se não tiver x a expressão cada coordenada da lista fica com um passo da resolução da expressão
//Se tiver x cada coordenada da lista fica com um valor de x, sendo a primeira coordenada o valor de x de -10.0 e a ultima o valor de x de 10.0
function python_to_list(string){
    var number_list = []
    if (string.indexOf(",") != -1){
        while (string.indexOf(",") != -1){
            number_list.push(string.substring(0, string.indexOf(",")))
            string = string.substring(string.indexOf(",")+2)
        }
        number_list.push(string.substring(0, string.length))
    }else {
        number_list.push(string.substring(0, string.length))
    }
    return number_list
}

//Função responsável por passar o input do utilizador para o código em python
//Se o input do utilizador tiver "x", chama a função drawgraph para desenhar o gráfico
//Caso contrário apenas coloca o output do código de pythob na GUI
//A função também remove os espaços em branco caso existam
function math_engine_call(){
    var python = require('python-shell')
    var path = require('path')
    const expression = document.querySelector('input').value

    var options = {
        ScriptPath : path.join(__dirname, '/../python/'),
        PythonPath : 'C://Python310//python.exe',
        args : [expression.split(" ").join("")]
    }

    python.PythonShell.run(path.join(__dirname, '/python/calc.py'), options,function(err, message){
        var string = message[0]
        string = string.replace("[", "")
        string = string.replace("]", "")
        while (string.indexOf("'") != -1) {
            string = string.replace("'", "")
        }
        var number_list = []

        //console.log("string -> " + string)
        number_list = python_to_list(string)
        if (expression.indexOf("x") != -1){
            console.log("Graph")
            //console.log(number_list)
            drawgraph(number_list)
        }   else{
            console.log("Not Graph")
            //console.log(number_list)
            document.getElementById('result').innerHTML = number_list[number_list.length - 1]
            add_step_by_step(number_list)
        }
    })
}

//Clicar Enter para fazer a conta:
document.getElementById('input_number').addEventListener("keypress", function(key){
    if (key.key === 'Enter') {
        math_engine_call()
    }
})


/*
//Quando o utilizador escrever qualquer coisa no input a conta é efetuada:
document.getElementById('input_number').addEventListener("keyup", function(key){
    setTimeout(math_engine_call(), 0)
    if (document.getElementById('input_number').value == ""){
        document.getElementById("result").innerText = "----"
    }
})
*/
