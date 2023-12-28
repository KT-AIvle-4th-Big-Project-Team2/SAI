import React from 'react';
import { Button } from '@mui/material';

const BoardView = () => {
  return (
    <>      
    
      <div>글 제목</div>
      <div>글 내용</div>
      <p></p>
      <Button variant="contained" href="/Board">글 목록</Button>
      <hr />
      <p></p>
      <div>comment</div>
    </>
  )
}

export default BoardView