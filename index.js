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


var express = require('express');
var app = express();
app.listen(3000, function () {
    console.log('server running on port 3000');
})
app.get('/name', callName);

var nome = 'Kaic Murilo Nunes';
var cargo = 'Dev';
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
