import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { Button, TextField, Box } from '@mui/material';
import CloudUploadIcon from '@mui/icons-material/CloudUpload';
import axios from 'axios';

const Board1Mod = () => {
  const [text, setText] = useState({ title: '', contents: '' });
  const { post_num } = useParams();
  const [boardContent, setBoardContent] = useState({});
  const navigate = useNavigate(); // useNavigate 훅 사용

  const handleFileUpload = () => {
    // 파일 업로드 로직을 구현
    console.log('File upload functionality to be implemented.');
  };
  const name = 'Marie85'
  const handleTextInput = () => {
    const { title, contents } = text;

    // PATCH 요청을 통해 수정된 데이터로 업데이트
    axios
      .patch(`http://subdomain.storeaivle.com/board/postlist/${post_num}/updatepost`, {
        title,
        contents,
        name,
      })
      .then((response) => {
        console.log(response.data);
        // 성공적으로 업데이트된 경우 페이지 이동
        navigate('/Board1');
      })
      .catch((error) => {
        console.error(error);
        // 오류 발생 시 처리
      });
  };

  // 수정할 글을 받아온 다음 변수로 설정

  useEffect(() => {
    axios
      .get(`http://subdomain.storeaivle.com/board/postlist/${post_num}`)
      .then((response) => {
        setBoardContent(response.data);
        setText((prevText) => ({
          ...prevText,
          title: response.data[0].title || '',
          contents: response.data[0].contents || '',
        }));
      })
      .catch((error) => {
        console.error('Error fetching data:', error);
      });
  }, [post_num]);
  

  return (
    <div className="container">
    <Box sx={{ height: '100%', mt: 5, mb: 5, width: 'fit-content' }}>
        <span style={{fontSize : 30, fontWeight : 'bold', color : '#012A5B'}}>창업 정보</span>
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
        rows={20}
        id='boardContents'
        name='boardContents'
        value={text.contents}
        onChange={(e) => setText((prevText) => ({ ...prevText, contents: e.target.value }))}
      />
      </div>
        <p></p>
        <div style={{ display: 'flex', justifyContent: 'flex-end', width: '100%', marginBottom : 20 }}>
          <Button variant="contained" sx={{ mr: 2}} onClick={handleTextInput}>
            수정
          </Button>
            <Button href='/Board1' variant="contained">
              취소
            </Button>
        </div>
      </div>
    </div>
  );
};

export default Board1Mod;