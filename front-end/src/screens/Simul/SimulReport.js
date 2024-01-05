import React from 'react';
import { Paper, Grid, Typography, Box } from '@mui/material/';

const SimulReport = () => {
  const user = '오진원';
  const danger = '위험';
  const result = 9.3;

  const Gu = '동대문구';
  const Dong = '전농동';
  const Sector = '치킨 전문점';
  const startupCapital = 'dddd원'; // 동적으로 계산되거나 API에서 가져오는 값으로 변경할 수 있습니다.

  const InfoText = ({ children }) => (
    <Typography fontSize={18} sx={{ml : 10, mt : 10, mr : 10}}>
      {children}
    </Typography>
  );

  return (
    <Paper elevation={3} borderRadius={8} bgcolor="#cccccc" sx={{ mt: 3, mb: 4, height: 2000 }}>
      <Box p={2} bgcolor="grey.100">
        <Typography fontSize={40} sx={{ml : 10, mt : 2}}>
          SAI! 예상 창업 비용
        </Typography>
      </Box>
      <Box p={2} border="1px solid black" borderRadius={8} sx={{ height: 1800, mb: 3}}>
        <Typography fontSize={40} sx={{ml : 10, mt : 2}}>
          선택 값을 반영해 SAI!로 분석한 {user} 님의 매장의 예상 매출이에요
        </Typography>

        <Grid container spacing={2} sx={{padding: 10}}>
          <Grid item xs={4}>
            <Typography fontSize={25}>지역 {Gu} {Dong}</Typography>
          </Grid>
          <Grid item xs={4}>
            <Typography fontSize={25}>업종 {Sector}</Typography>
          </Grid>
          <Grid item xs={4}>
            <Typography fontSize={25}>창업준비금 {startupCapital}</Typography>
          </Grid>
        </Grid>

        <Box sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '40vh' }}>
          <Typography fontSize={50}>
            그래프
          </Typography>
        </Box>

        <Box bgcolor={'gray.100'}>
          <Typography fontSize={30} sx={{ml : 10, mt : 10}}>창업 지수 : {danger}</Typography>
          <InfoText>{Gu} {Dong}에서 {Sector} 업종 창업은 서울시 내 동종 업종의 평균 추정 매출 대비 {danger}% 낮아요.</InfoText>
          <InfoText>{Gu} {Dong}에서 {Sector} 업종 창업은 자치구에 비해 매출이 (증가/감소) 추세예요. 인근 지역에 비해 (활성화/ 비활성화) 된 상권이에요. 경쟁 관계에 유의하세요.</InfoText>
          <InfoText>{Gu} {Dong}에서 {Sector} 업종의 점포수가 전년 동기에 비해 (증가/감소)하고 있어요. 상권이 (발달/쇠퇴)하는 시기인 경우 입지 선정에 신중하셔야 해요.</InfoText>
          <InfoText>{Gu} {Dong}은 전년 동분기에 비해 유동인구가 [감소]하고 있는 지역이에요. 마케팅이 중요한 상권이에요.</InfoText>
        </Box>
      </Box>
    </Paper>
  );
}

export default SimulReport;
