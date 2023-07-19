import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import axios from 'axios'

function App() {
  const [count, setCount] = useState(0)

  const getTasks = async () => {
    try{

    const data = await axios.get("http://localhost:8000/tasks")
    console.log(data);
  }catch{
    console.log("error");
  }
  }

  const getTask = async (id: number) => {
    try{
      const data = await axios.get(`http://localhost:8000/tasks/${id}`)
      console.log(data);
    }catch{
      console.log("error");
    }
  }

  useEffect( () => {
    void (async () => {
        await getTasks();
    })();
  },[])

  return (
    <>
      <div>
        <a href="https://vitejs.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={async () => {
            await getTask(count);
            setCount((count) => count + 1);
        }}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.tsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
