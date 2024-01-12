import React, { useState, useEffect } from 'react';
import { styled } from '@mui/system';
import { useParams, useNavigate } from 'react-router-dom';
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


// 창업 정보 게시판 글 수정

const Board1Mod = () => {
  const [text, setText] = useState({ title: '', contents: '' });
  const { post_num } = useParams();
  const [boardContent, setBoardContent] = useState({});
  const navigate = useNavigate();
  const name = 'jinwon97'
  const [uploadedFileName, setUploadedFileName] = useState('');

  // 파일 업로드 관련 로직

  const handleFileUpload = (e) => {
    const file = e.target.files[0];
    const formData = new FormData();
    formData.append('file', file);

    // axios.post("http://subdomain.storeaivle.com/board/postlist/uploadfile", formData)
    //   .then(function (response) {
    //     console.log(response);
    //     setUploadedFileName(response.data.filename);  // 서버에서 파일 이름을 받아옴
    //   })
    //   .catch(function (error) {
    //     console.log(error);
    //   });
  };

  const handleTextInput = () => {
    const { title, content } = text;

    axios.patch(`http://subdomain.storeaivle.com/board/postlist/${post_num}`, {
      title,
      name,
      content,
    })
    .then((response) => {
      console.log(response.data);
    })
    .catch((error) => {
      console.error(error);
    });
  };

  // 기존 글 정보 받아오기

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
            <VisuallyHiddenInput type="file" />
          </Button>
          {uploadedFileName && (
            <div>
              Uploaded File: {uploadedFileName}
            </div>
          )}
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