const express = require('express')
const mongoose = require('mongoose')
const cors = require('cors')
const CureQueueModel = require('./Models/CureQueue')

const app = express()
app.use(cors())
app.use(express.json())

mongoose.connect('mongodb+srv://CureQueue:Blackathon123!@cluster0.hhqbnua.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

app.get('/get', (req, res) => {
    CureQueueModel.find()
    .then(result => res.json(result))
    .catch(err => res.json(err))
})

app.post('/add', (req, res) => {
    const task = req.body.task;
    CureQueueModel.create({
        task: task
    }).then(result => res.json(result))
    .catch(err => res.json(err))
})

app.listen(3001, () => {
    console.log("Server is Running")
})