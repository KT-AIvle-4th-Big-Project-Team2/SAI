import React, { useState, useEffect } from 'react';
import { Paper, Typography, TextField, Button } from '@mui/material';
import axios from 'axios';

const Comment1 = () => {
  const [comment, setComment] = useState('');
  const [comments, setComments] = useState([]);
  const [post_num, setPost_num] = useState('');

  const handleCommentChange = (e) => {
    setComment(e.target.value);
  };

  const handleAddComment = () => {
    if (comment.trim() !== '') {
      setComments([...comments, comment]);
      setComment('');
    }
  };

  
    function getcomment() {
      axios.get(`http://127.0.0.1:8000/board/postlist/${post_num}/comment`)
        .then((response) => {
          setComments(response.data); // Update state with fetched data
          console.log(response.data);
        })
        .catch(function (error) {
          console.log(error);
        });
    }
    useEffect(() => {
      getcomment();
    }, [post_num]); // Include post_num as a dependency
  

  return (
    <Paper elevation={3} sx={{ p: 3, mt: 3 }}>
      <Typography variant="h6" sx={{ mb: 2 }}>
        Comment
      </Typography>
      {comments.map((c, index) => (
        <Typography key={index} variant="body1" sx={{ mb: 1 }}>
          {c}
        </Typography>
      ))}
      <TextField
        fullWidth
        multiline
        rows={4}
        label="Add a comment"
        value={comment}
        onChange={handleCommentChange}
        sx={{ mb: 2 }}
      />
      <Button variant="contained" onClick={handleAddComment}>
        Add Comment
      </Button>
    </Paper>
  );
};

export default Comment1;