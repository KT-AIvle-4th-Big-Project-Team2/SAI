import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import { ThemeProvider, createTheme, CssBaseline } from '@mui/material';
import { AuthProvider } from './components/Auth/AuthContext'; // AuthProvider를 import
import './Pretendard-1.3.9/web/static/pretendard.css'; // 상대 경로로 CSS 파일을 import

// 커스텀 테마 지정
const theme = createTheme({
  palette: {
    primary: {
      main: '#012A5B',
      gray: '#EEEEEE',
      orange: '#FF6B00',
      dark: '#012A5B',
      pink: '#F25278',
      blue: '#0055FF'
    },
  },
  typography: {
    fontFamily: 'Pretendard Thin, Pretendard, sans-serif'// Pretendard 폰트 패밀리 지정
  },
});

//배포할땐 strict mode 해제
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <AuthProvider>
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <App />
    </ThemeProvider>
  </AuthProvider>
);