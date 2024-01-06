// import React from 'react'
// import {Avatar, Button, CssBaseline, TextField, Grid, Box, Typography, Container} from '@mui/material/';
// import LockOutlinedIcon from '@mui/icons-material/LockOutlined';

// const Myinfo = () => {
//   const name = '홍길동'
//   const sex = '남성'
//   const age = 25
//   const email = 'asdf@Google.com'
//   return (
//     <Container component="main" maxWidth="xs">
//       <CssBaseline />
//       <Box
//         sx={{
//           marginTop: 8,
//           display: 'flex',
//           flexDirection: 'column',
//           alignItems: 'center',
//         }}
//       >
//         <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
//           <LockOutlinedIcon />
//         </Avatar>
//         <Typography component="h1" variant="h5">
//           내 정보 수정
//         </Typography>
//         <Box component="form" noValidate sx={{ mt: 3 }}>
//           <Grid container spacing={2}>
//             <Grid item xs={12}>
//               <h4>이름 : {name}</h4>
//             </Grid>
//             <Grid item xs={12}>
//               <h4>성별 : {sex}</h4>
//             </Grid>
//             <Grid item xs={12}>
//               <h4>나이 : {age}</h4>
//             </Grid>
//             <Grid item xs={12}>
//               <h4>이메일 : {email}</h4>
//             </Grid>
//             <Grid item xs={12}>
//               <TextField
//                 required
//                 fullWidth
//                 name="password"
//                 label="Password"
//                 type="password"
//                 id="password"
//                 autoComplete="new-password"
//               />
//             </Grid>
//             <Grid item xs={12}>
//               <TextField
//                 required
//                 fullWidth
//                 name="password"
//                 label="PasswordCheck"
//                 type="password"
//                 id="password"
//               />
//             </Grid>
//           </Grid>
//           <Button
//             type="submit"
//             fullWidth
//             variant="contained"
//             href = '/Home'
//             sx={{ mt: 3, mb: 2 }}
//           >
//             수정 완료
//           </Button>
//         </Box>
//       </Box>
//     </Container>
//   )
// }

// export default Myinfo

import React from 'react';
import { Avatar, Button, CssBaseline, TextField, Grid, Box, Typography, Container } from '@mui/material';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import Withdrawal from './WithDrawal';

const Myinfo = () => {
  const name = '홍길동';
  const sex = '남성';
  const age = 25;
  const email = 'asdf@Google.com';

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
        <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
          <LockOutlinedIcon />
        </Avatar>
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