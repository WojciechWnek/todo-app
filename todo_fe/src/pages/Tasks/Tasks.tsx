import { useEffect, useState } from 'react';
import axios from 'axios';
import { TaskCard } from '../../components/TaskCard/TaskCard';
import {
  Button,
  Dialog,
  DialogActions,
  DialogContent,
  DialogTitle,
  TextField,
} from '@mui/material';

interface ITasks {
  createdAt: string;
  description: string;
  done: boolean;
  editedAt: string;
  id: number;
  title: string;
}

function App() {
  const [tasks, setTasks] = useState<ITasks[]>([]);
  const [open, setOpen] = useState(false);
  const [titleValue, setTitleValue] = useState('');
  const [descriptionValue, setDescriptionValue] = useState('');

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  const addTask = () => {
    void (async () => {
      try {
        await axios.post('http://localhost:8000/tasks/', {
          title: titleValue,
          description: descriptionValue,
          done: false,
        });
        getTasks();
        handleClose();
        setTitleValue('');
        setDescriptionValue('');
      } catch {
        console.log('error');
      }
    })();
  };

  const getTasks = () => {
    void (async () => {
      try {
        const response = await axios.get('http://localhost:8000/tasks/');
        setTasks(response.data as ITasks[]);
      } catch {
        console.log('error');
      }
    })();
  };

  useEffect(() => {
    getTasks();
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
          getTasks={getTasks}
        />
      ))}
      <Button variant="contained" onClick={handleClickOpen} sx={{ marginTop: 4 }}>
        Add Task
      </Button>
      <Dialog open={open} onClose={handleClose}>
        <DialogTitle>Add new task</DialogTitle>
        <DialogContent>
          <TextField
            autoFocus
            margin="dense"
            id="title"
            label="Title"
            type="text"
            fullWidth
            variant="standard"
            value={titleValue}
            onChange={(e) => {
              console.log(e.currentTarget);
              setTitleValue(e.currentTarget.value as string);
            }}
          />
          <TextField
            autoFocus
            margin="dense"
            id="description"
            label="Description"
            type="text"
            fullWidth
            variant="standard"
            value={descriptionValue}
            onChange={(e) => {
              console.log(e.currentTarget);
              setDescriptionValue(e.currentTarget.value as string);
            }}
          />
        </DialogContent>
        <DialogActions>
          <Button onClick={handleClose}>Cancel</Button>
          <Button onClick={() => addTask()}>Add</Button>
        </DialogActions>
      </Dialog>
    </>
  );
}

export default App;
