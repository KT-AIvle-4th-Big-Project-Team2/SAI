import React, { useState, useEffect } from 'react';
import {
  Avatar,
  Button,
  CssBaseline,
  TextField,
  FormControlLabel,
  Checkbox,
  Link,
  Grid,
  Box,
  Typography,
  Container,
} from '@mui/material/';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { useAuth } from '../../components/Auth/AuthContext';
import axios from 'axios';
import logo from '../../assets/SAI_logo_slogan.png'

function Copyright(props) {
  return (
    <Typography variant="body2" color="text.secondary" align="center" {...props}>
      {'Copyright © '}
      <Link color="inherit" href="https://mui.com/">
        Your Website
      </Link>{' '}
      {new Date().getFullYear()}
      {'.'}
    </Typography>
  );
}

// TODO remove, this demo shouldn't need to reset the theme.

const defaultTheme = createTheme();

/*
export default function SignIn() {
  const { loginHandler, setUserInfo, setCsrfTokenHandler } = useAuth();

  const [authTokens, setAuthTokens] = useState('')
  const handleSubmit = (event) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    const joinData = {
      email: data.get('email'),
      password: data.get('password'),
    };
    console.log(joinData)
      const {email, password} = joinData
      const username = email
      axios.post("https://subdomain.storeaivle.com/accounts/login", {
        username,
        password
      },
      {
        withCredentials: true,
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json',
        },
        credentials: 'include',
      }
      )
        .then((response) => {
          if (response.status === 200) {
            console.log("CSRF token received:", response.headers['Set-Cookie']);
            loginHandler();
            setUserInfo(response.data)
            console.log(response.data)
          }
        })
        .catch(function (error) {
          console.log(error);
        });
    };
  */

    export default function SignIn() {
      const { loginHandler, setUserInfo, setCsrfTokenHandler } = useAuth();
    
      const handleSubmit = async (event) => {
        event.preventDefault();
        const data = new FormData(event.currentTarget);
        const joinData = {
          email: data.get('email'),
          password: data.get('password'),
        };
        console.log(joinData);
    
        try {
          const response = await fetch("https://subdomain.storeaivle.com/accounts/login", {
            method: "POST",
            headers: {
              'Content-Type': 'application/json',
              'Accept': 'application/json',
            },
            body: JSON.stringify({
              username: joinData.email,
              password: joinData.password
            }),
            credentials: 'include', // 자격 증명을 포함시킵니다.
          });
    
          if (response.ok) {
            const data = await response.json();
            console.log("CSRF token received:", response.headers.get('Set-Cookie'));
            loginHandler();
            setUserInfo(data);
            console.log(data);
          } else {
            console.error("Response not OK", response.status);
          }
        } catch (error) {
          console.error("Network error:", error);
        }
      };

  return (
    <ThemeProvider theme={defaultTheme}>
      <Container component="main" maxWidth="xs">
        <CssBaseline />
        <Box
          sx={{
            marginTop: 15,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
          }}
        >
        <Box component="form" border={1} p = {3} onSubmit={handleSubmit} noValidate sx={{ mt: 1, minWidth: 400, display: 'flex',
            flexDirection: 'column',
            alignItems: 'center', }}>
              <img src={logo} alt="logoslogan"/>
              <Typography component="h1" variant="h5">
                로그인
              </Typography>
            <TextField
              margin="normal"
              required
              fullWidth
              id="email"
              label="이메일"
              name="email"
              autoComplete="email"
              autoFocus
            />
            <TextField
              margin="normal"
              required
              fullWidth
              name="password"
              label="비밀번호"
              type="password"
              id="password"
              autoComplete="current-password"
            />
            <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
            >
              로그인
            </Button>
            
          </Box>
            <Grid container sx={{mt:1}}>
              <Grid item xs>
                <Link href="/findid" variant="body2">
                  비밀번호 찾기
                </Link>
              </Grid>
              <Grid item>
                <Link href="signup" variant="body2">
                  {"회원가입"}
                </Link>
              </Grid>
            </Grid>
        </Box>
        <Copyright sx={{ mt: 8, mb: 4 }} />
      </Container>
    </ThemeProvider>
  );
        
}