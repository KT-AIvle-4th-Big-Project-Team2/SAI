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


const SimulReport2 = () => {
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
    
    <Button variant='contained' sx={{mt : 4, color: '#FFFFFF', backgroundColor: '#012A5B'}}>분석 보고서</Button><Button variant='outlined' sx={{mt : 4, color : '#012A5B'}}>시뮬레이션 리포트</Button>
      <StyledPaper sx={{ height : 'auto', padding : 3}}>
          <Box sx={{ml: 4, mb: 3, width: 'fit-content', height: 'auto' }}>
            <Typography style={{ fontSize : 40, fontWeight : 'bold' }}><span style={{ color : '#FFFFFF' }}> SAI 창업 분석 보고서</span></Typography>
          </Box>
          <Paper border="1px solid black" sx={{ height: 'auto', mb: 3, ml : 4, mr : 4, padding : 2}}>
            <TitleType> 선택 값을 반영해 SAI!로 분석한</TitleType>
            <TitleType><span style={{ color : '#6474C8' }}>{da.행정구} {da.행정동} {da.업종}</span> 업종의 매장의 예상 매출이에요</TitleType>
            <DivLine />

            <Box sx={{ bgcolor: 'primary.gray', mt : 2, mb : 5}}>
            <TitleType>종합 의견</TitleType>
            <ContentsType><span style={{ color : '#6474C8' }}>{da.행정구} {da.행정동}</span>에서 <span style={{ color : '#6474C8' }}>{da.업종}</span> 업종 점포수는 전년 동기에 비해 (증가/감소)하고 있어요. 상권이 (발달/쇠퇴)하는 시기의 경우 입지 선정에 신중하셔야 해요.</ContentsType>
            <ContentsType><span style={{ color : '#6474C8' }}>{da.행정구} {da.행정동}</span>은 자치구에서 매출이 (증가/감소) 추세예요. 평균 임대 시세 등 고정 비용에 대한 관리가 중요해요.</ContentsType>
            <ContentsType><span style={{ color : '#6474C8' }}>{da.행정구} {da.행정동}</span>은 전년 동 분기에 비해 유동인구가 (증가/감소)하고 있는 지역입니다. 마케팅이 중요한 상권이에요.</ContentsType>
            <ContentsType><span style={{ color : '#6474C8' }}>{da.행정구} </span>는 행정동 (n)개 중 <span style={{ color : '#6474C8' }}>{da.행정동}</span>의 점포 수는 (0)위, 매출액 (0)위, 유동인구 (0)위에요.</ContentsType>
            </Box>
            <Grid container spacing={3}>
             <Grid item xs={4}>
                <Box border="1px solid black" sx={{padding : 3}}>
                    <TitleType>점포수</TitleType>
                    <br></br>
                    <Box sx={{bgcolor : 'primary.pink', height : '100px', padding : 2}}>
                    <Typography sx={{ textAlign: 'center', fontWeight: 'bold', fontSize: 20 }}><span style={{ color: 'white' }}>전 분기 대비</span></Typography>
                    <Typography sx={{ textAlign: 'center', fontWeight: 'bold', fontSize: 30 }}><span style={{ color: 'white' }}>+ 11개</span></Typography>
                    </Box>
                    <Box sx={{bgcolor : 'primary.gray', height : '100px', padding : 2, marginTop : 2}}>
                    <Typography sx={{ textAlign: 'center', fontWeight: 'bold', fontSize: 20 }}><span style={{ color: 'black' }}>2023년 3분기</span></Typography>
                    <Typography sx={{ textAlign: 'center', fontWeight: 'bold', fontSize: 30 }}><span style={{ color: 'black' }}>800개</span></Typography>
                    </Box>
                    <Box sx={{bgcolor : 'primary.pink', height : '100px', padding : 2, marginTop : 2}}>
                    <Typography sx={{ textAlign: 'center', fontWeight: 'bold', fontSize: 20 }}><span style={{ color: 'white' }}>전년 동분기 대비</span></Typography>
                    <Typography sx={{ textAlign: 'center', fontWeight: 'bold', fontSize: 30 }}><span style={{ color: 'white' }}>+ 9개</span></Typography>
                    </Box>
                    <Box sx={{display: 'flex', justifyContent: 'space-between', mt: 2}}>
                    <Typography sx={{ fontWeight: 'bold', fontSize: 15 }}><span style={{ color: 'black' }}>나의 등수</span></Typography>
                    <Typography sx={{ fontWeight: 'bold', fontSize: 15 }}><span style={{ color: 'black' }}>10 / 16위</span></Typography>
                    </Box>
                </Box>
              </Grid>
              <Grid item xs={4}>
              <Box border="1px solid black" sx={{padding : 3}}>
                    <TitleType>매출액</TitleType>
                    <br></br>
                    <Box sx={{bgcolor : 'primary.blue', height : '100px', padding : 2}}>
                    <Typography sx={{ textAlign: 'center', fontWeight: 'bold', fontSize: 20 }}><span style={{ color: 'white' }}>전 분기 대비</span></Typography>
                    <Typography sx={{ textAlign: 'center', fontWeight: 'bold', fontSize: 30 }}><span style={{ color: 'white' }}>- 11개</span></Typography>
                    </Box>
                    <Box sx={{bgcolor : 'primary.gray', height : '100px', padding : 2, marginTop : 2}}>
                    <Typography sx={{ textAlign: 'center', fontWeight: 'bold', fontSize: 20 }}><span style={{ color: 'black' }}>2023년 3분기</span></Typography>
                    <Typography sx={{ textAlign: 'center', fontWeight: 'bold', fontSize: 30 }}><span style={{ color: 'black' }}>만원</span></Typography>
                    </Box>
                    <Box sx={{bgcolor : 'primary.blue', height : '100px', padding : 2, marginTop : 2}}>
                    <Typography sx={{ textAlign: 'center', fontWeight: 'bold', fontSize: 20 }}><span style={{ color: 'white' }}>전년 동분기 대비</span></Typography>
                    <Typography sx={{ textAlign: 'center', fontWeight: 'bold', fontSize: 30 }}><span style={{ color: 'white' }}>만원</span></Typography>
                    </Box>
                    <Box sx={{display: 'flex', justifyContent: 'space-between', mt: 2}}>
                    <Typography sx={{ fontWeight: 'bold', fontSize: 15 }}><span style={{ color: 'black' }}>나의 등수</span></Typography>
                    <Typography sx={{ fontWeight: 'bold', fontSize: 15 }}><span style={{ color: 'black' }}>12 / 16위</span></Typography>
                    </Box>
                </Box>
              </Grid>
              <Grid item xs={4}>
              <Box border="1px solid black" sx={{padding : 3}}>
                    <TitleType>점포수</TitleType>
                    <br></br>
                    <Box sx={{bgcolor : 'primary.blue', height : '100px', padding : 2}}>
                    <Typography sx={{ textAlign: 'center', fontWeight: 'bold', fontSize: 20 }}><span style={{ color: 'white' }}>전 분기 대비</span></Typography>
                    <Typography sx={{ textAlign: 'center', fontWeight: 'bold', fontSize: 30 }}><span style={{ color: 'white' }}>+ 11명</span></Typography>
                    </Box>
                    <Box sx={{bgcolor : 'primary.gray', height : '100px', padding : 2, marginTop : 2}}>
                    <Typography sx={{ textAlign: 'center', fontWeight: 'bold', fontSize: 20 }}><span style={{ color: 'black' }}>2023년 3분기</span></Typography>
                    <Typography sx={{ textAlign: 'center', fontWeight: 'bold', fontSize: 30 }}><span style={{ color: 'black' }}>800ha / 명</span></Typography>
                    </Box>
                    <Box sx={{bgcolor : 'primary.blue', height : '100px', padding : 2, marginTop : 2}}>
                    <Typography sx={{ textAlign: 'center', fontWeight: 'bold', fontSize: 20 }}><span style={{ color: 'white' }}>전년 동분기 대비</span></Typography>
                    <Typography sx={{ textAlign: 'center', fontWeight: 'bold', fontSize: 30 }}><span style={{ color: 'white' }}>- 9명</span></Typography>
                    </Box>
                    <Box sx={{display: 'flex', justifyContent: 'space-between', mt: 2}}>
                    <Typography sx={{ fontWeight: 'bold', fontSize: 15 }}><span style={{ color: 'black' }}>나의 등수</span></Typography>
                    <Typography sx={{ fontWeight: 'bold', fontSize: 15 }}><span style={{ color: 'black' }}>10 / 16위</span></Typography>
                    </Box>
                </Box>
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

export default SimulReport2;
