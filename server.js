//day 1

var dataJson 
const fs = require("fs");
const express = require('express');
const app = express()

//use json
app.use(express.json())

//Start program load data from file history
fs.readFile("history.json","utf-8",(err,buf) => {
    if (err) {
        console.log(err)
    }
    const jsonFile = JSON.parse(buf)
    dataJson = Object.values(jsonFile)
})

function saveDataToFile(){
    const testJson = JSON.stringify(dataJson)
    fs.writeFile("history.json",testJson,(err,data) => {
        if(err){
            console.log(`Error : ${err}`)
        }
        else{
            console.log(`saved to file!!`)
        }
    })
}

app.get(`/api/history`,(req,res) => {
    res.json(dataJson)
})

app.post(`/api/history`,(req,res) => {
    dataJson.push(req.body)
    saveDataToFile()
    res.status(201).end()
})

app.listen(3000, () => {
    console.log('Application is running on port 3000')
})


