import React, { useState } from 'react';
import { styled } from '@mui/system';
import { Button, TextField, Box, Link } from '@mui/material';
import CloudUploadIcon from '@mui/icons-material/CloudUpload';
import axios from 'axios';

const VisuallyHiddenInput = styled('input')({
  clip: 'rect(0 0 0 0)',
  clipPath: 'inset(50%)',
  height: 1,
  overflow: 'hidden',
  position: 'absolute',
  bottom: 0,
  left: 0,
  whiteSpace: 'nowrap',
  width: 1,
});

const BoardWrite = () => {
  const [text, setText] = useState({ title: '', content: '' });

  const handleFileUpload = () => {
    // Implement file upload functionality here
    console.log('File upload functionality to be implemented.');
  };

  const handleTextInput = () => {
    const { title, content } = text;

    axios.post("http://127.0.0.1:8000/board/postlist/", {
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
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', width: '100%' }}>
          <Button component="label" variant="contained" startIcon={<CloudUploadIcon />} onClick={handleFileUpload}>
            Upload file
            <VisuallyHiddenInput type="file" />
          </Button>
          {/* Add your picture upload button here */}
        </div>
        <p></p>
        <div style={{ width: '100%', marginBottom: '10px' }}>
          <TextField
            fullWidth
            id='boardTitle'
            label='Title'
            name='boardTitle'
            value={text.title}
            onChange={(e) => setText((prevText) => ({ ...prevText, title: e.target.value }))}
          />
        </div>
        <div style={{ width: '100%', marginBottom: '10px' }}>
          <TextField
            fullWidth
            multiline
            rows={20} // Adjust the number of rows as needed
            id='boardContent'
            label='Content'
            name='boardContent'
            value={text.content}
            onChange={(e) => setText((prevText) => ({ ...prevText, content: e.target.value }))}
          />
        </div>
        <p></p>
        <div style={{ display: 'flex', justifyContent: 'flex-end', width: '100%' }}>
          <Link to='/Board1'>
            <Button variant="contained" sx={{ mr: 2 }} onClick={handleTextInput}>
              글쓰기
            </Button>
          </Link>
          <Button variant="contained" href="/Board">
            취소
          </Button>
        </div>
      </div>
    </>
  );
};

export default BoardWrite;