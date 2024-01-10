import React from 'react';
import { CircularProgress } from '@mui/material';

const LoadingPage = () => {
    return (
        <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh' }}>
            <CircularProgress color="secondary" size={80} />
        </div>
      );
    };
    
    export default LoadingPage;