const mongoose = require('mongoose')

const CureQueueSchema = new mongoose.Schema({
    task: String   
})

const CureQueueModel = mongoose.model("Patient List", CureQueueSchema)
module.exports = CureQueueModel