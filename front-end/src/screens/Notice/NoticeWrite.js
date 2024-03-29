import React, { useState } from 'react';
import { styled } from '@mui/system';
import { Button, TextField, Box } from '@mui/material';
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

// 공지사항 글 쓰기

const NoticeWrite = () => {

  const name = 'admin'
  const [text, setText] = useState({ title: '', contents: '' });


  // 공지사항 글 쓰기 관련 통신
  const handleTextInput = () => {
    const { title, contents } = text;
    axios.post("http://subdomain.storeaivle.com/announcement/announcementlist/createpost", {
      title,
      name,
      contents,
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
      <Box sx={{ height: '100%', mt: 5, mb: 5, width: 'fit-content' }}>
          <span style={{fontSize : 30, fontWeight : 'bold', color : '#012A5B'}}>공지사항</span>
      </Box>
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
        <p></p>
        <div style={{ width: '100%', marginBottom: '10px' }}>
          <TextField
            fullWidth
            id='noticeTitle'
            label='Title'
            name='noticeTitle'
            value={text.title}
            onChange={(e) => setText((prevText) => ({ ...prevText, title: e.target.value }))}
          />
        </div>
        <div style={{ width: '100%', marginBottom: '10px' }}>
          <TextField
            fullWidth
            multiline
            rows={20} // Adjust the number of rows as needed
            id='noticeContents'
            label='Contents'
            name='noticeContents'
            value={text.contents}
            onChange={(e) => setText((prevText) => ({ ...prevText, contents: e.target.value }))}
          />
        </div>
        <p></p>
        <div style={{ display: 'flex', justifyContent: 'flex-end', width: '100%', marginBottom : 20 }}>
            <Button variant="contained" sx={{ mr: 2 }} href='/notice' onClick={handleTextInput}>
              글쓰기
            </Button>
          <Button variant="contained" href="/notice">
            취소
          </Button>
        </div>
      </div>
    </div>
  );
};

export default NoticeWrite;