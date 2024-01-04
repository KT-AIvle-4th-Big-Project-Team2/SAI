import * as React from 'react';
import {
  Box,
  Paper,
  Typography
}
from '@mui/material/'
import DivLine from '../../components/Styles/DivLine';
import { ResponsiveCirclePacking } from '@nivo/circle-packing'


const SimulReport = () => {
  const data = {
      "name": "nivo",
      "color": "hsl(38, 70%, 50%)",
      "loc" : 100
  }

  
  const user = '오진원'
  const danger = '위험' 
  const result = 9.3

  const Gu = '동대문구'
  const Dong = '전농동'
  const Sector = '치킨 전문점'

  return (
    <>
      <Paper borderRadius={8} bgcolor={'primary.main'} sx={{mt : 3, mb : 4, height : 'auto', padding : 10}}>
          <Box sx={{ mt: 3, mb: 3, width: 'fit-content', height: 'auto' }}>
            <Typography fontSize={30} sx={{ml : 10, mt : 2}}> SAI! 예상 창업 비용</Typography>
          </Box>
          <Box p={2} border="1px solid black" borderRadius={8} sx={{ height: 'auto', mb: 3}}>
            <Typography fontSize={30} sx={{ml : 10, mt : 2}}> 선택 값을 반영해 SAI!로 분석한</Typography>
            <Typography fontSize={30} sx={{ml : 10, mt : 2}}> {user} 님의 매장의 예상 매출이에요</Typography>
            <DivLine />
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: 10 }}>
            <Typography fontSize={20} sx={{ml : 30, mt : 5}}>지역 {Gu} {Dong}</Typography>
            <Typography fontSize={20} sx={{mt : 5}}>업종 {Sector}</Typography>
            <Typography fontSize={20} sx={{mt : 5, mr : 30}}>창업준비금 ddddd원</Typography>
            </div>
            <Box sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '40vh' }}>
            <ResponsiveCirclePacking
              data={data}
              margin={{ top: 20, right: 20, bottom: 20, left: 20 }}
              id="name"
              value="loc"
              />
            </Box>
            <Box bgcolor="primary.main" >
              <Typography fontSize={30} sx={{ml : 10, mt : 10, mr : 10}}>창업 지수 : {danger}</Typography>
              <Typography fontSize={18} sx={{ml : 10, mt : 10, mr : 10}}>{Gu} {Dong}에서 {Sector} 업종 창업은 서울시 내 동종 업종의 평균 추정 매출 대비 {danger}% 낮아요.</Typography>
              <Typography fontSize={18} sx={{ml : 10, mt : 10, mr : 10}}>{Gu} {Dong}에서 {Sector} 업종 창업은 자치구에 비해 매출이 (증가/감소) 추세예요. 인근 지역에 비해 (활성화/ 비활성화) 된 상권이에요. 경쟁 관계에 유의하세요.</Typography>
              <Typography fontSize={18} sx={{ml : 10, mt : 10, mr : 10}}>{Gu} {Dong}에서 {Sector} 업종의 점포수가 전년 동기에 비해 (증가/감소)하고 있어요. 상권이 (발달/쇠퇴)하는 시기인 경우 입지 선정에 신중하셔야 해요.</Typography>
              <Typography fontSize={18} sx={{ml : 10, mt : 10, mr : 10, mb : 10}}>{Gu} {Dong}은 전년 동분기에 비해 유동인구가 [감소]하고 있는 지역이에요. 마케팅이 중요한 상권이에요.</Typography>
            </Box>
            <Box bgcolor={'gray.100'}>
              <Typography fontSize={30} sx={{ml : 10, mt : 10, mr : 10}}>비슷한 지역 추천</Typography>
              <Typography fontSize={18} sx={{ml : 10, mt : 10, mr : 10}}>{Gu} {Dong} {Sector} 업종과 비슷한 추정 매출을 보이는 곳은 {danger}이 있어요.</Typography>

              <Typography fontSize={18} sx={{ml : 10, mt : 10, mr : 10}}>{danger}</Typography>
              <Typography fontSize={18} sx={{ml : 10, mt : 10, mr : 10}}>2023년도 3,4분기 평균 추정 매출</Typography>
              <Typography fontSize={18} sx={{ml : 10, mt : 10, mr : 10}}>XXXX원 yyy원 높아요</Typography>
              <Typography fontSize={18} sx={{ml : 10, mt : 10, mr : 10}}>{danger}</Typography>
              <Typography fontSize={18} sx={{ml : 10, mt : 10, mr : 10}}>2023년도 3,4분기 평균 추정 매출</Typography>
              <Typography fontSize={18} sx={{ml : 10, mt : 10, mr : 10}}>XXXX원 yyy원 높아요</Typography>
            </Box>
            <Box bgcolor={'gray.100'}>
              <Typography fontSize={30} sx={{ml : 10, mt : 10, mr : 10}}>매출 영향 요인 분석</Typography>
              <Typography fontSize={18} sx={{ml : 10, mt : 10, mr : 10}}>SAI로 분석한 name님의 매장의 추정 매출의 영향 요인이에요.</Typography>
              <Typography fontSize={18} sx={{ml : 10, mt : 10, mr : 10}}>graph1, graph2</Typography>
              <Typography fontSize={18} sx={{ml : 10, mt : 10, mr : 10}}>2023년도 3,4분기 평균 추정 매출</Typography>
              <Typography fontSize={18} sx={{ml : 10, mt : 10, mr : 10}}>XXXX원 yyy원 높아요</Typography>
              <Typography fontSize={18} sx={{ml : 10, mt : 10, mr : 10}}>{danger}</Typography>
              <Typography fontSize={18} sx={{ml : 10, mt : 10, mr : 10}}>분석된 파란색blue 요인은 매출을 증가시키는데 기여할 수 있어요.</Typography>
              <Typography fontSize={18} sx={{ml : 10, mt : 10, mr : 10}}>분석된 빨간색red 요인은 매출을 증가시키는데 기여할 수 있어요.</Typography>
            </Box>

            <Box bgcolor={'gray.100'}>
                <Typography fontSize={30} sx={{ml : 10, mt : 10, mr : 10}}>프랜차이즈 창업 비용</Typography>
                <Typography fontSize={18} sx={{ml : 10, mt : 10, mr : 10}}>비슷한 창업 비용으로 가능한 {Sector} 업종 프랜차이즈 목록이에요.</Typography>
              <Box bgcolor={'gray.100'}>
                <Typography fontSize={18} sx={{ml : 10, mt : 10, mr : 10}}>전구 아이콘 참고 도움말</Typography>
                <Typography fontSize={18} sx={{ml : 10, mt : 10, mr : 10}}>좋은 자리라면 평균 임대료에 권리금이 추가로 더 발생할 수 있어요.</Typography>
                <Typography fontSize={18} sx={{ml : 10, mt : 10, mr : 10}}>{Gu} {Dong}의 평균 임대 면적은 ()m^2이고, 평균 임대료는 M^2 당 (얼마)이에요.</Typography>
              </Box>
              <Typography fontSize={18} sx={{ml : 10, mt : 10, mr : 10}}>프랜차이즈1</Typography>
              <Box>
                <Typography fontSize={18} sx={{ml : 10, mt : 10, mr : 10}}>예상 창업 비용</Typography>
                <Typography fontSize={18} sx={{ml : 10, mt : 10, mr : 10}}>(임대료 및 보증금 포함)</Typography>
              </Box>
                <Typography fontSize={18} sx={{ml : 10, mt : 10, mr : 10}}>XXXX원</Typography>
              <Box>
                <DivLine/>
                <Typography fontSize={18} sx={{ml : 10, mt : 10, mr : 10}}>가입비 :</Typography>
                <Typography fontSize={18} sx={{ml : 10, mt : 10, mr : 10}}>분석된 파란색blue 요인은 매출을 증가시키는데 기여할 수 있어요.</Typography>
                <Typography fontSize={18} sx={{ml : 10, mt : 10, mr : 10}}>분석된 빨간색red 요인은 매출을 증가시키는데 기여할 수 있어요.</Typography>
              </Box>
            </Box>
        </Box>
      </Paper>
    </>
  )
}
export default SimulReport

