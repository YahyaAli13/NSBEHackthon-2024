import React, { useState } from 'react'
import Create from './Create'
import axios from 'axios'

function Home() {
    const [patients, setPatients] = useState([])
    useEffect(() => {
        axios.get('http://localhost:3001/get')
        .then(result => setCureQueue(result.data))
        .catch(err => console.log(err))
    }, [])
  return (
    <div>
        <h1>CureQueue</h1>
        <Create />
        {
            patients.length === 0 
            ?
            <div><h2>No Record</h2></div>
            :
            patients.map(patients =>  (
                <div>
                    {patients.task}
                </div>
            ))
        }
    </div>
  )
}

export default Home