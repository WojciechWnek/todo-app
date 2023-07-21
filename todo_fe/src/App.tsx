import { useEffect, useState } from 'react';
import reactLogo from './assets/react.svg';
import viteLogo from '/vite.svg';
import './App.css';
import axios from 'axios';
import { TaskCard } from './components/TaskCard/TaskCard';

interface ITasks {
  createdAt: string;
  description: string;
  done: boolean;
  editedAt: string;
  id: number;
  title: string;
}

function App() {
  const [count, setCount] = useState(0);
  const [tasks, setTasks] = useState<ITasks[]>([]);

  const getTasks = async () => {
    try {
      const response = await axios.get('http://localhost:8000/tasks/');
      console.log(response.data);
      setTasks(response.data as ITasks[]);
    } catch {
      console.log('error');
    }
  };

  const getTask = (id: number) => {
    void (async () => {
      try {
        const data = await axios.get(`http://localhost:8000/tasks/${id}/`);
        console.log(data);
      } catch {
        console.log('error');
      }
    })();
  };

  useEffect(() => {
    void (async () => {
      await getTasks();
    })();
  }, []);

  return (
    <>
      {tasks.map((task) => (
        <TaskCard
          key={task.id}
          id={task.id}
          done={task.done}
          description={task.description}
          createdAt={task.createdAt}
          editedAt={task.editedAt}
          title={task.title}
        />
      ))}
    </>
  );
}

export default App;
