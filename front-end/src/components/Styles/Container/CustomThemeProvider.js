import React from 'react';
import { createTheme, ThemeProvider } from '@mui/material';

const customTheme = createTheme({
  palette: {
    primary: {
      main: '#32cd32',
    },
  },
});

const CustomThemeProvider = ({ children }) => {
  return <ThemeProvider theme={customTheme}>{children}</ThemeProvider>;
};

export default CustomThemeProvider;