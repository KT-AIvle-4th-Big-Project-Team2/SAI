import React, {useState} from 'react'
import { Box } from '@mui/material'
import Button from '@mui/material/Button';
import Grid from '@mui/material/Grid';
import KakaoMap from '../KakaoMap';

export default function SelectVariants() {
  const [Gu, setGu] = useState('');
  const [Dong, setDong] = useState('');
  const Gu_SELECT = ['종로구',
    '중구',
    '용산구',
    '성동구',
    '광진구',
    '동대문구',
    '중랑구',
    '성북구',
    '강북구',
    '도봉구',
    '노원구',
    '은평구',
    '서대문구',
    '마포구',
    '양천구',
    '강서구',
    '구로구',
    '금천구',
    '영등포구',
    '동작구',
    '관악구',
    '서초구',
    '강남구',
    '송파구',
    '강동구',];
  const jonglo = ['가회동',
    '교남동',
    '무악동',
    '부암동',
    '사직동',
    '삼청동',
    '숭인1동',
    '숭인2동',
    '이화동',
    '종로1·2·3·4가동',
    '종로5·6가동',
    '창신1동',
    '창신2동',
    '창신3동',
    '청운효자동',
    '평창동',
    '혜화동',
  ]
  const jung = ['광희동',
  '다산동',
  '동화동',
  '명동',
  '소공동',
  '신당5동',
  '신당동',
  '약수동',
  '을지로동',
  '장충동',
  '중림동',
  '청구동',
  '필동',
  '황학동',
  '회현동',
  ]
  const junglang = ['망우3동',
  '망우본동',
  '면목2동',
  '면목3·8동',
  '면목4동',
  '면목5동',
  '면목7동',
  '면목본동',
  '묵1동',
  '묵2동',
  '상봉1동',
  '상봉2동',
  '신내1동',
  '신내2동',
  '중화1동',
  '중화2동',
  ]


  
  const handleChange = (event) => {
    setGu(event.target.value);
  };

  const handleChange2 = (event) => {
    setDong(event.target.value);
  };

  return (
    <>
    <Box sx = {{mt : 3, mb : 5 }}><h2>지역 선택</h2></Box>
    <Grid container spacing={2}>
      <Grid xs={2}>
      {Gu_SELECT.map((Gu, idx) => {
        return <Button onClick={handleChange}>{Gu}</Button>
      })}
      </Grid>
      <Grid xs={4}>
      {jonglo.map((dong, idx) => {
        return <Button onClick={handleChange2}>{dong}</Button>
      })}
      </Grid>
    </Grid>
    <KakaoMap />
      
      <br></br>
          
      <Button href = '/SimulReport' size='large' variant="contained">리포트 보기</Button>
    </>
  );
}