import {
  Accordion,
  AccordionDetails,
  AccordionSummary,
  Button,
  Checkbox,
  Grid,
  TextField,
  Typography,
} from '@mui/material';
import axios from 'axios';
import React, { useState } from 'react';

interface ITaskCard {
  createdAt: string;
  description: string;
  done: boolean;
  editedAt: string;
  id: number;
  title: string;
}

export const TaskCard = ({ title, createdAt, description, id, done, editedAt }: ITaskCard) => {
  const [isEditting, setIsEditting] = useState(false);
  const [descriptionValue, setDescriptionValue] = useState<string>(description);
  const [titleValue, setTitleValue] = useState<string>(title);

  const editTask = (id: number) => {
    void (async () => {
      try {
        const data = await axios.put(`http://localhost:8000/tasks/${id}/`, {
          description: descriptionValue,
          title: titleValue,
          createdAt: createdAt,
          done: done,
        });
        console.log(data);
      } catch {
        console.log('error');
      } finally {
        setIsEditting(false);
      }
    })();
  };

  return (
    <Accordion>
      <AccordionSummary aria-controls="panel2a-content" id="panel2a-header">
        <Grid container justifyContent={'space-between'} columnGap={20}>
          <Grid item>
            {!isEditting ? (
              <Typography align="left">{titleValue}</Typography>
            ) : (
              <TextField
                id="standard-multiline-static"
                value={titleValue}
                variant="standard"
                onClick={(e) => e.stopPropagation()}
                onChange={(e) => setTitleValue(e.currentTarget.value)}
              />
            )}
          </Grid>
          <Grid item>
            <Typography align="right">{new Date(createdAt).toLocaleString()}</Typography>
          </Grid>
        </Grid>
      </AccordionSummary>
      <AccordionDetails>
        <Grid container direction="column">
          <Grid item flex={1}>
            {!isEditting ? (
              <Typography align="left">{descriptionValue}</Typography>
            ) : (
              <TextField
                fullWidth
                id="standard-multiline-static"
                multiline
                rows={4}
                value={descriptionValue}
                variant="standard"
                onChange={(e) => setDescriptionValue(e.currentTarget.value)}
              />
            )}
          </Grid>
          <Grid item>
            {!isEditting ? (
              <Button onClick={() => setIsEditting(true)}>Edit</Button>
            ) : (
              <Button onClick={() => editTask(id)}>Save</Button>
            )}
            <Button color="error">Delete</Button>
          </Grid>
        </Grid>
      </AccordionDetails>
    </Accordion>
  );
};
