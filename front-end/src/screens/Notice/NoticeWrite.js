import React, { useState } from 'react';
import { styled } from '@mui/system';
import { Button, TextField, Box, Link } from '@mui/material';
import axios from 'axios';


const NoticeWrite = () => {
  const [text, setText] = useState({ title: '', content: '' });


  const handleTextInput = () => {
    const { title, content } = text;

    axios.post("http://127.0.0.1:8000/Notice/postlist/", {
      title,
      content,
    })
      .then(function (response) {
        console.log(response);
        // Consider using a redirect method here
      })
      .catch(function (error) {
        console.log(error);
      });
  };

  return (
    <>
      <Box sx={{ height: '100%', mt: 3, mb: 3, width: 'fit-content' }}>
        <h2>창업 정보</h2>
      </Box>
        <div style={{ width: '100%', marginBottom: '10px' }}>
          <TextField
            fullWidth
            id='NoticeTitle'
            label='Title'
            name='NoticeTitle'
            value={text.title}
            onChange={(e) => setText((prevText) => ({ ...prevText, title: e.target.value }))}
          />
        </div>
        <div style={{ width: '100%', marginBottom: '10px' }}>
          <TextField
            fullWidth
            multiline
            rows={20} // Adjust the number of rows as needed
            id='NoticeContent'
            label='Content'
            name='NoticeContent'
            value={text.content}
            onChange={(e) => setText((prevText) => ({ ...prevText, content: e.target.value }))}
          />
        </div>
        <p></p>
        <div style={{ display: 'flex', justifyContent: 'flex-end', width: '100%' }}>
          <Link to='/Notice'>
            <Button variant="contained" sx={{ mr: 2 }} onClick={handleTextInput}>
              글쓰기
            </Button>
          </Link>
          <Button variant="contained" href="/Notice">
            취소
          </Button>
        </div>
    </>
  );
};

export default NoticeWrite;