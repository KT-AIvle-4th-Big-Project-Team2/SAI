import React, {useState} from 'react'
import { Box } from '@mui/material'
import Button from '@mui/material/Button';

export default function SelectVariants() {
  const [Gu, setGu] = useState('')

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
    '강동구',]
  const Dong_SELECT = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

  const handleChange = (event) => {
    setGu(event.target.value);
  };

  return (
    <>
    <Box sx = {{mt : 3, mb : 5 }}><h2>지역 선택</h2></Box>
          
      {Gu_SELECT.map((Gu, idx) => {
        return <Button>{Gu}</Button>
        
      })}
          
          
      <Button href = '/SimulReport' size='large'>리포트 보기</Button>
    </>
  );
}