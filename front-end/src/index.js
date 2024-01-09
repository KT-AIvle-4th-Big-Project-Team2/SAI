import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import { ThemeProvider, createTheme, CssBaseline } from '@mui/material';
import { AuthProvider } from './components/Auth/AuthContext'; // AuthProvider를 import

const theme = createTheme({
  palette: {
    primary: {
      main: '#8398CA'
    },
  },
  typography: {
    fontFamily: "'Noto Sans KR', sans-serif"
  }
});

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <AuthProvider> {/* AuthProvider로 감싸기 */}
      <ThemeProvider theme={theme}>
        <CssBaseline />
        <App />
      </ThemeProvider>
    </AuthProvider>
  </React.StrictMode>
);