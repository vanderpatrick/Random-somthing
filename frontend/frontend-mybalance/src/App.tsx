import React, { useEffect, useState } from 'react';
import './App.css';
import axios from 'axios';

// Start making an interface
interface User {
  id: number;
  name: string;
}

interface Bills {
  id: number;
  user_bill_id: number;
  bill_name: string;
  bill_category: string; // Corrected property name
  bill_cost: number;
}

function App() {
  const [users, setUsers] = useState<User[]>([]);
  const [bills, setBills] = useState<Bills[]>([]);

  useEffect(() => {
    const apiUrl = '/users'; // Note the leading slash

    axios
      .get<User[]>(apiUrl)
      .then((res) => {
        setUsers(res.data);
        console.log(res.data); // Log the user data
      })
      .catch((err) => {
        console.error('Error fetching the data:', err);
      });

    const billFetch = '/bills';
    axios
      .get<Bills[]>(billFetch)
      .then((res) => {
        setBills(res.data);
        console.log(res.data); // Log the bill data
      })
      .catch((err) => {
        console.error('Error loading the bills', err);
      });
  }, []);

  const [formData, setFormData] = useState({
    bill_name: '',
    user_bill_id: 0,
    bill_category: '',
    bill_cost: 0,
  });

  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = event.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = (event: React.FormEvent) => {
  event.preventDefault();

  // Define the endpoint for creating a new bill
  const postNewBill = '/bills/create';


  // Create an object with the data you want to send in the request body
const newBillData = {
  bill_name: formData.bill_name,
  bill_category: formData.bill_category,
  bill_cost: formData.bill_cost,
  user_bill_id: formData.user_bill_id,
};

  // Make the POST request to create a new bill
  axios
    .post<Bills>(postNewBill, newBillData)
    .then((res) => {
      // Handle the response as needed
      console.log('New bill created:', res.data);

      // Optionally, update the bills state to reflect the new bill
      setBills([...bills, res.data]); // Assuming res.data contains the newly created bill
    })
    .catch((err) => {
      console.error('Error creating a new bill:', err);
    });

  console.log('Form data submitted:', formData);

  // Reset the form
  setFormData({
    bill_name: '',
    user_bill_id: 0,
    bill_category: '',
    bill_cost: 0,
  });
};


  return (
    <div className="App">
      {users.map((user) => (
        <li key={user.id}>{user.name}</li>
      ))}
      {bills.map((bill: Bills) => (
        <ul key={bill.id}>
          <li>{bill.bill_category}</li> {/* Corrected property name */}
          <li>{bill.bill_cost}</li>
          <li>{bill.bill_name}</li>
        </ul>
      ))}
      <form onSubmit={handleSubmit}>
        <div>
          <label>Bill Name:</label>
          <input
            type="text"
            name="bill_name"
            value={formData.bill_name}
            onChange={handleInputChange}
          />
        </div>
        <div>
          <label>Bill Category:</label>
          <input
            type="text"
            name="bill_category"
            value={formData.bill_category}
            onChange={handleInputChange}
          />
        </div>
        <div>
          <label>Bill Cost:</label>
          <input
            type="number"
            name="bill_cost"
            value={formData.bill_cost}
            onChange={handleInputChange}
          />
        </div>
        <div>
          <label>user_bill_id</label>
          <input
            type="number"
            name="user_bill_id"
            value={formData.user_bill_id}
            onChange={handleInputChange}
          />
        </div>
        <button type="submit">Add Bill</button>
      </form>
    </div>
  );
}

export default App;
