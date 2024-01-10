import React, { useState } from 'react';
import { styled } from '@mui/system';
import { Button, TextField, Box, Link } from '@mui/material';
import CloudUploadIcon from '@mui/icons-material/CloudUpload';
import axios from 'axios';
import DivLine from '../../components/Styles/DivLine';

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

const Board1Write = () => {
  const name = 'jinwon97'
  const [text, setText] = useState({ title: '', contents: '' });

  const handleFileUpload = () => {
    // Implement file upload functionality here
    console.log('File upload functionality to be implemented.');
  };

  const handleTextInput = () => {
    const { title, contents } = text;
    console.log("이름",name);
    axios.post("http://subdomain.storeaivle.com/board/postlist/createpost", {
      
      title:title,
      contents:contents,
      user:9,
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
    <div className="container">
      <Box sx={{ height: '100%', mt: 3, mb: 3, width: 'fit-content' }}>
        <h2>창업 정보</h2>
      </Box>
      <DivLine />
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
            id='board1Contents'
            label='Contents'
            name='board1Contents'
            value={text.contents}
            onChange={(e) => setText((prevText) => ({ ...prevText, contents: e.target.value }))}
          />
        </div>
        <p></p>
        <div style={{ display: 'flex', justifyContent: 'flex-end', width: '100%' }}>
            <Button variant="contained" sx={{ mr: 2 }}  onClick={handleTextInput}>
              글쓰기
            </Button>
          <Button variant="contained" href="/Board">
            취소
          </Button>
        </div>
      </div>
    </div>
  );
};

export default Board1Write;