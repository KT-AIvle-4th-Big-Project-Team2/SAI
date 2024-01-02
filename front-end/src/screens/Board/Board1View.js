import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { Box, Button, Paper, Typography, Divider, Link } from '@mui/material';
import axios from 'axios';
import DivLine from '../../components/Styles/DivLine';

const Board1View = () => {
  const { post_num } = useParams();
  const [boardContent, setBoardContent] = useState({}); // Change to object

  function getBoardContent() {
    axios.get(`http://127.0.0.1:8000/board/postlist/${post_num}`)
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

  return (
    <>
    <Box sx={{ p: 2, height: '100%' }}>
      <Typography variant="h4" sx={{ mb: 2 }}>
        게시판
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

      <Button variant="contained" href="/Board" sx={{ mb: 2 }}>
        글 목록
      </Button>
      <DivLine />

      <Paper elevation={3} sx={{ p: 3, mt: 3 }}>
        <Typography variant="h6" sx={{ mb: 2 }}>
          Comment
        </Typography>
        {/* Add your comment components here */}
      </Paper>
      </Box>
    </>
  );
};

export default Board1View;