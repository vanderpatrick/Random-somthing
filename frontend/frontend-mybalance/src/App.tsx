import './App.css';
import useFetchData from "./components/FetchAPI.tsx";

function App() {
  useFetchData('http://127.0.0.1:8000/');

  return (
    <p>starting here </p>
  );
}

export default App;
