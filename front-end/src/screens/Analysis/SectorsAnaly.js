import React, { useState } from 'react';
import { Box, Button, Grid, Divider} from '@mui/material';

const SectorsAnaly = () => {
  const [sector, setSector] = useState('');

  const sectors = [
    '한식음식점',
    '카페',
    '분식전문점',
    '간이주점',
    '치킨전문점',
    '중식음식점',
    '패스트푸드점',
    '제과점',
    '일식음식점',
    '양식음식점',
    '편의점',
    '일반의류',
    '화장품',
    '의약품',
    '일반교습학원',
    '미용실',
    '세탁소'
  ];

  const handleChange = (event) => {
    setSector(event.target.value);
  };

  return (
    <Box sx={{ mt: 3, mb: 3 }}>
      <Box>
        <h2>업종 선택</h2>
      </Box>
      <Divider sx={{ borderColor: 'lime', mt: 3, mb: 3 }} />
        <Grid container spacing={2} sx={{ height: '100%' }}>
          <Grid item xs={3}>
            <Box border={1} p={2} borderRadius={4} sx={{ height: '100%' }}>
              {sectors.map((sector, idx) => (
                <Button key={sector} value={sector} variant="outlined" onClick={handleChange} sx={{ mr: 2, mb: 1 }}>
                  {sector}
                </Button>
              ))}
            </Box>
          </Grid>
          <Grid item xs={4} container justifyContent="flex-end" style={{ display: sector ? 'block' : 'none' }}>
            <Box border={1} p={2} borderRadius={4} sx={{ height: '100%', width: '100%' }}>
              <h5>현재 선택 업종: {sector}</h5>
              <Button href="#Report" size="large" variant="contained">
                분석 보기
              </Button>
            </Box>
          </Grid>
        </Grid>
    </Box>
  );
};

export default SectorsAnaly;