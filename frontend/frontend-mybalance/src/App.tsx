import React, {useEffect, useState} from 'react';
import './App.css';
import axios from 'axios'

//start making an interface
interface  User {
  id: number;
  name: string;
}

function App() {
  const [users, setUsers] = useState<User[]>([]);
  useEffect(() => {
    const apiUrl= '/users'; // Note the leading slash

    axios.get<User[]>(apiUrl)
        .then((res) => {
          setUsers(res.data)
            console.log()
        })
        .catch((err)=> {
          console.error("error fetchind the data:", err)
        })
  }, []);
  return (
    <div className="App">
        {users.map((user) => (
            <li key={user.id}>{user.name}</li>
        ))}
    </div>
  );
}

export default App;
