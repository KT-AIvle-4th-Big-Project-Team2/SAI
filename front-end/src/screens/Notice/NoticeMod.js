import React, { useState, useEffect } from 'react';
import { useParams, Link, useNavigate } from 'react-router-dom';
import { Button, TextField, Box } from '@mui/material';
import CloudUploadIcon from '@mui/icons-material/CloudUpload';
import axios from 'axios';

const NoticeMod = () => {
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
      .patch(`http://subdomain.storeaivle.com/announcements/announcementlist/updatepost/${post_num}`, {
        title,
        contents,
        name,
      })
      .then((response) => {
        console.log(response.data);
        // 성공적으로 업데이트된 경우 페이지 이동
        navigate('/Notice');
      })
      .catch((error) => {
        console.error(error);
        // 오류 발생 시 처리
      });
  };

  useEffect(() => {
    axios
      .get(`http://subdomain.storeaivle.com/announcements/announcementlist/${post_num}`)
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
          <span style={{fontSize : 30, fontWeight : 'bold', color : '#012A5B'}}>공지사항</span>
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
          <Button variant="contained" sx={{ mr: 2 }} onClick={handleTextInput}>
            수정
          </Button>
            <Button href='/Notice' variant="contained">
              취소
            </Button>
        </div>
      </div>
    </div>
  );
};

export default NoticeMod;