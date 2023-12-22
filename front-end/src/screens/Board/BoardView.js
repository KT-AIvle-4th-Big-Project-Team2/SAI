import React from 'react';
import Box from '@mui/material/Box';
import Container from '@mui/material/Container';
import { Button } from '@mui/material';

const BoardView = () => {
  return (
    <>      
    <Container >
    <Box sx={{ width : '75%', bgcolor: '#cfe8fc', height: '100vh' }}>
    
      <div>글 제목</div>
      <div>글 내용</div>
      <p></p>
      <Button variant="contained" href="/Board">글 목록</Button>
      <hr />
      <p></p>
      <div>comment</div>
      </Box>
    </Container>
    </>
  )
}

export default BoardView