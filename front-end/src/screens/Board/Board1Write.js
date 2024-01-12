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

const Board1Write = () => {
  const name = 'jinwon97'
  const [text, setText] = useState({ title: '', contents: '' });

  const handleFileUpload = () => {
    // Implement file upload functionality here
    console.log('File upload functionality to be implemented.');
  };

  //파일 업로드 관련 통신

  // const handleFileUpload = (e) => {
  //   const file = e.target.files[0];
  //   const formData = new FormData();
  //   formData.append('file', file);

  // axios.post("http://subdomain.storeaivle.com/board/postlist/uploadfile", formData)
  //   .then(function (response) {
  //     console.log(response);
  //     setUploadedFileName(response.data.filename);  // 서버에서 파일 이름을 받아옴
  //   })
  //   .catch(function (error) {
  //     console.log(error);
  //   });
  // };

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
    <Box sx={{ height: '100%', mt: 5, mb: 5, width: 'fit-content' }}>
        <span style={{fontSize : 30, fontWeight : 'bold', color : '#012A5B'}}>창업 정보</span>
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
            id='board1Contents'
            label='Contents'
            name='board1Contents'
            value={text.contents}
            onChange={(e) => setText((prevText) => ({ ...prevText, contents: e.target.value }))}
          />
        </div>
        <p></p>
        <div style={{ display: 'flex', justifyContent: 'flex-end', width: '100%', marginBottom : 20 }}>
          <Button variant="contained" sx={{ mr: 2 }} href='/board1' onClick={handleTextInput}>
            글쓰기
          </Button>
          <Button variant="contained" href="/Board1">
            취소
          </Button>
        </div>
      </div>
    </div>
  );
};

export default Board1Write;