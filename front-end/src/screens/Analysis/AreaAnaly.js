import React, { useState } from 'react';
import { Box, Button, Grid } from '@mui/material';
import Data from '../../assets/서울시 행정동.json';

const jsonData = Data;
const uniqueGu = new Set();
jsonData.forEach(item => {
  uniqueGu.add(item.시군구명);
});

const uniqueGuArray = Array.from(uniqueGu);

const DongArray = []; // Rename the array to avoid conflict with state variable

for (let i = 0; i < 25; i++) {
  DongArray[i] = jsonData
    .filter(item => item.시군구명 === uniqueGuArray[i])
    .map(item => item.읍면동명);
}

export default function AreaAnaly() {
  const [Gu, setGu] = useState('');
  const [selectedDong, setSelectedDong] = useState(''); // Rename to avoid conflict

  const handleChange = (event) => {
    setGu(event.target.value);
    setSelectedDong(''); // Reset selectedDong when Gu changes
  };

  const handleChange2 = (event) => {
    setSelectedDong(event.target.value);
  };

  function SelectDong() {
    for (let i = 0; i < 25; i++) {
      if (Gu === uniqueGuArray[i]) {
        // Check if DongArray[i] exists before calling map
        return DongArray[i] ? (
          DongArray[i].map((dong, idx) => (
            <Button key={dong} value={dong} onClick={handleChange2}>
              {dong}
            </Button>
          ))
        ) : null;
      }
    }
    return null; // Return null if no matching Gu is found
  }

  return (
    <>
      <Box sx={{ mt: 3, mb: 5 }}>
        <h2>지역 선택</h2>
      </Box>
      <Grid container spacing={2}>
        <Grid>
          {uniqueGuArray.map((gu, idx) => (
            <Button key={gu} value={gu} onClick={handleChange}>
              {gu}
            </Button>
          ))}
        </Grid>
        <Grid>
          <h2>현재 선택 지역 : {Gu}</h2>
          <SelectDong />
        </Grid>
      </Grid>
      <h2>현재 선택 지역 : {selectedDong}</h2>
      <br />
      <Button href="#report" size="large" variant="contained">
        리포트 보기
      </Button>
    </>
  );
}