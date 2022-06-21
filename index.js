// const fs = require('fs');

// var nome = 'Kaic Nunes';
// var funcao = 'Tec';
// var ramal = '3041-8785';

// fs.writeFile('nomeAss.txt', nome + '\n' + funcao + '\n' + ramal, (err) => {
//     if (err) throw err;
//     console.log('O arquivo foi criado!');
// });

// const { spawn } = require("child_process");
// const child = spawn("python", ["main.py"]);
// child.on("exit", (code) => console.log("exitCode:", code));

//importing dependencies
var express = require('express');
var app = express();
var bodyParser=require("body-parser");


//middlewares
app.use(bodyParser.urlencoded({extended:true}));

app.listen(3000, function () {
    console.log('server running on port 3000');
})

//ROTAS
app.get('/name', callName);
app.get("/",function(req,res){
    res.send('rota de envio')
});
  

var nome = 'Joao Teste';
var cargo = 'Deve';
var ramal = '3041-8785';

function callName(req, res) {
    
    var spawn = require("child_process").spawn;
    var process = spawn('python', ["./main.py",
        nome,
        cargo,
        ramal]);
    process.stdout.on('data', function (data) {
        res.send(data.toString());
    })
}
