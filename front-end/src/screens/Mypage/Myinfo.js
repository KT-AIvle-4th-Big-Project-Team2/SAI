import React, {useState} from 'react';
import { Button, CssBaseline, TextField, Grid, Box, Typography, Container } from '@mui/material';
import Withdrawal from './WithDrawal';
import logo from '../../assets/SAI_logo_slogan.png'

const Myinfo = () => {

  // 내 정보 예시로 받아오기
  const [userdata, setUserdata] = useState({})

  const name = '오진원';
  const sex = '남성';
  const age = 28;
  const email = 'asdf@Google.com';

  // function getuserinfo() {
  //   fetch("URL")
  //     .then((response) => {
  //       if (!response.ok) {
  //         throw new Error(`HTTP error! status: ${response.status}`);
  //       }
  //       return response.json();
  //     })
  //     .then((data) => {
  //       setUserdata(...data);
  //       console.log(data);
  //     })
  //     .catch((error) => {
  //       console.log(error);
  //     });
  // }


  return (
    <Container component="main" maxWidth="xs">
      <CssBaseline />
      <Box
        sx={{
          marginTop: 8,
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
        }}
      >
          <img src={logo} alt="logoslogan"/>
          <Typography component="h1" variant="h5">
            내 정보 수정
          </Typography>
        <Box component="form" noValidate sx={{ mt: 3  }} >
          <Grid container spacing={2}>
            <Grid item xs={12}>
              <Typography variant="subtitle1" color="textSecondary">이름: {name}</Typography>
            </Grid>
            <Grid item xs={12}>
              <Typography variant="subtitle1" color="textSecondary">성별: {sex}</Typography>
            </Grid>
            <Grid item xs={12}>
              <Typography variant="subtitle1" color="textSecondary">나이: {age}</Typography>
            </Grid>
            <Grid item xs={12}>
              <Typography variant="subtitle1" color="textSecondary">이메일: {email}</Typography>
            </Grid>
            <Grid item xs={12}>
                <TextField
                  name="nickname"
                  fullWidth
                  id="nickname"
                  label="닉네임"
                  autoFocus
                />
              </Grid>
            <Grid item xs={12}>
              <TextField
                fullWidth
                name="password"
                label="비밀번호"
                type="password"
                id="password"
                autoComplete="new-password"
                variant="outlined"
              />
            </Grid>
            <Grid item xs={12}>
              <TextField
                fullWidth
                name="password"
                label="비밀번호 확인"
                type="password"
                id="repassword"
                variant="outlined"
              />
            </Grid>
          </Grid>
          <Button
            type="submit"
            fullWidth
            variant="contained"
            href="/Home"
            sx={{ mt: 3, mb: 2, backgroundColor: 'primary.main', color: 'white' }}
          >
            수정 완료
          </Button>
        </Box>
      </Box>
      <Withdrawal />
    </Container>
  );
};

export default Myinfo;