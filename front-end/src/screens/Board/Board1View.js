import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { Box, Button, Paper, Typography, Divider, TextField } from '@mui/material';
import axios from 'axios';
import DivLine from '../../components/Styles/DivLine';

const Board1View = () => {
  const name = 'tester1'
  const [comment, setComment] = useState({contents : ''});
  const [comments, setComments] = useState([]);
  const { post_num } = useParams();
  const navigate = useNavigate();
  const [boardContent, setBoardContent] = useState({}); // Change to object

  function getBoardContent() {
    axios.get(`http://43.202.42.122/board/postlist/${post_num}`)
      .then((response) => {
        setBoardContent(response.data); // Update state with fetched data
        console.log(response.data);
      })
      .catch(function (error) {
        console.log(error);
      });
  }

  function getcomment() {
    axios.get(`http://127.0.0.1:8000/board/postlist/${post_num}/comment`)
      .then((response) => {
        setComments(response.data); // Update state with fetched data
        console.log(response.data);
      })
      .catch(function (error) {
        console.log(error);
      });
  }

  useEffect(() => {
    getBoardContent();
    getcomment();
  }, [post_num]); // Include post_num as a dependency

  const handleCommentInput = () => {
    console.log(comment)
    const {contents} = comment;
    axios.post(`http://127.0.0.1:8000/board/postlist/${post_num}/createcomment`, {
      contents,
      name,
    })
      .then(function (response) {
        console.log(response);
        // Consider using a redirect method here
        navigate(`/Board1View/${post_num}`)
      })
      .catch(function (error) {
        console.log(error);
      });
  };

  const handleCommentDelete = (commentId) => {
    axios.delete(`http://127.0.0.1:8000/board/postlist/deletecomment/${commentId}`)
      .then((response) => {
        console.log(response.data);
        // 삭제 성공 시 리다이렉트 또는 필요한 동작 수행
        navigate('/Board1');
      })
      .catch((error) => {
        console.error(error);
        // 오류 발생 시 처리
      });
  };

  const handleDelete = () => {
    axios.delete(`http://127.0.0.1:8000/board/postlist/${post_num}/deletepost`)
      .then((response) => {
        console.log(response.data);
        // 삭제 성공 시 리다이렉트 또는 필요한 동작 수행
        navigate('/Board1');
      })
      .catch((error) => {
        console.error(error);
        // 오류 발생 시 처리
      });
  };

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
      <Box sx={{ display: 'flex', justifyContent: 'flex-end' }}>
        <Button variant="contained" href={`/Board1Mod/${post_num}`} sx={{ mb: 2, mr : 2 }}>
          글 수정
        </Button>
        <Button variant="contained" onClick={handleDelete} sx={{ mb: 2, mr: 2 }}>
          글 삭제
        </Button>
        <Button variant="contained" href="/Board1" sx={{ mb: 2 }}>
          글 목록
        </Button>
      </Box>
      <DivLine />
      <Paper elevation={3} sx={{ p: 3, mt: 3 }}>
      <Typography variant="h4" sx={{ mb: 2 }}>
        Comment
      </Typography>
      <DivLine />
      {comments.map((c) => (
        <div key={c.comment_id}>
        <Typography variant="body1" fontSize={15} sx={{ mb: 3, display: 'flex', justifyContent: 'space-between' }}>
          <span>ㄴ {c.contents}</span>
          <span>{c.name} {c.date} 
            <Button size='small' onClick={() => handleCommentDelete(c.comment_id)} href={`/Board1View/${post_num}`} sx={{ ml: 1 }}>
              X
            </Button>
          </span>
        </Typography>
      </div>
      ))}
      <TextField
        fullWidth
        multiline
        rows={4}
        label="Add a comment"
        value={comment.contents}
        sx={{ mb: 2 }}
        onChange={(e) => setComment((prevText) => ({ ...prevText, contents: e.target.value }))}
      />
      <Button  variant="contained" onClick={handleCommentInput} href={`/Board1View/${post_num}` }>
        댓글 달기
      </Button>
    </Paper>

      </Box>
    </>
  );
};

export default Board1View;