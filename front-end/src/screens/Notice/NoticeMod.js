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

const NoticeMod = () => {
  const [text, setText] = useState({ title: '', content: '' });
  const { post_num } = useParams();
  const [NoticeContent, setNoticeContent] = useState({});

  const handleTextInput = () => {
    const { title, content } = text;

    // Make a PATCH request to update the post with the modified data
    axios.patch(`http://127.0.0.1:8000/board1/postlist/${post_num}`, {
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
    axios.get(`http://127.0.0.1:8000/board1/postlist/${post_num}`)
      .then((response) => {
        setNoticeContent(response.data);
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
    <>
      <Box sx={{ height: '100%', mt: 3, mb: 3, width: 'fit-content' }}>
        <h2>창업 정보</h2>
      </Box>
        <p></p>
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
            rows={20}
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
              수정
            </Button>
          </Link>
          <Button variant="contained" href="/Notice">
            취소
          </Button>
        </div>
    </>
  )
}

export default NoticeMod