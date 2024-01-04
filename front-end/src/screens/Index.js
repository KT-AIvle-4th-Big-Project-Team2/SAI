import React from 'react';
import {Button, Grid, Box, Typography, CssBaseline} from '@mui/material/';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import backgroundimg from './indexbackground.jpg'
const theme = createTheme({
  palette: {
    primary: {
      main: '#DAA520', // 주황색 또는 다른 원하는 색상으로 변경
    },
    secondary: {
      main: '#1E90FF', // 파란색 또는 다른 원하는 색상으로 변경
    },
  },
});

const About = () => {


  return (
    <ThemeProvider theme={theme}>
    <CssBaseline />
    <Grid container spacing={2} textAlign="center" p={2} sx={{ minHeight: '30qovh', mt: 5}} >
      
      <Box p={3} width="100%" height={200} textAlign="center" border="1px solid orange" borderRadius="4px">
      <Grid item xs={12}>
        <Typography variant="h3">창업지원 프로그램</Typography>
      </Grid>
      <Grid item xs={12}>
        <Typography>상업용 부동산에서 발생할 수 있는 미래가치인 매출을 추정하는 AI 알고리즘 공간에서 발생하는 부가가치에 따라 부동산 가치를 결정하는 수익환원법을 사용합니다.</Typography>
      </Grid>
      </Box>
      <Grid container spacing={2} justifyContent="space-around" mt={4}>
        
      <Grid item xs={12}>
        <Button variant="outlined" sx={{ mt: 5, mb: 3 }} size="large" href="/login">
          로그인 하여 지금 시작
        </Button>
      </Grid>
        {/* 네모 박스 1 */}
        <Grid item xs={12} sm={6} md={3}>
          <Box p={3} width="100%" height={200} textAlign="center" border="1px solid orange" borderRadius="4px">
            <Typography>내용1</Typography>
          </Box>
        </Grid>
        {/* 네모 박스 2 */}
        <Grid item xs={12} sm={6} md={3}>
          <Box p={3} width="100%" height={200} textAlign="center" border="1px solid orange" borderRadius="4px">
            <Typography>내용2</Typography>
          </Box>
        </Grid>
        {/* 네모 박스 3 */}
        <Grid item xs={12} sm={6} md={3}>
          <Box p={3} width="100%" height={200} textAlign="center" border="1px solid orange" borderRadius="4px">
            <Typography>내용3</Typography>
          </Box>
        </Grid>
        {/* 네모 박스 4 */}
        <Grid item xs={12} sm={6} md={3}>
          <Box p={3} width="100%" height={200} textAlign="center" border="1px solid orange" borderRadius="4px">
            <Typography>내용4</Typography>
          </Box>
        </Grid>
      </Grid>
    </Grid>
    </ThemeProvider>
  );
};

export default About;