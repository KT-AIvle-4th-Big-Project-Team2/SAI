import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
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

const Board2Mod = () => {
  const [text, setText] = useState({ title: '', content: '' });
  const { post_num } = useParams();
  const [boardContent, setBoardContent] = useState({});

  const handleFileUpload = () => {
    // Implement file upload functionality here
    console.log('File upload functionality to be implemented.');
  };

  const handleTextInput = () => {
    const { title, content } = text;

    // Make a PATCH request to update the post with the modified data
    axios.patch(`http://subdomain.storeaivle.com/board2/postlist/${post_num}`, {
      title,
      content,
    })
    .then((response) => {
      console.log(response.data);
      // Handle success, redirect, or show a success message
    })
    .catch((error) => {
      console.error(error);
      // Handle error, show an error message, etc.
    });
  };

  useEffect(() => {
    // Fetch existing post content when the component mounts
    axios.get(`http://subdomain.storeaivle.com/board2/postlist/${post_num}`)
      .then((response) => {
        setBoardContent(response.data);
        setText({
          title: response.data.title,
          content: response.data.content,
        });
      })
      .catch((error) => {
        console.error(error);
      });
  }, [post_num]);

  return (
    <div className="container">
      <Box sx={{ height: '100%', mt: 3, mb: 3, width: 'fit-content' }}>
        <h2>창업 게시판 수정</h2>
      </Box>
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', width: '100%' }}>
          <Button component="label" variant="contained" startIcon={<CloudUploadIcon />} onClick={handleFileUpload}>
            Upload file
            {/* ... (VisuallyHiddenInput remains the same) */}
          </Button>
        </div>
        <p></p>
        <div style={{ width: '100%', marginBottom: '10px' }}>
          <TextField
            fullWidth
            id='board2Title'
            label='Title'
            name='board2Title'
            value={text.title}
            onChange={(e) => setText((prevText) => ({ ...prevText, title: e.target.value }))}
          />
        </div>
        <div style={{ width: '100%', marginBottom: '10px' }}>
          <TextField
            fullWidth
            multiline
            rows={20}
            id='board2Content'
            label='Content'
            name='board2Content'
            value={text.content}
            onChange={(e) => setText((prevText) => ({ ...prevText, content: e.target.value }))}
          />
        </div>
        <p></p>
        <div style={{ display: 'flex', justifyContent: 'flex-end', width: '100%' }}>
          <Link to='/Board2'>
            <Button variant="contained" sx={{ mr: 2 }} onClick={handleTextInput}>
              수정
            </Button>
          </Link>
          <Button variant="contained" href="/Board2">
            취소
          </Button>
        </div>
      </div>
    </div>
  )
}

export default Board2Mod