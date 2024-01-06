import * as React from 'react';
import { useState } from 'react';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import {
  Avatar,
  Button,
  CssBaseline,
  TextField,
  FormControl,
  FormControlLabel,
  Checkbox,
  Link,
  Grid,
  Box,
  Typography,
  Container,
  Radio,
  RadioGroup,
  FormLabel,
} from '@mui/material/';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import axios from 'axios';
import TermsModal from '../../components/TermsModal';

function Copyright(props) {
  return (
    <Typography variant="body2" color="text.secondary" align="center" {...props}>
      {'Copyright © SAI! All Rights Reserved.'}
    </Typography>
  );
}

// TODO remove, this demo shouldn't need to reset the theme.

const defaultTheme = createTheme();

export default function SignUp() {

  
  const [checked, setChecked] = useState(false);
  const [emailError, setEmailError] = useState('');
  const [passwordState, setPasswordState] = useState('');
  const [passwordError, setPasswordError] = useState('');
  const [nameError, setNameError] = useState('');
  const [registerError, setRegisterError] = useState('');


  const handleSubmit = (event) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    const joinData = {
      email: data.get('email'),
      name: data.get('name'),
      password: data.get('password'),
      rePassword: data.get('rePassword'),
      age: data.get('age')
    };
    const { email, name, password, rePassword, age } = joinData;
    axios.post("https://subdomain.storeaivle.com/accounts/signin/", {
      name,
      password,
      email,
      age
    })


    const emailRegex =
      /([\w-.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([\w-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$/;
    if (!emailRegex.test(email)) {
      setEmailError('올바른 이메일 형식이 아닙니다.');
    } else {
      setEmailError('');
    }
    // 비밀번호 유효성 체크
    const passwordRegex = /^(?=.*[a-zA-Z])(?=.*[!@#$%^*+=-])(?=.*[0-9]).{8,25}$/;
    if (!passwordRegex.test(password)) {
      setPasswordState('숫자+영문자+특수문자 조합으로 8자리 이상 입력해주세요!');
    } else {
      setPasswordState('');
    }

    // 비밀번호 같은지 체크
    if (password !== rePassword) {
      setPasswordError('비밀번호가 일치하지 않습니다.');
    } else {
      setPasswordError('');
    }

    // 이름 유효성 검사
      const nameRegex = /^[가-힣a-zA-Z]+$/;
      if (!nameRegex.test(name) || name.length < 1) {
        setNameError('올바른 이름을 입력해주세요.');
      } else {
        setNameError('');
      }

      const ageRegex = /^(?=.*[0-9])/;
      if (!ageRegex.test(age) || age.length < 1) {
        setNameError('올바른 이름을 입력해주세요.');
      } else {
        setNameError('');
      }

      // 회원가입 동의 체크
      if (!checked) alert('회원가입 약관에 동의해주세요.');

    };

  // 동의 체크

  //이용약관 모달
  const [isChecked, setIsChecked] = useState(false);
  const [isTermsModalOpen, setTermsModalOpen] = useState(false);

  const handleAgree = (event) => {
    setIsChecked(event.target.checked);
  };

  const handleAgreeTextClick = () => {
    if (!isChecked) {
      setTermsModalOpen(true);
    }
  };

  const handleCloseTermsModal = () => {
    setTermsModalOpen(false);
  };

  return (
    <ThemeProvider theme={defaultTheme}>
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
          <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
            <LockOutlinedIcon />
          </Avatar>
          <Typography component="h1" variant="h5">
            회원가입
          </Typography>
          <Box component="form" noValidate onSubmit={handleSubmit} sx={{ mt: 3 }}>
            <Grid container spacing={2}>
              <Grid item xs={12}>
                <TextField
                  autoComplete="given-name"
                  name="name"
                  required
                  fullWidth
                  id="name"
                  label="이름"
                  autoFocus
                  error={nameError !== '' || false}
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  autoComplete="given-name"
                  name="nickname"
                  required
                  fullWidth
                  id="nickname"
                  label="닉네임"
                  autoFocus
                  error={nameError !== '' || false}
                />
              </Grid>
              <Grid item xs={12}>
                <FormControl>
                  <FormLabel id="demo-row-radio-buttons-group-label">성별 *</FormLabel>
                  <RadioGroup
                    row
                    aria-labelledby="demo-row-radio-buttons-group-label"
                    name="row-radio-buttons-group"
                  >
                    <FormControlLabel value="male" control={<Radio />} label="남성" />
                    <FormControlLabel value="female" control={<Radio />} label="여성" />
                  </RadioGroup>
                </FormControl>
              </Grid>
              <Grid item xs={12}>
                <TextField
                  required
                  fullWidth
                  id="age"
                  label="나이"
                  name="age"
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  required
                  fullWidth
                  id="email"
                  label="이메일"
                  name="email"
                  autoComplete="email"
                  error={emailError !== '' || false}
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  required
                  fullWidth
                  name="password"
                  label="비밀번호 (숫자 + 영문자 + 특수문자 8자리 이상)"
                  type="password"
                  id="password"
                  autoComplete="new-password"
                  error={passwordState !== '' || false}
                  helperText={passwordState}
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  required
                  fullWidth
                  name="repassword"
                  label="비밀번호 확인"
                  type="password"
                  id="repassword"
                  error={passwordError !== '' || false}
                />
              </Grid>
              <Grid container alignItems="center" sx={{ml:2, mt :1}}>
              <Grid item>
                <FormControlLabel
                  control={<Checkbox onChange={handleAgree} color="primary" />}
                />
              </Grid>
              <Grid item>
                <span
                  style={{ textDecoration: 'underline', cursor: 'pointer' }}
                  onClick={handleAgreeTextClick}
                >
                  개인정보 수집 및 이용에 동의합니다.
                </span>
              </Grid>
              {!isChecked && (
                <TermsModal open={isTermsModalOpen} onClose={handleCloseTermsModal} />
              )}
            </Grid>
            </Grid>
            <Button
              type="submit"
              fullWidth
              variant="contained"
              href = '/login'
              sx={{ mt: 3, mb: 2 }}
            >
              회원가입
            </Button>
            <Grid container justifyContent="flex-end">
              <Grid item>
                <Link href="/login" variant="body2">
                  이미 계정이 있으신가요? 로그인
                </Link>
              </Grid>
            </Grid>
          </Box>
        </Box>
        <Copyright sx={{ mt: 5 }} />
      </Container>
    </ThemeProvider>
  );
}