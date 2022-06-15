var express = require('express');
var app = express();
const fs = require("fs");
  
// Helper function to read and serve html files 
// according to the requested paths 
function readAndServe(path, res) {
    fs.readFile(path, function (err, data) {
        res.end(data);
    })
}
  
// Setting get request path to receive id as query parameter 
app.get('/:id', function (req, res) {
    console.log(req.params);
  
    // Mapping different id's with respective html files
    if (req.params.id == "id1")
        readAndServe("./id1.html", res);
    else if (req.params.id == "id2")
        readAndServe("./id2.html", res);
    else {
        res.end("Invalid request");
    }
});
  
app.listen(8080, () => { console.log("Server Listening on Port 8080") });