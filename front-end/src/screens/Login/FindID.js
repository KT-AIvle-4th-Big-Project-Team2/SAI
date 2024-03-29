import * as React from 'react';
import { Button, TextField, Link, Box, Typography, Container } from '@mui/material/';
import { useNavigate } from 'react-router-dom';
import logo from '../../assets/SAI_logo_slogan.png';
import { createTheme, ThemeProvider } from '@mui/material/styles';

// 회원가입 찾기 페이지

const defaultTheme = createTheme();

function Copyright(props) {
  return (
    <Typography variant="body2" color="text.secondary" align="center" {...props}>
      Copyright© 2024 SAI All rights reserved.
    </Typography>
  );
}

export default function FindID() {
  const navigate = useNavigate();

  const handleButtonClick = () => {
    // 여기에 이메일로 비밀번호 찾기 안내 통신 로직

    // Alert 표시
    alert('이메일로 비밀번호 찾기 안내를 보내드렸습니다.');

    // '/login' 페이지로 리디렉션
    navigate('/login');
  };

  return (
    
    <ThemeProvider theme={defaultTheme}>
    <Container component="main" maxWidth="xs">
      <Box
        component="form"
        border={1}
        p={3}
        noValidate
        sx={{
          mt: 16,
          minWidth: 400,
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
        }}
      >
        <img src={logo} alt="logoslogan" />
        <Typography component="h1" variant="h5">
          비밀번호 찾기
        </Typography>
        <Box sx={{ mt: 1 }}>
          <TextField
            margin="normal"
            required
            fullWidth
            id="Name"
            label="이름"
            name="Name"
            autoComplete="Name"
            autoFocus
          />
          <TextField
            margin="normal"
            required
            fullWidth
            name="Email"
            label="이메일"
            type="Email"
            id="Email"
            autoComplete="email"
          />
          <Button
            fullWidth
            variant="contained"
            sx={{ mt: 3, mb: 2 }}
            onClick={handleButtonClick} // 클릭 시 handleButtonClick 함수 호출
          >
            제출
          </Button>
        </Box>
      </Box>
      <Box textAlign="right" sx={{mt : 1}}>
        <Link href="/login" variant="body2">
          로그인으로 돌아가기
        </Link>
      </Box>
      <Copyright sx={{ mt: 8, mb: 4 }} />
    </Container>
    </ThemeProvider>
  );
}