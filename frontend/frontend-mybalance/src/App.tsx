import './App.css'
import {useState, useEffect} from "react"
import axios from 'axios';


interface UserData {
  id: number
  name:string
  is_patrick: boolean
  balance: number
}

function App() {
  useEffect(() => {
  axios.get('http://127.0.0.1:8000/')
    .then((response) => {
      // Axios automatically parses JSON responses
      console.log(response.data);
    })
    .catch((error) => {
      console.error('Error fetching data:', error);
    });
}, []);
  return (
      <p>starting here </p>
  )
}

export default App
