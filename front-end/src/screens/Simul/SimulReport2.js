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
import { ResponsivePie } from '@nivo/pie'
import { ResponsiveBar } from '@nivo/bar'
import { ResponsiveLine } from '@nivo/line'
import { styled } from '@mui/system';
import { useTheme } from '@mui/material/styles';

const createGradientStyle = (theme) => ({
  background: `linear-gradient(180deg, ${theme.palette.primary.dark} 0%, ${theme.palette.grey[100]} 30%,  ${theme.palette.grey[100]} 30%, ${theme.palette.grey[100]} 100%)`,
});


const StyledPaper = styled(Paper)(({ theme }) => createGradientStyle(theme));


const SimulReport2 = () => {
  const theme = useTheme();

  const stores = [
    { id: '2022년 3분기', value: 872, color: '#9B9B9B' },
    { id: '2022년 4분기', value: 882, color: '#9B9B9B' },
    { id: '2023년 1분기', value: 881, color: '#9B9B9B' },
    { id: '2023년 2분기', value: 889, color: '#9B9B9B' },
    { id: '2023년 3분기', value: 895, color: '#236cff' },
  ];
  
  const StoreGraph = () => (
    <div style={{ height: '300px' }}>
      <ResponsiveBar
        data={stores}
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

  const opens = [
    { id: '2022년 3분기', value: 872, color: '#9B9B9B' },
    { id: '2022년 4분기', value: 882, color: '#9B9B9B' },
    { id: '2023년 1분기', value: 881, color: '#9B9B9B' },
    { id: '2023년 2분기', value: 889, color: '#9B9B9B' },
    { id: '2023년 3분기', value: 895, color: '#236cff' },
  ];
  
  const OpenGraph = () => (
    <div style={{ height: '300px' }}>
      <ResponsiveBar
        data={opens}
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

  const closes = [
    { id: '2022년 3분기', value: 872, color: '#9B9B9B' },
    { id: '2022년 4분기', value: 882, color: '#9B9B9B' },
    { id: '2023년 1분기', value: 881, color: '#9B9B9B' },
    { id: '2023년 2분기', value: 889, color: '#9B9B9B' },
    { id: '2023년 3분기', value: 895, color: '#236cff' },
  ];
  
  const CloseGraph = () => (
    <div style={{ height: '300px' }}>
      <ResponsiveBar
        data={closes}
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

  const risidals = [
    { id: '2022년 3분기', value: 872, color: '#9B9B9B' },
    { id: '2022년 4분기', value: 882, color: '#9B9B9B' },
    { id: '2023년 1분기', value: 881, color: '#9B9B9B' },
    { id: '2023년 2분기', value: 889, color: '#9B9B9B' },
    { id: '2023년 3분기', value: 895, color: '#236cff' },
  ];

  const ResidalGraph = () => (
    <div style={{ height: '300px' }}>
      <ResponsiveBar
        data={risidals}
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

  const sectordata = [
    { id: '관공서', value: 6, color: '#236cff' },
    { id: '금융기관', value: 3, color: '#236cff' },
    { id: '병원', value: 4, color: '#236cff' },
    { id: '학교', value: 14, color: '#236cff' },
    { id: '유통점', value: 0, color: '#236cff' },
    { id: '극장', value: 0, color: '#236cff' },
    { id: '숙박시설', value: 0, color: '#236cff' },
    { id: '교통시설', value: 26, color: '#236cff' },
  ];
  
  const SectorGraph = () => (
    <div style={{ height: '300px' }}>
      <ResponsiveBar
        data={sectordata}
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

  const peopledata = [
    {
        id: '서울시',
        data: [
          { x: '2022년 3분기', y: 159 },
          { x: '2022년 4분기', y: 155 },
          { x: '2023년 1분기', y: 155 },
          { x: '2023년 2분기', y: 155 },
          { x: '2023년 3분기', y: 154 },
        ],
      },
      
    {
        id: '자치구',
        data: [
          { x: '2022년 3분기', y: 63 },
          { x: '2022년 4분기', y: 62 },
          { x: '2023년 1분기', y: 61 },
          { x: '2023년 2분기', y: 60 },
          { x: '2023년 3분기', y: 51 },
        ],
      },
    {
      id: '선택상권',
      data: [
        { x: '2022년 3분기', y: 51 },
        { x: '2022년 4분기', y: 54 },
        { x: '2023년 1분기', y: 52 },
        { x: '2023년 2분기', y: 66 },
        { x: '2023년 3분기', y: 55 },
      ],
    }
  ];


  
const BumpGraph = () => (
    <div style={{ height: '300px' }}>
    <Box sx={{display : 'flex', justifyContent : 'space-between', mt : 2, ml : 2, mr : 10}}>
        <Typography sx={{fontSize : 20, fontWeight : 'bold'}}>주거 공간 추이</Typography>
        <Typography sx={{fontSize : 18}}>단위 : 1ha 당 명</Typography>
    </Box>
    <ResponsiveLine
      data={peopledata}
      margin={{ top: 40, right: 100, bottom: 70, left: 60 }}
      colors={['#6474C8', '#FF6B00', 'gray']}
      lineWidth={3}
      pointSize={10}
      pointColor={{ theme: 'background' }}
      pointBorderWidth={3}
      pointBorderColor={{ from: 'serieColor' }}
      enablePoints={true}
      enableGridX={true}
      enableGridY={true}
      curve="monotoneX"
      axisTop={null}
      axisRight={null}
      axisLeft={{
        tickSize: 5,
        tickPadding: 5,
        tickRotation: 0,
      }}
      legends={[
        {
          anchor: 'bottom',
          direction: 'row',
          translateY: 50,
          itemsSpacing: 20,
          itemWidth: 80,
          itemHeight: 20,
          itemTextColor: '#999',
          symbolSize: 12,
          symbolShape: 'circle',
        }
          ]}
      
    />
  </div>
);

    const consume = [
        { id: 'Category 1', label: 'Category 1', value: 35 },
        { id: 'Category 2', label: 'Category 2', value: 27 },
        { id: 'Category 3', label: 'Category 3', value: 6 },
        { id: 'Category 4', label: 'Category 4', value: 5 },
        { id: 'Category 5', label: 'Category 5', value: 2 },
    ];

    const PieGraph = () => (
    <div style={{ height: '350px', marginTop : '20px' }}>
        <ResponsivePie
        margin={{ top: 50, right: 80, bottom: 100, left: 80 }}
        data={consume}
        sortByValue={true} // 크기순으로 정렬
        innerRadius={0} // 내부 공간을 채우는 비율 (0.5는 반원 형태)
        padAngle={0.1} // 데이터 사이의 간격
        enableArcLinkLabels={false}
        colors={{ scheme: 'category10' }}
        radialLabel="label" // 중앙 범주 텍스트는 데이터의 'label' 속성 사용
        radialLabelsLinkHorizontalLength={10} // 중앙 범주와 그래프 간의 가로 길이
        radialLabelsLinkDiagonalLength={12} // 중앙 범주와 그래프 간의 대각선 길이
        radialLabelsTextXOffset={6} // 중앙 범주 텍스트의 X 오프셋
        radialLabelsTextColor="#333" // 중앙 범주 텍스트 색상
        radialLabelsLinkColor="#666" // 중앙 범주와 그래프 간의 선 색상
        legends={[
            {
                anchor: 'bottom',
                direction: 'row',
                justify: false,
                translateX: 0,
                translateY: 50,
                itemsSpacing: 0,
                itemWidth: 100,
                itemHeight: 18,
                itemTextColor: '#999',
                itemDirection: 'left-to-right',
                itemOpacity: 1,
                symbolSize: 18,
                symbolShape: 'circle',
                effects: [
                    {
                        on: 'hover',
                        style: {
                            itemTextColor: '#000'
                        }
                    }
                ]
            }
        ]}
        />
    </div>
    )



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
    const ml = 0;
    const mt = 2;
  
    return (
      <Typography style={{ fontSize, marginLeft: ml, marginTop: mt, fontWeight : 'bold' }}>
        {children}
      </Typography>
    );
  };

  const ContentsType = ({children}) => {
    const fontSize = 20;
    const ml = 0;
    const mt = 2;
  
    return (
      <Typography style={{ fontSize, marginLeft: ml, marginTop: mt }}>
        {children}
      </Typography>
    );
  };
  


  return (
    <div className="container">  
    
    <Button variant='outlined' sx={{mt : 4, color: '#ffffff', paddingY: 1, borderRadius: 0, width : '150px', bgcolor:"#012A5B"}}><span style={{fontSize : 18}}>분석 보고서</span></Button>
    <Button variant='contained' href= '/SimulReport' sx={{mt : 4, color : '#FFFFFF', bgcolor : '#C5C1C1',  paddingY: 1, borderRadius: 0}}><span style={{fontSize : 18}}>시뮬레이션 리포트</span></Button>
      <StyledPaper sx={{ height : 'auto', padding : 5, minWidth : '1200px'}}>
          <Box sx={{ml: 4, mb: 3, width: 'fit-content', height: 'auto' }}>
            <Typography style={{ fontSize : 40, fontWeight : 'bold' }}><span style={{ color : '#FFFFFF' }}> SAI 창업 분석 보고서</span></Typography>
          </Box>
          <Paper border="1px solid black" sx={{ height: 'auto', mb: 3, ml : 4, mr : 4, padding : 8, borderRadius: 8}}>
            <TitleType> 선택 값을 반영해 SAI로 분석한</TitleType>
            <TitleType><span style={{ color : '#6474C8' }}>{da.행정구} {da.행정동} {da.업종}</span> 업종의 분석 보고서에요.</TitleType>
            <DivLine />

            <TitleType>종합 의견</TitleType>
            <Box sx={{ bgcolor: 'primary.gray', mt : 2, mb : 5, padding : 3, borderRadius : 3}}>
            <ContentsType><span style={{ color : '#6474C8', fontWeight : 'bold' }}>{da.행정구} {da.행정동}</span>에서 <span style={{ color : '#6474C8', fontWeight : 'bold'  }}>{da.업종}</span> 업종 <span style={{ fontWeight: 'bold' }}>점포수</span>는 전년 동기에 비해 <span style={{ fontWeight: 'bold', color:'#236cff'}}>(증가/감소)</span>하고 있어요. 상권이 <span style={{ fontWeight: 'bold', color:'#236cff'}}>(발달/쇠퇴)</span>하는 시기의 경우 입지 선정에 신중하셔야 해요.</ContentsType>
            <ContentsType><span style={{ color : '#6474C8', fontWeight : 'bold' }}>{da.행정구} {da.행정동}</span>은 자치구에서 <span style={{ fontWeight: 'bold' }}>매출</span>이 <span style={{ fontWeight: 'bold', color:'#236cff'}}>(증가/감소)</span> 추세예요. 평균 임대 시세 등 고정 비용에 대한 관리가 중요해요.</ContentsType>
            <ContentsType><span style={{ color : '#6474C8', fontWeight : 'bold' }}>{da.행정구} {da.행정동}</span>은 전년 동 분기에 비해 <span style={{ fontWeight: 'bold' }}>유동인구</span>가 <span style={{ fontWeight: 'bold', color:'#236cff'}}>(증가/감소)</span>하고 있는 지역입니다. 마케팅이 중요한 상권이에요.</ContentsType>
            <ContentsType><span style={{ color : '#6474C8', fontWeight : 'bold' }}>{da.행정구} </span> 행정동 <span style={{ fontWeight: 'bold' }}>(n)개 </span>중 <span style={{ color : '#6474C8', fontWeight : 'bold'  }}>{da.행정동}</span>의 <span style={{ fontWeight: 'bold' }}>점포 수는 (0)위, 매출액 (0)위, 유동인구 (0)위</span>에요.</ContentsType>
            </Box>
            <Grid container spacing={3}>
             <Grid item xs={4}>
                <Box  sx={{padding : 3}}>
                    <TitleType>점포수</TitleType>
                    <br></br>
                    <Box sx={{bgcolor : 'primary.pink', height : '100px', padding : 2, borderRadius : 3}}>
                    <Typography sx={{ textAlign: 'center', fontWeight: 'bold', fontSize: 20 }}><span style={{ color: 'white' }}>전 분기 대비</span></Typography>
                    <Typography sx={{ textAlign: 'center', fontWeight: 'bold', fontSize: 30 }}><span style={{ color: 'white' }}>+ 11개</span></Typography>
                    </Box>
                    <Box sx={{bgcolor : 'primary.gray', height : '100px', padding : 2, marginTop : 2, borderRadius : 3}}>
                    <Typography sx={{ textAlign: 'center', fontWeight: 'bold', fontSize: 20 }}><span style={{ color: 'black' }}>2023년 3분기</span></Typography>
                    <Typography sx={{ textAlign: 'center', fontWeight: 'bold', fontSize: 30 }}><span style={{ color: 'black' }}>800개</span></Typography>
                    </Box>
                    <Box sx={{bgcolor : 'primary.pink', height : '100px', padding : 2, marginTop : 2, borderRadius : 3}}>
                    <Typography sx={{ textAlign: 'center', fontWeight: 'bold', fontSize: 20 }}><span style={{ color: 'white' }}>전년 동분기 대비</span></Typography>
                    <Typography sx={{ textAlign: 'center', fontWeight: 'bold', fontSize: 30 }}><span style={{ color: 'white' }}>+ 9개</span></Typography>
                    </Box>
                    <Box sx={{display: 'flex', justifyContent: 'space-between', mt: 2, borderRadius : 3}}>
                    <Typography sx={{ fontWeight: 'bold', fontSize: 15 }}><span style={{ color: 'black' }}>나의 등수</span></Typography>
                    <Typography sx={{ fontWeight: 'bold', fontSize: 15 }}><span style={{ color: 'black' }}>10 / 16위</span></Typography>
                    </Box>
                </Box>
              </Grid>
              <Grid item xs={4}>
              <Box  sx={{padding : 3}}>
                    <TitleType>매출액</TitleType>
                    <br></br>
                    <Box sx={{bgcolor : 'primary.blue', height : '100px', padding : 2, borderRadius : 3}}>
                    <Typography sx={{ textAlign: 'center', fontWeight: 'bold', fontSize: 20 }}><span style={{ color: 'white' }}>전 분기 대비</span></Typography>
                    <Typography sx={{ textAlign: 'center', fontWeight: 'bold', fontSize: 30 }}><span style={{ color: 'white' }}>- 11개</span></Typography>
                    </Box>
                    <Box sx={{bgcolor : 'primary.gray', height : '100px', padding : 2, marginTop : 2, borderRadius : 3}}>
                    <Typography sx={{ textAlign: 'center', fontWeight: 'bold', fontSize: 20 }}><span style={{ color: 'black' }}>2023년 3분기</span></Typography>
                    <Typography sx={{ textAlign: 'center', fontWeight: 'bold', fontSize: 30 }}><span style={{ color: 'black' }}>만원</span></Typography>
                    </Box>
                    <Box sx={{bgcolor : 'primary.blue', height : '100px', padding : 2, marginTop : 2, borderRadius : 3}}>
                    <Typography sx={{ textAlign: 'center', fontWeight: 'bold', fontSize: 20 }}><span style={{ color: 'white' }}>전년 동분기 대비</span></Typography>
                    <Typography sx={{ textAlign: 'center', fontWeight: 'bold', fontSize: 30 }}><span style={{ color: 'white' }}>만원</span></Typography>
                    </Box>
                    <Box sx={{display: 'flex', justifyContent: 'space-between', mt: 2, borderRadius : 3}}>
                    <Typography sx={{ fontWeight: 'bold', fontSize: 15 }}><span style={{ color: 'black' }}>나의 등수</span></Typography>
                    <Typography sx={{ fontWeight: 'bold', fontSize: 15 }}><span style={{ color: 'black' }}>12 / 16위</span></Typography>
                    </Box>
                </Box>
              </Grid>
              <Grid item xs={4}>
              <Box  sx={{padding : 3}}>
                    <TitleType>점포수</TitleType>
                    <br></br>
                    <Box sx={{bgcolor : 'primary.blue', height : '100px', padding : 2, borderRadius : 3}}>
                    <Typography sx={{ textAlign: 'center', fontWeight: 'bold', fontSize: 20 }}><span style={{ color: 'white' }}>전 분기 대비</span></Typography>
                    <Typography sx={{ textAlign: 'center', fontWeight: 'bold', fontSize: 30 }}><span style={{ color: 'white' }}>+ 11명</span></Typography>
                    </Box>
                    <Box sx={{bgcolor : 'primary.gray', height : '100px', padding : 2, marginTop : 2, borderRadius : 3}}>
                    <Typography sx={{ textAlign: 'center', fontWeight: 'bold', fontSize: 20 }}><span style={{ color: 'black' }}>2023년 3분기</span></Typography>
                    <Typography sx={{ textAlign: 'center', fontWeight: 'bold', fontSize: 30 }}><span style={{ color: 'black' }}>800ha / 명</span></Typography>
                    </Box>
                    <Box sx={{bgcolor : 'primary.blue', height : '100px', padding : 2, marginTop : 2, borderRadius : 3}}>
                    <Typography sx={{ textAlign: 'center', fontWeight: 'bold', fontSize: 20 }}><span style={{ color: 'white' }}>전년 동분기 대비</span></Typography>
                    <Typography sx={{ textAlign: 'center', fontWeight: 'bold', fontSize: 30 }}><span style={{ color: 'white' }}>- 9명</span></Typography>
                    </Box>
                    <Box sx={{display: 'flex', justifyContent: 'space-between', mt: 2, borderRadius : 3}}>
                    <Typography sx={{ fontWeight: 'bold', fontSize: 15 }}><span style={{ color: 'black'}}>나의 등수</span></Typography>
                    <Typography sx={{ fontWeight: 'bold', fontSize: 15 }}><span style={{ color: 'black'}}>10 / 16위</span></Typography>
                    </Box>
                </Box>
              </Grid>
            </Grid>

            <Box sx={{mt : 15}}>
              <TitleType>Best 매출</TitleType>
              <Grid container>
              <Grid item xs={4}>
                <Box sx={{ padding: 3, mt: 3, mb : 3, height: '250px', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}>
                    <Box border="1px solid gray" sx={{ width: '200px', height: '60px', padding: 2, borderRadius: 8, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}>
                    <Typography sx={{ textAlign: 'center', fontWeight: 'bold', fontSize: 20 }}>
                        <span style={{ color: 'gray' }}>성별 / 연령대</span>
                    </Typography>
                    </Box>
                    <br />
                    <Typography sx={{ textAlign: 'center', fontWeight: 'bold', fontSize: 30, color: '#236cff' }}>
                    여성 / 40대
                    </Typography>
                </Box>
                </Grid>
                <Grid item xs={4}>
                <Box  sx={{ padding: 3, mt: 3, mb : 3, height: '250px', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}>
                    <Box border="1px solid gray" sx={{ width: '200px', height: '60px', padding: 2, borderRadius: 8, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}>
                    <Typography sx={{ textAlign: 'center', fontWeight: 'bold', fontSize: 20 }}>
                        <span style={{ color: 'gray' }}>요일</span>
                    </Typography>
                    </Box>
                    <br />
                    <Typography sx={{ textAlign: 'center', fontWeight: 'bold', fontSize: 30, color: '#236cff' }}>
                    목요일(24.3%)
                    </Typography>
                </Box>
                </Grid>
                <Grid item xs={4}>
                <Box sx={{ padding: 3, mt: 3, mb : 3, height: '250px', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}>
                    <Box border="1px solid gray" sx={{ width: '200px', height: '60px', padding: 2, borderRadius: 8, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}>
                    <Typography sx={{ textAlign: 'center', fontWeight: 'bold', fontSize: 20 }}>
                        <span style={{ color: 'gray' }}>시간대</span>
                    </Typography>
                    </Box>
                    <br />
                    <Typography sx={{ textAlign: 'center', fontWeight: 'bold', fontSize: 30, color: '#236cff' }}>
                    14 ~ 17시
                    </Typography>
                </Box>
                </Grid>
              </Grid>
            </Box>


            <Box sx={{mt : 10}}>
              <TitleType>Best 유동인구</TitleType>
              <Grid container spacing={3}>
              <Grid item xs={3}>
                <Box sx={{ padding: 3, mt: 3, mb : 3, height: '250px', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}>
                    <Box border="1px solid gray" sx={{ width: '200px', height: '60px', padding: 2, borderRadius: 8, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}>
                    <Typography sx={{ textAlign: 'center', fontWeight: 'bold', fontSize: 20 }}>
                        <span style={{ color: 'gray' }}>성별</span>
                    </Typography>
                    </Box>
                    <br />
                    <Typography sx={{ textAlign: 'center', fontWeight: 'bold', fontSize: 30, color: '#236cff' }}>
                    여성
                    </Typography>
                </Box>
                </Grid>
                <Grid item xs={3}>
                <Box  sx={{ padding: 3, mt: 3, mb : 3, height: '250px', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}>
                    <Box border="1px solid gray" sx={{ width: '200px', height: '60px', padding: 2, borderRadius: 8, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}>
                    <Typography sx={{ textAlign: 'center', fontWeight: 'bold', fontSize: 20 }}>
                        <span style={{ color: 'gray' }}>요일</span>
                    </Typography>
                    </Box>
                    <br />
                    <Typography sx={{ textAlign: 'center', fontWeight: 'bold', fontSize: 30, color: '#236cff' }}>
                    목요일
                    </Typography>
                </Box>
                </Grid>
                <Grid item xs={3}>
                <Box sx={{ padding: 3, mt: 3, mb : 3, height: '250px', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}>
                    <Box border="1px solid gray" sx={{ width: '200px', height: '60px', padding: 2, borderRadius: 8, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}>
                    <Typography sx={{ textAlign: 'center', fontWeight: 'bold', fontSize: 20 }}>
                        <span style={{ color: 'gray' }}>시간대</span>
                    </Typography>
                    </Box>
                    <br />
                    <Typography sx={{ textAlign: 'center', fontWeight: 'bold', fontSize: 30, color: '#236cff' }}>
                    14 ~ 17시
                    </Typography>
                </Box>
                </Grid>
                <Grid item xs={3}>
                <Box  sx={{ padding: 3, mt: 3, mb : 3, height: '250px', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}>
                    <Box border="1px solid gray" sx={{ width: '200px', height: '60px', padding: 2, borderRadius: 8, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}>
                    <Typography sx={{ textAlign: 'center', fontWeight: 'bold', fontSize: 20 }}>
                        <span style={{ color: 'gray' }}>시간대</span>
                    </Typography>
                    </Box>
                    <br />
                    <Typography sx={{ textAlign: 'center', fontWeight: 'bold', fontSize: 30, color: '#236cff' }}>
                    14 ~ 17시
                    </Typography>
                </Box>
                </Grid>
              </Grid>
            </Box>

            <Box sx={{mt : 15}}>
              <TitleType>점포 수</TitleType>
              <Box sx={{mt : 3}}>
                    <Typography style={{ fontSize: '23px'}}>선택하신 지역의 <span style={{ color : '#6474C8', fontWeight : 'bold' }}>{da.업종}</span> 업종의 점포수는 <span style={{ color: '#6474C8', fontWeight : 'bold' }}>895개</span>가 있어요.</Typography>
                <Box border="1px solid gray" sx={{mt : 2, display: 'flex', justifyContent: 'space-between', borderRadius : 1, padding:.5}}>
                    <Typography sx={{ ml : 20, fontSize: 20 }}><span style={{ color: '#5F5F5F' }}>전년 동분기 대비</span><span style={{ color: '#FF6B00', fontWeight : 'bold' }}> n개</span></Typography>
                    <Typography sx={{ mr : 20, fontSize: 20 }}><span style={{ color: '#5F5F5F' }}>전분기 대비</span><span style={{ color: '#FF6B00', fontWeight : 'bold' }}> n개</span></Typography>
                </Box>                
                <Box border="1px solid gray" sx={{mt : 2, borderRadius : 1, padding:.5}}>
                    <Typography sx={{ ml : 5, fontSize: 20, textAlign: 'center' }}><span style={{ color: '#6474C8', fontWeight : 'bold'}}>{da.지역구} {da.행정동}</span>에서 <span style={{ color: '#6474C8', fontWeight : 'bold'  }}>{da.업종}</span> 점포 수가 전년 동기에 비해 <span style={{ fontWeight: 'bold', color:'#236cff'}}>(증가/감소)</span> 하고 있어요.</Typography>
                    <Typography sx={{ ml : 5, fontSize: 20, textAlign: 'center' }}><span style={{ color: '#000000' }}>상권이 <span style={{ fontWeight: 'bold', color:'#236cff'}}>(발달/쇠퇴)</span>하는 시기인 경우 입지 선정에 신중하셔야 해요.</span></Typography>
                </Box>
                <StoreGraph />
              </Box>
            </Box>
            <Box sx={{mt : 15}}>
              <TitleType>개업 수</TitleType>
              <Box sx={{mt : 3}}>
                    <Typography style={{ fontSize: '23px'}}>선택하신 지역의 <span style={{ color : '#6474C8', fontWeight : 'bold'}}>{da.업종}</span> 업종의 개업한 점포수는 <span style={{ color: '#6474C8', fontWeight : 'bold' }}>895개</span>가 있어요.</Typography>
                <Box border="1px solid gray" sx={{mt : 2, display: 'flex', justifyContent: 'space-between', borderRadius : 1, padding:.5}}>
                    <Typography sx={{ ml : 20, fontSize: 20 }}><span style={{ color: '#5F5F5F' }}>전년 동분기 대비</span><span style={{ color: '#FF6B00', fontWeight : 'bold' }}> n개</span></Typography>
                    <Typography sx={{ mr : 20, fontSize: 20 }}><span style={{ color: '#5F5F5F' }}>전분기 대비</span><span style={{ color: '#FF6B00', fontWeight : 'bold' }}> n개</span></Typography>
                </Box>              
                <Box border="1px solid gray" sx={{mt : 2, borderRadius : 1, padding:.5}}>
                    <Typography sx={{ ml : 5, fontSize: 20, textAlign: 'center' }}><span style={{ color: '000000' }}>전분기 대비 개업 업소수는 <span style={{ fontWeight: 'bold', color:'#236cff'}}>(증가/감소)</span>, 폐업수는 <span style={{ fontWeight: 'bold', color:'#236cff'}}>(증가/감소)</span> 하고 있어요.</span></Typography>
                    <Typography sx={{ ml : 5, fontSize: 20, textAlign: 'center' }}><span style={{ color: '000000' }}>상권 변화가 <span style={{ fontWeight: 'bold', color:'#236cff'}}>(활발하/침체되)</span>고 유동적이에요. 입지 선정에 유의하세요!</span></Typography>
                </Box>
                <OpenGraph />
            </Box>
            </Box>
            <Box sx={{mt : 15}}>
              <TitleType>폐업 수</TitleType>
              <Box sx={{mt : 3}}>
              <Typography style={{ fontSize: '23px'}}>선택하신 지역의 <span style={{ color : '#6474C8', fontWeight : 'bold' }}>{da.업종}</span> 업종의 폐업한 점포수는 <span style={{ color: '#6474C8', fontWeight : 'bold' }}>895개</span>가 있어요.</Typography>                    
              <Box border="1px solid gray" sx={{mt : 2, display: 'flex', justifyContent: 'space-between', borderRadius : 1, padding:.5}}>
                    <Typography sx={{ ml : 20, fontSize: 20 }}><span style={{ color: '#5F5F5F' }}>전년 동분기 대비</span><span style={{ color: '#FF6B00', fontWeight : 'bold' }}> n개</span></Typography>
                    <Typography sx={{ mr : 20, fontSize: 20 }}><span style={{ color: '#5F5F5F' }}>전분기 대비</span><span style={{ color: '#FF6B00', fontWeight : 'bold' }}> n개</span></Typography>
                </Box>                
                <Box border="1px solid gray" sx={{mt : 2, borderRadius : 1, padding:.5}}>
                    <Typography sx={{ ml : 5, fontSize: 20, textAlign: 'center' }}><span style={{ color: '000000' }}>전분기 대비 개업 업소수는 <span style={{ fontWeight: 'bold', color:'#236cff'}}>(증가/감소)</span>, 폐업수는 <span style={{ fontWeight: 'bold', color:'#236cff'}}>(증가/감소)</span> 하고 있어요.</span></Typography>
                    <Typography sx={{ ml : 5, fontSize: 20, textAlign: 'center' }}><span style={{ color: '000000' }}>상권 변화가 <span style={{ fontWeight: 'bold', color:'#236cff'}}>(활발하/침체되)</span>고 유동적이에요. 입지 선정에 유의하세요!</span></Typography>
                </Box>
                <CloseGraph />
              </Box>
            </Box>
            <Box sx={{mt : 15}}>
              <TitleType>배후지 분석</TitleType>
              <Box sx={{mt : 3}}>
                <Typography sx={{fontSize: 25 }}>주요 시설, 집객시설 현황</Typography> 
                <Box border="1px solid gray" sx={{ mt: 3, height: '70px', display: 'flex', flexDirection: 'column', justifyContent: 'center' , borderRadius : 1}}>
                    <Typography sx={{ fontSize: 20, textAlign: 'center', color: '#000000' }}>
                        선택하신 지역은 <span style={{ color: '#6474C8', fontWeight : 'bold'}}>(시설)</span> 비율이 가장 높아요. 주요 시설은 <span style={{ color: '#6474C8', fontWeight : 'bold'  }}> (1등), (2등)</span>와 <span style={{ color: '#6474C8', fontWeight : 'bold'  }}>(3등)</span>(이)가 있어요.
                    </Typography>
                </Box>
                <SectorGraph />
              </Box>
              <Box sx={{mt : 15}}>
                <Typography sx={{fontSize: 25 }}>주거인구 수</Typography> 
                <Box border="1px solid gray" sx={{ mt: 3, height: '70px', display: 'flex', flexDirection: 'column', justifyContent: 'center' , borderRadius : 1}}>
                    <Typography sx={{ fontSize: 20, textAlign: 'center', color: '#000000' }}>
                        선택하신 지역은 <span style={{color : '#6474C8', fontWeight : 'bold'}}>(인구수)명</span>이 주거중이에요.
                    </Typography>
                </Box>
                <ResidalGraph />
              </Box>
              <Box sx={{mt : 15}}>
                <Typography sx={{ fontSize: 25 }}>소비트랜드</Typography> 
                <Box border="1px solid gray" sx={{ mt: 3, height: '80px', display: 'flex', flexDirection: 'column', justifyContent: 'center' , borderRadius : 1}}>
                    <Typography sx={{ fontSize: 20, textAlign: 'center', color: '#000000' }}>
                        선택하신 지역은 <span style={{color : '#6474C8', fontWeight : 'bold'}}>(소비액 1등)</span> 소비가 가장 많은 지역이에요.
                    </Typography>
                    <Typography sx={{ fontSize: 20, textAlign: 'center', color: '#000000' }}>
                        <span style={{color : '#6474C8', fontWeight : 'bold'}}>(소비액 1등)</span> 에 대한 창업을 고려하시거나 관련하여 유리한 업종을 검토해보세요!
                    </Typography>
                </Box>
                <PieGraph />

              </Box>
              <Box sx={{display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                justifyContent: 'center',
                }}
            >
                <Button variant='contained' href = '/SimulReport' sx={{ mt: 8, width: '300px', height : '50px', bgcolor : '#012A5B', color : '#FFFFFF', borderRadius:3 }}>
                <Typography sx={{fontSize : 20}}>시뮬레이션 리포트 보러가기</Typography>
                </Button>
            </Box>
            </Box>
        </Paper>
        <Box sx={{mt : 7, ml : 5, mb : 5, mr : 7}}>
        <Typography><span style={{color : '#5F5F5F'}}>SAI 제공 정보는 각 제공 업체로부터 받는 정보로 참고용으로 이용해 주시길 바랍니다. SAI의 추정 매출은 각 매장의 실제 매출이 아니며, 일정 부분 오차가 존재합니다. 이점을 양해하여 주시기 바라며, 추정 매출의 절댓값보다는 각 매장들의 매출 추이에 더 집중해서 창업 시뮬레이션에 활용해 주시기 바랍니다. 더 양질의 서비스 제공을 위해 앞으로 더 많은 데이터를 수집하고, AI 모델을 정교화하여 정확도를 높여가겠습니다. 또한, 사용자는 그 어떤 정보도 재배포 할 수 없으며 서면 동의 없이 상업적 목적으로 사용될 수 없습니다.</span></Typography>
        </Box>
      </StyledPaper>
    </div>
  )
}

export default SimulReport2;
