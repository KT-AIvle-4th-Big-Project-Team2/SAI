import React from 'react';
import {
  Button,
  CssBaseline,
  TextField,
  Link,
  Grid,
  Box,
  Typography,
  Container,
} from '@mui/material/';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { useAuth } from '../../components/Auth/AuthContext';
import axios from 'axios';
import logo from '../../assets/SAI_logo_slogan.png'

function Copyright(props) {
  return (
    <Typography variant="body2" color="text.secondary" align="center" {...props}>
      Copyright© 2024 SAI All rights reserved.
    </Typography>
  );
}


const defaultTheme = createTheme();

//const [cookies, setCookie, removeCookie] = useCookies(['my-cookie']);

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
 // 예시: CSRF 토큰을 가져오는 함수

// 회원 가입 관련 페이지

    export default function SignIn() {

      // 로그인 관리 Auth 변수 호출
      const { loginHandler, setUserInfo, setCsrfTokenHandler } = useAuth();
    
      // 로그인 제출 관련 함수 정리

      const handleSubmit = async (event) => {
        event.preventDefault();
        const data = new FormData(event.currentTarget);
        const joinData = {
          email: data.get('email'),
          password: data.get('password'),
        };
    
        /*
        try {
          // CSRF 토큰을 받는 요청을 먼저 보냅니다.
          const csrfResponse = await fetch("http://subdomain.storeaivle.com/accounts/getcsrf/", {
            method: "GET",
            headers: {
              'Accept': 'application/json',
            },
            credentials: 'include',
          });
    
          if (csrfResponse.ok) {
            const csrfData = await csrfResponse.json();
            const csrfToken = csrfData.csrf_token;
            console.log(csrfData);
            console.log(csrfToken);
            // 사용 예시
            
            // CSRF 토큰을 설정합니다.
            setCsrfTokenHandler(csrfToken);
          
            // 로그인 요청을 보냅니다.
            const loginResponse = await fetch("http://subdomain.storeaivle.com/accounts/login/", {
              method: "POST",
              headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'X-CSRFToken': csrfToken,
              },
              body: JSON.stringify({
                username: joinData.email,
                password: joinData.password
              }),
              credentials: 'include',
            });
          
            if (loginResponse.ok) {
              const data = await loginResponse.json();
              
              console.log("Login successful:", data);
              console.log(csrfToken);
              
              loginHandler();
              setUserInfo(data);
            } else {
              console.error("Login failed:", loginResponse.status);
            }
          } else {
            console.error("Failed to fetch CSRF token:", csrfResponse.status);
          }
          
        } catch (error) {
          console.error("Network error:", error);
        }
      };
      */

      try {
        const response = await axios.post('http://subdomain.storeaivle.com/accounts/login/', {
          username: joinData.email,
          password: joinData.password
        }, {
          headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
          },
          withCredentials: false // 이 옵션을 false로 설정
        });
    
        console.log("Login successful:", response.data);
        loginHandler();
        setUserInfo(response.data);
      } catch (error) {
        if (error.response) {
          // 서버로부터 응답이 있으나 2xx 범위 밖인 경우
          console.error("Login failed:", error.response.status);
        } else if (error.request) {
          // 요청이 이루어졌으나 응답이 없는 경우
          console.error("No response:", error.request);
        } else {
          // 요청 설정 중 발생한 오류
          console.error("Error:", error.message);
        }
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
              onClick={loginHandler}
              href = '/Home'  // 임시로 링크 설정
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