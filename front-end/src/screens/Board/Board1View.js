import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { Box, Button, Paper, Typography, Divider, TextField } from '@mui/material';
import axios from 'axios';
import DivLine from '../../components/Styles/DivLine';
// import { useAuth } from '../../components/Auth/AuthContext';

// 창업 정보 게시판 글 자세히 보기

const Board1View = () => {
  const username = 'jinwon97'
  const [comment, setComment] = useState({contents : ''});
  const [comments, setComments] = useState([]);
  const { post_num } = useParams();
  const navigate = useNavigate();
  const [boardContent, setBoardContent] = useState({});
  // const { csrfToken } = useAuth();

  // 게시판 상세 글 받아오기
  function getBoardContent() {
    axios.get(`http://subdomain.storeaivle.com/board/postlist/${post_num}`)
      .then((response) => {
        setBoardContent(response.data);
        console.log(response.data);
      })
      .catch(function (error) {
        console.log(error);
      });
  }

  // 게시판 댓글 받아오기
  function getcomment() {
    axios.get(`http://subdomain.storeaivle.com/board/postlist/${post_num}/comment`)
      .then((response) => {
        setComments(response.data);
        console.log(response.data);
      })
      .catch(function (error) {
        console.log(error);
      });
  }


  // 페이지에 게시판 상세 글과 댓글 작동
  useEffect(() => {
    getBoardContent();
    getcomment();
  }, [post_num]);


  // 댓글 POST 통신
  const handleCommentInput = () => {
    console.log(comment)
    const {contents} = comment;
    axios.post(`http://subdomain.storeaivle.com/board/postlist/${post_num}/createcomment`, {
      contents: contents,
      name: username
    })
      .then(function (response) {
        console.log(response);
        navigate(`/Board1View/${post_num}`)
      })
      .catch(function (error) {
        console.log(error);
      });
  };


  // 댓글 Del 통신
  const handleCommentDelete = (commentId) => {
    axios.delete(`http://subdomain.storeaivle.com/board/postlist/deletecomment/${commentId}`)
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


  // 글 삭제 통신
  const handleDelete = () => {
    axios.delete(`http://subdomain.storeaivle.com/board/postlist/${post_num}/deletepost`)
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
    <div className="container">
    <Box sx={{ p: 2, height: '100%' }}>
    <Box sx={{ height: '100%', mt: 5, mb: 5, width: 'fit-content' }}>
        <span style={{fontSize : 30, fontWeight : 'bold', color : '#012A5B'}}>창업 정보</span>
    </Box>
      <Divider sx={{ mt: 3, mb: 3 }} />
      <Paper elevation={3} sx={{ p: 3, mb: 3, minHeight: 700 }} key={boardContent.post_id}>
        <Typography variant="h4" >
          {boardContent.length > 0 ? boardContent[0].title || "Loading..." : "Loading..."}
        </Typography>
        <DivLine />
      <Box style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center'}}>
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
      {boardContent.length > 0 ? boardContent[0].name && (
          <>
            {boardContent[0].name === username && (
              <>
                <Button variant="contained" href={`/Board1Mod/${post_num}`} sx={{ mb: 2, mr: 2 }}>
                  글 수정
                </Button>
                <Button variant="contained" onClick={handleDelete} sx={{ mb: 2, mr: 2, color: '#FFFFFF' }}>
                  글 삭제
                </Button>
              </>
            )}
          </>
        ) : "Loading..."}
        <Button  variant="contained" href="/Board1" sx={{ mb: 2 }}>
          글 목록
        </Button>
      </Box>
      <DivLine />
      <Paper elevation={3} sx={{ p: 3, mt: 3 }}>
      <Typography>
      <span style={{fontSize : 30, fontWeight : 'bold', color : '#012A5B'}}>Comment</span>
      </Typography>
      <DivLine />
      {comments.map((c) => (
        <div key={c.comment_id}>
        <Typography variant="body1" fontSize={15} sx={{ mb: 3, display: 'flex', justifyContent: 'space-between' }}>
          <span>ㄴ {c.contents}</span>
          <span>{c.name} {c.date}
          {c.name === username && (
        <>
            <Button size='small' onClick={() => handleCommentDelete(c.comment_id)} href={`/Board1View/${post_num}`} sx={{ ml: 1 }}>
              X
            </Button>
            </>
      )}
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
      <Button variant="contained" sx={{ bgcolor : '#012A5B', color : '#FFFFFF' }} onClick={handleCommentInput} >
        댓글 달기
      </Button>
    </Paper>

      </Box>
    </div>
  );
};

export default Board1View;