import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { Box, Button, Paper, Typography, Divider, TextField } from '@mui/material';
import axios from 'axios';
import DivLine from '../../components/Styles/DivLine';

const NoticeView = () => {
  const name = 'tester1'
  const { post_num } = useParams();
  const navigate = useNavigate();
  const [boardContent, setBoardContent] = useState({}); // Change to object

  function getBoardContent() {
    axios.get(`http://subdomain.storeaivle.com/announcements/announcementlist/${post_num}`)
      .then((response) => {
        setBoardContent(response.data); // Update state with fetched data
        console.log(response.data);
      })
      .catch(function (error) {
        console.log(error);
      });
  }

  useEffect(() => {
    getBoardContent();
  }, [post_num]); // Include post_num as a dependency


  const handleDelete = () => {
    axios.delete(`http://subdomain.storeaivle.com/announcements/announcementlist/deletepost/${post_num}`)
      .then((response) => {
        console.log(response.data);
        // 삭제 성공 시 리다이렉트 또는 필요한 동작 수행
        navigate('/notice');
      })
      .catch((error) => {
        console.error(error);
        // 오류 발생 시 처리
      });
  };

  return (
    <div className="container">
    <Box sx={{ p: 2, height: '100%' }}>
      <Typography variant="h4" sx={{ mb: 2 }}>
        공지사항
      </Typography>
      <Divider sx={{ mt: 3, mb: 3 }} />
      <Paper elevation={3} sx={{ p: 3, mb: 3, minHeight: 700 }} key={boardContent.post_id}>
        <Typography variant="h4" >
          {boardContent.length > 0 ? boardContent[0].title || "Loading..." : "Loading..."}
        </Typography>
        <DivLine />
      <Box style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center'}}>
      <Typography variant="h8">
       작성자 : {boardContent.length > 0 ?  boardContent[0].name || "Loading..." : "Loading..."}
          </Typography>
        <Typography variant="h8">
         작성일시 : {boardContent.length > 0 ? boardContent[0].date || "Loading..." : "Loading..."}
        </Typography>
        </Box>
        
        <DivLine />
        <Typography variant="body1" sx={{ height: 'auto' }}>
          {boardContent.length > 0 ? boardContent[0].contents : ""}
        </Typography>
      </Paper>
      <Box sx={{ display: 'flex', justifyContent: 'flex-end' }}>
        <Button variant="contained" href={`/noticeMod/${post_num}`} sx={{ mb: 2, mr : 2 }}>
          글 수정
        </Button>
        <Button variant="contained" onClick={handleDelete} sx={{ mb: 2, mr: 2 }}>
          글 삭제
        </Button>
        <Button variant="contained" href="/notice" sx={{ mb: 2 }}>
          글 목록
        </Button>
      </Box>
      <DivLine />
      </Box>
    </div>
  );
};


export default NoticeView;