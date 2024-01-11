import React from 'react';
import { CircularProgress } from '@mui/material';

// 로딩 페이지 컴포넌트

const LoadingPage = () => {
    return (
        <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh' }}>
            <CircularProgress color="secondary" size={80} />
        </div>
      );
    };
    
    export default LoadingPage;