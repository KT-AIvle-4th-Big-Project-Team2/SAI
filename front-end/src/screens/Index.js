import React from 'react';
import { Button, Grid, Box, Typography, CssBaseline } from '@mui/material/';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import backgroundimg from './indexbackground.jpg';
import backimage from '../assets/mainpage_picture.png';

const theme = createTheme({
  palette: {
    primary: {
      main: '#DAA520',
    },
    secondary: {
      main: '#1E90FF',
    },
  },
  components: {
    MuiCssBaseline: {
      styleOverrides: {
        body: {
          backgroundImage: `url(${backimage})`,
          backgroundSize: 'cover',
        },
      },
    },
    MuiButton: { // 여기로 이동
      styleOverrides: {
        root: {
          backgroundColor: 'black',
          color: 'white',
          '&:hover': {
            backgroundColor: 'lightblue',
          },
        },
      },
    },
  },
});


const About = () => {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Grid container spacing={2} textAlign="center" p={2} sx={{ minHeight: '50vh', mt: 5 }}>
        
        <Grid item xs={12} p={3} sx={{ border: '1px solid black', borderRadius: '4px' }}>
          <Typography variant="h3">창업지원 프로그램</Typography>
          <Typography>상업용 부동산에서 발생할 수 있는 미래가치인 매출을 추정하는 AI 알고리즘...</Typography>
        </Grid>

        <Grid item xs={12} container spacing={2} justifyContent="space-around" mt={4}>
          {/* 네모 박스들 */}
          {[1, 2, 3, 4].map((box) => (
            <Grid item xs={12} sm={6} md={3} key={box}>
              <Box p={3} sx={{ border: '1px solid black', borderRadius: '4px' }}>
                <Typography>{`내용${box}`}</Typography>
              </Box>
            </Grid>
          ))}

          <Grid item xs={12}>
            <Button variant="outlined" sx={{ mt: 5, mb: 3 }} size="large" href="/login" >
              로그인 하여 지금 시작
            </Button>
          </Grid>
        </Grid>
      </Grid>
    </ThemeProvider>
  );
};

export default About;
