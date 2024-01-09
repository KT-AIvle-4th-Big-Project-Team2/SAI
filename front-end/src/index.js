import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import { ThemeProvider, createTheme, CssBaseline } from '@mui/material';

const theme = createTheme({
  palette: {
    primary: {
      main: '#8398CA',
      gray: '#EEEEEE',
      orange: '#FF6B00',
      dark: '#012A5B',
      pink: '#F25278',
      blue: '#0055FF'
    },
  },
  typography: {
    fontFamily: "'Noto Sans KR'"
  }
});


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  
    <React.StrictMode>
      <ThemeProvider theme={theme}>
      <CssBaseline />
      <App />
      </ThemeProvider>
    </React.StrictMode>
);