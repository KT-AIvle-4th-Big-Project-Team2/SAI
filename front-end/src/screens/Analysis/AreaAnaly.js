import React, { useState } from 'react';
import { Box, Button, Grid, Divider } from '@mui/material';
import Data from '../../assets/서울시 행정동.json';
import DivLine from '../../components/Styles/DivLine'

const jsonData = Data;
const uniqueGu = new Set();
jsonData.forEach(item => {
  uniqueGu.add(item.시군구명);
});

const uniqueGuArray = Array.from(uniqueGu);

const DongArray = [];
for (let i = 0; i < 25; i++) {
  DongArray[i] = jsonData
    .filter(item => item.시군구명 === uniqueGuArray[i])
    .map(item => item.읍면동명);
}

export default function AreaAnaly() {
  const [Gu, setGu] = useState('');
  const [selectedDong, setSelectedDong] = useState('');

  const handleChange = (event) => {
    setGu(event.target.value);
    setSelectedDong('');
  };

  const handleChange2 = (event) => {
    setSelectedDong(event.target.value);
  };

  function SelectDongButtons() {
    for (let i = 0; i < 25; i++) {
      if (Gu === uniqueGuArray[i]) {
        return DongArray[i] ? (
          DongArray[i].map((dong, idx) => (
            <Button
              key={dong}
              value={dong}
              variant="outlined"
              sx={{ mr: 2, mb: 1 }}
              onClick={handleChange2}
            >
              {dong}
            </Button>
          ))
        ) : null;
      }
    }
    return null;
  }

  return (
    <>
    <Box sx={{ height: '100%', mt: 3, mb: 3, width: 'fit-content' }}>
      <h2 >지역 선택</h2>
    </Box>
    <DivLine />
      <Grid container spacing={2} sx={{ height: '100%' }}>
        {/* First Grid */}
        <Grid item xs={3}>
          <Box border={1} p={2} borderRadius={4} sx={{height: '100%', fontWeight: 'bold' }}>
            <h5>지역구 : {Gu}</h5>
            {uniqueGuArray.map((gu, idx) => (
              <Button
                key={gu}
                value={gu}
                variant="outlined"
                onClick={handleChange}
                sx={{ mr: 2, mb: 1, }}
              >
                {gu}
              </Button>
            ))}
            </Box>
        </Grid>

        {/* Second Grid */}
        <Grid item xs={3} style={{ display: Gu ? 'block' : 'none' }}>
          <Box border={1} p={2} borderRadius={4} sx={{height: '100%', fontWeight: 'bold' }}>
            <h5>행정동 : {selectedDong}</h5>
            <SelectDongButtons />
          </Box>
        </Grid>

        {/* Third Grid */}
        <Grid
          item
          xs={6}
          container
          justifyContent="flex-end"
          style={{ display: selectedDong ? 'block' : 'none' }}
        >
          <Box border={1} p={2} borderRadius={4} sx={{ height: '100%', width: '100%' }}>
            <h4>현재 선택 지역 : {selectedDong}</h4>
            <br />
            <Button href="#report" size="large" variant="contained">
              리포트 보기
            </Button>
          </Box>
        </Grid>
      </Grid>
    </>
  );
}