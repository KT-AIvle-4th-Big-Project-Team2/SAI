import * as React from 'react';
import {
  Box,
  Paper,
  Typography,
  Grid,
  Button,
}
from '@mui/material/'
import DivLine from '../../components/Styles/DivLine';
import { ResponsiveCirclePacking } from '@nivo/circle-packing'
import { ResponsiveBullet } from '@nivo/bullet'
import { ResponsiveBar } from '@nivo/bar'
import { ResponsiveBump } from '@nivo/bump';
import { styled } from '@mui/system';
import { useTheme } from '@mui/material/styles';

const createGradientStyle = (theme) => ({
  background: `linear-gradient(180deg, ${theme.palette.primary.dark} 0%, ${theme.palette.grey[100]} 30%,  ${theme.palette.grey[100]} 30%, ${theme.palette.grey[100]} 100%)`,
  borderRadius: 3,
  padding: theme.spacing(2),
  marginBottom: theme.spacing(4),
  height: 'auto',
});


const StyledPaper = styled(Paper)(({ theme }) => createGradientStyle(theme));


const SimulReport = () => {
  const theme = useTheme();
  const data1 = {
    "name": "nivo",
    "color": "hsl(249, 70%, 50%)",
    "children" : [
    {
      "name": "변수 요인 1",
      "color": "hsl(200, 70%, 50%)",
      "loc": 150
    },
    {
      "name": '변수 요인 2',
      "color": "hsl(200, 70%, 40%)",
      "loc": 90
    },
    {
      "name": '변수 요인 3',
      "color": "hsl(200, 70%, 30%)",
      "loc": 80
    }
  ]
  }
  
  const CircleGraph = () => (
    <div style={{ height: '550px' }}>
    <ResponsiveCirclePacking
      data={data1}
      margin={{ top: 20, right: 20, bottom: 20, left: 20 }}
      id="id"
      value="loc"
      colors={({ depth }) => (depth === 0 ? 'white' : 'hsl(200, 70%, ' + (70 - 20 * depth) + '%)')}
      borderColor={({ depth }) => (depth === 0 ? 'white' : 'hsl(200, 70%, 50%)')}
    />
  </div>
);


  const data2 = [
    {
      "id": '9%',
      "ranges": [0, 100],
      "measures": [50],
      "markers": [null], // markers는 필요에 따라 추가
    },
  ];

  const data3 = [
    { id: 'y1', value: 10, color: 'blue' },
    { id: 'y2', value: 5, color: 'orange' },
    { id: 'y3', value: 2, color: 'gray' },
  ];
  
  const BarGraph = () => (
    <div style={{ height: '450px' }}>
      <ResponsiveBar
        data={data3}
        keys={['value']}
        indexBy="id"
        margin={{ top: 50, right: 60, bottom: 50, left: 60 }}
        padding={0.3}
        colors={(bar) => bar.data.color}
        axisBottom={{
          tickSize: 5,
          tickPadding: 5,
          tickRotation: 0,
        }}
        axisLeft={{
          tickSize: 5,
          tickPadding: 5,
          tickRotation: 0,
        }}
      />
    </div>
  );
  
  const data4 = [
    {
      id: '선택상권',
      data: [
        { x: '2023년 2분기', y: 2000 },
        { x: '2023년 3분기', y: 2500 },
        { x: '2024년 4분기', y: 2000 },
      ],
    },
    {
      id: '자치구',
      data: [
        { x: '2023년 2분기', y: 1000 },
        { x: '2023년 3분기', y: 1200 },
        { x: '2024년 4분기', y: 1100 },
      ],
    },
    {
      id: '서울시',
      data: [
        { x: '2023년 2분기', y: 500 },
        { x: '2023년 3분기', y: 600 },
        { x: '2024년 4분기', y: 700 },
      ],
    },
  ];
  
  const BumpGraph = () => (
    <div style={{ height: '400px' }}>
    <ResponsiveBump
      data={data4}
      margin={{ top: 40, right: 100, bottom: 40, left: 60 }}
      colors={['#6474C8', '#FF6B00', 'gray']}
      lineWidth={3}
      activeLineWidth={6}
      inactiveLineWidth={3}
      inactiveOpacity={0.15}
      pointSize={10}
      activePointSize={16}
      inactivePointSize={0}
      pointColor={{ theme: 'background' }}
      pointBorderWidth={3}
      activePointBorderWidth={3}
      pointBorderColor={{ from: 'serie.color' }}
      axisTop={null}
      axisRight={null}
      axisBottom={{
        tickSize: 5,
        tickPadding: 5,
        tickRotation: 0,
      }}
      axisLeft={{
        tickSize: 5,
        tickPadding: 5,
        tickRotation: 0,
      }}
      legends={[
        {
          anchor: 'bottom-right',
          direction: 'column',
          translateY: 30,
          itemsSpacing: 20,
          itemWidth: 80,
          itemHeight: 20,
          itemTextColor: '#999',
          symbolSize: 12,
          symbolShape: 'circle',
          effects: [
            {
              on: 'hover',
              style: {
                itemTextColor: '#000',
              },
            },
          ],
        },
      ]}
    />
  </div>
  );



  const user = '오진원'
  const da = 
  {
    "행정구": "강남구",
    "행정동": "대치2동",
    "업종": "분식전문점",
    "자본금": 50000,
    "23년도_3분기_추정": 26311165.29,
    "23년도_4분기_예측": 23117808.08,
    "매출_영향_요인": {
    "연령대_50_유동인구_수": 924903558070.8405,
    "프랜차이즈_점포_수": 849707370460.7758,
    "유흥_지출_총금액": 668962936987.3386,
    "아파트_면적_66_제곱미터_미만_세대_수": 663654487872.4412,
    "연령대_10_직장_인구_수": 663071132644.3005
    },
    "시뮬레이션_결과": "bad",
    "평균_추정_매출_대비": [
    66.09290900288883
    ],
    "매출_증감": "감소",  
    "상권_활성": "비활성화",
    "개업_증감": "증가",
    "지역_성장": "발달",
    "유동인구_증감": "증가",
    "유사_행정동1_명": "삼성1동",
    "유사_행정동1_예측": 164482029.68,
    "유사_행정동1_차이": [
    -138170864.39000002
    ],
    "유사_행정동2_명": "명일2동",
    "유사_행정동2_예측": 159672831.6,
    "유사_행정동2_차이": [
    -133361666.31
    ]
    }

  const TitleType = ({children}) => {
    const fontSize = 30;
    const ml = 10;
    const mt = 2;
  
    return (
      <Typography style={{ fontSize, marginLeft: ml, marginTop: mt, fontWeight : 'bold' }}>
        {children}
      </Typography>
    );
  };

  const ContentsType = ({children}) => {
    const fontSize = 20;
    const ml = 10;
    const mt = 2;
  
    return (
      <Typography style={{ fontSize, marginLeft: ml, marginTop: mt }}>
        {children}
      </Typography>
    );
  };
  


  return (
    <div className="container">  
    
    <Button variant='outlined' sx={{mt : 4, color : '#012A5B'}}>분석 보고서</Button><Button variant='contained' sx={{mt : 4, color: '#FFFFFF', backgroundColor: '#012A5B'}}>시뮬레이션 리포트</Button>
      <StyledPaper sx={{ height : 'auto', padding : 3}}>
          <Box sx={{ml: 4, mb: 3, width: 'fit-content', height: 'auto' }}>
            <Typography style={{ fontSize : 40, fontWeight : 'bold' }}><span style={{ color : '#FFFFFF' }}> SAI 창업 시뮬레이션 리포트</span></Typography>
          </Box>
          <Paper border="1px solid black" borderRadius={8} sx={{ height: 'auto', mb: 3, ml : 4, mr : 4, padding : 2}}>
            <TitleType> 선택 값을 반영해 SAI!로 분석한</TitleType>
            <TitleType> {user} 님의 매장의 예상 매출이에요</TitleType>
            <DivLine />
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: 10 }}>
            <Typography fontSize={20} sx={{ml : 20, mt : 5, fontWeight : 'bold'} }>지역 <span style={{ color : '#6474C8', fontStyle: 'italic' }}>{da.행정구} {da.행정동}</span></Typography>
            <Typography fontSize={20} sx={{mt : 5, fontWeight : 'bold'}}>업종 <span style={{ color : '#6474C8', fontStyle: 'italic' }}>{da.업종}</span></Typography>
            <Typography fontSize={20} sx={{mt : 5, mr : 20, fontWeight : 'bold'}}>창업준비금 <span style={{ color : '#6474C8', fontStyle: 'italic' }}>{da.자본금}원</span></Typography>
            </div>
            <BumpGraph />

            <Box>
              <Typography fontSize={30} sx={{ml : 1, mt : 10, mr : 10, fontWeight : 'bold'}}>창업 전망 : {da.시뮬레이션_결과}</Typography>
              <Box bgcolor={'primary.gray'} sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '12vh', marginTop:5,  }}>
              <ResponsiveBullet
                data={data2}
                margin={{left : 10, right : 10, top: 30, bottom: 30}}
                title="Bullet Chart Example"
                rangeColors={['#FACFD5']} // 옅은 분홍색
                measureColors={['blue']} // 파란색
                theme={{ textColor: '#333' }} // 텍스트 색상 지정 (선택사항)
                measureBorderWidth={5}
                rangeBorderWidth={5}
              />
              </Box>
              <Box sx={{ mt : 2, mb : 5}}>
              <ContentsType><span style={{ color : '#6474C8' }}>{da.행정구} {da.행정동}</span>에서 <span style={{ color : '#6474C8' }}>{da.업종}</span> 업종 창업은 <span style={{ fontWeight: 'bold' }}>서울시 내 동종 업종의 평균 추정 매출 대비</span> {da.평균_추정_매출_대비}% 낮아요.</ContentsType>
              <ContentsType><span style={{ color : '#6474C8' }}>{da.행정구} {da.행정동}</span>에서 <span style={{ color : '#6474C8' }}>{da.업종}</span> 업종 창업은 자치구에 비해 매출이 (증가/감소) 추세예요. 인근 지역에 비해 (활성화/ 비활성화) 된 상권이에요. 경쟁 관계에 유의하세요.</ContentsType>
              <ContentsType><span style={{ color : '#6474C8' }}>{da.행정구} {da.행정동}</span>에서 <span style={{ color : '#6474C8' }}>{da.업종}</span> 업종의 점포수가 전년 동기에 비해 (증가/감소)하고 있어요. 상권이 (발달/쇠퇴)하는 시기인 경우 입지 선정에 신중하셔야 해요.</ContentsType>
              <ContentsType><span style={{ color : '#6474C8' }}>{da.행정구} {da.행정동}</span>은 전년 동분기에 비해 유동인구가 [감소]하고 있는 지역이에요. 마케팅이 중요한 상권이에요.</ContentsType>
              </Box>
            </Box>
            <Grid container spacing={2}>
             <Grid item xs={6}>
              <TitleType>비슷한 지역 추천</TitleType>
              <br></br>
              <ContentsType><span style={{ color : '#6474C8' }}>{da.행정구} {da.행정동} {da.업종}</span> 업종과 비슷한 추정 매출을 보이는 곳은 <span style={{ color : '#FF6B00' }}>{da.유사_행정동1_명}, {da.유사_행정동2_명}</span>이 있어요.</ContentsType>
              <br></br>
              <ContentsType><span style={{ fontWeight : 'bold'}}>{da.유사_행정동1_명}</span></ContentsType>
              <br></br>
              <ContentsType>2023년도 3,4분기 평균 추정 매출</ContentsType>
              <ContentsType>XXXX원 yyy원 높아요</ContentsType>
              <br></br>
              <ContentsType><span style={{ fontWeight : 'bold'}}>{da.유사_행정동2_명}</span></ContentsType>
              <br></br>
              <ContentsType>2023년도 3,4분기 평균 추정 매출</ContentsType>
              <ContentsType>XXXX원 yyy원 높아요</ContentsType>
              </Grid>
              <Grid item xs={6}>
                <BarGraph />
              </Grid>
            </Grid>
            <Box sx={{mt : 5}}>
              <TitleType>매출 영향 요인 분석</TitleType>
              <br></br>
              <ContentsType>SAI로 분석한 {user}님의 매장의 추정 매출의 영향 요인이에요.</ContentsType>
              <br></br>
            </Box>
              <CircleGraph />
            <Box>
              <br></br>
              <ContentsType>분석된 <span style={{ color : '#0500FF' }}>파란색</span> 요인은 매출을 증가시키는데 기여할 수 있어요.</ContentsType>
              <ContentsType>분석된 <span style={{ color : '#FF0000' }}>빨간색</span> 요인은 매출을 증가시키는데 기여할 수 있어요.</ContentsType>
              <ContentsType>창업시 매장의 높은 매출을 위해서는 해당 요인들을 관리하는 것을 고려하시는 것이 좋아요.</ContentsType>
            </Box>

            <Box sx={{mt : 10, mb : 10}}>
                <Typography fontSize={30} sx={{ml : 1}}>프랜차이즈 창업 비용</Typography>
                <ContentsType>비슷한 창업 비용으로 가능한 {da.업종} 업종 프랜차이즈 목록이에요.</ContentsType>
              <Box sx = {{bgcolor:'primary.gray', mt : 5, mb : 5}}>
                <br></br>
                <Typography fontSize={23} sx={{ml : 1}}>💡 <span style={{ fontWeight : 'bold'}}>참고 도움말</span></Typography>
                <ContentsType><span style={{ color : '#5F5F5F' }}>좋은 자리라면 평균 임대료에 권리금이 추가로 더 발생할 수 있어요.</span></ContentsType>
                <ContentsType><span style={{ color : '#5F5F5F' }}>{da.행정구} {da.행정동}의 평균 임대 면적은 ()m^2이고, 평균 임대료는 M^2 당 (얼마)이에요.</span></ContentsType>
                <br></br>
              </Box>
            </Box>
        </Paper>
      </StyledPaper>
    </div>
  )
}

export default SimulReport;
