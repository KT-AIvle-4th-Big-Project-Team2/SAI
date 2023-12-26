import React from 'react'
import Button from '@mui/material/Button'

const About = () => {
  return (
   <div align = 'center'>
  
    <div className = 'box1'>
        <h1>AI</h1>
        <h2>상업용 부동산에서 발생할 수 있는 미래가치인 매출을 추정하는 AI 알고리즘</h2>
      </div>
    <div>
        <h3>공간에서 발생하는 부가가치에 따라 부동산 가치를 결정하는 수익환원법을 사용합니다</h3>
    </div>
    <Button
      variant="outlined"
      sx={{ mt: 5, mb: 3 }}
      size="large"
      href = '/login'
    >
      로그인 하여 지금 시작
    </Button>
    </div>
  )
}

export default About