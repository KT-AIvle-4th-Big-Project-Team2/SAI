import React from 'react';
import { Box, Button, Paper, Typography, Divider } from '@mui/material';

const BoardView = () => {
  return (
    <Box sx={{ p: 2, height: '100%' }}>
      <Typography variant="h4" sx={{ mb: 2 }}>
        게시판
      </Typography>
      <Divider sx={{ borderColor: 'lime', mt: 3, mb: 3 }} />

      <Paper elevation={3} sx={{ p: 3, mb: 3, minHeight: 500 }}>
        <Typography variant="h4" sx={{ mb: 2 }}>
          글 제목
        </Typography>
        <hr />
        <Typography variant="body1" sx={{ height: 'auto' }}>
          글 내용
        </Typography>
      </Paper>

      <Button variant="contained" href="/Board" sx={{ mb: 2 }}>
        글 목록
      </Button>
      <hr />

      <Paper elevation={3} sx={{ p: 3, mt: 3 }}>
        <Typography variant="h6" sx={{ mb: 2 }}>
          Comment
        </Typography>
        {/* Add your comment components here */}
      </Paper>
    </Box>
  );
};

export default BoardView;