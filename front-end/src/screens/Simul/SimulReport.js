import React, { useState, useEffect } from 'react';
import {
  Box,
  Paper,
  Typography,
  Grid,
  Button,
}
from '@mui/material/'
import '../../Pretendard-1.3.9/web/static/pretendard.css';
import DivLine from '../../components/Styles/DivLine';
import { ResponsiveCirclePacking } from '@nivo/circle-packing'
import { ResponsiveBullet } from '@nivo/bullet'
import { ResponsiveBar } from '@nivo/bar'
import { ResponsiveLine } from '@nivo/line';
import { styled } from '@mui/system';
import LoadingPage from '../../components/LoadingPage';
import axios from 'axios';
import { getGlobalData } from '../globals';

const createGradientStyle = (theme) => ({
  background: `linear-gradient(180deg, ${theme.palette.primary.dark} 0%, ${theme.palette.grey[100]} 30%,  ${theme.palette.grey[100]} 30%, ${theme.palette.grey[100]} 100%)`,
});


const StyledPaper = styled(Paper)(({ theme }) => createGradientStyle(theme));


const SimulReport = () => {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  const [useda, setDa] = useState(null); // da 객체의 상태를 관리하기 위한 useState
  const [loading, setLoading] = useState(true);
  

  useEffect(() => {

    //URL생성
    const baseApiUrl = 'http://subdomain.storeaivle.com/analysis/marketai/';
    const location = getGlobalData('selectedGu');
    const category = getGlobalData('selectedmarket');
    const capital = getGlobalData('funds');
    const station = getGlobalData('selectedDong');

    const apiUrl = `${baseApiUrl}${location}/${category}/${capital}/${station}`;

    // API 호출 주소는 환경에 맞게 설정해주세요.
    //const apiUrl = 'http://subdomain.storeaivle.com/analysis/marketai/강남구/한식음식점/100000/삼성역';
    
    // URL 인코딩이 필요할 수 있습니다. 실제 요청에 맞게 조정해주세요.
    const encodedUrl = encodeURI(apiUrl);
    setLoading(true);

    console.log(location);
    axios.get(apiUrl)
      .then(response => {
        console.log(location);
        console.log("되냐?");
        setData(response.data); // 응답 데이터를 state에 저장합니다.
        setDa({
          "AI": response.data.AI,
          "region": response.data.region,
          "area_1": response.data.area_1,
          "area_2": response.data.area_2,
          "business": response.data.business,
          "funds": response.data.funds,
          "sales_23_2q": response.data.sales_23_2q,
          "esti_23_3q": response.data.esti_23_3q,
          "pred_23_4q": response.data.pred_23_4q,
          "top_influ": response.data.top_influ,
          "bottom_influ": response.data.bottom_influ,
          "sim_result": response.data.sim_result,
          "avg_sale_comp": response.data.avg_sale_comp,
          "sale_updown": response.data.sale_updown,
          "market_active": response.data.market_active,
          "opening_updown": response.data.opening_updown,
          "area_growth": response.data.area_growth,
          "fpeople_updown": response.data.fpeople_updown,
          "simil_area_name_1": response.data.simil_area_name_1,
          "simil_area_esti_1": response.data.simil_area_esti_1,
          "simil_area_diff_1": response.data.simil_area_diff_1,
          "simil_area_name_2": response.data.simil_area_name_2,
          "simil_area_esti_2": response.data.simil_area_esti_2,
          "simil_area_diff_2": response.data.simil_area_diff_2,
          "rent_fee": response.data.rent_fee,
          "posi_fran_num": response.data.posi_fran_num,
          "franchise_rec_1": response.data.franchise_rec_1,
          "franchise_rec_2": response.data.franchise_rec_2
        });
        setLoading(false);
        console.log("테스트",response.data.region);
      })
      .catch(error => {
        console.log("안되냐?");
        setError(error); // 오류가 발생하면 state에 저장합니다.
      });
  }, []);

/*
  useEffect(() => {
    // 3초 후에 로딩 상태 변경
    const timeoutId = setTimeout(() => {
      setLoading(false);
    }, 30000);

    // 컴포넌트가 언마운트될 때 타이머 클리어
    return () => clearTimeout(timeoutId);
  }, []); // 빈 배열을 전달하여 componentDidMount와 같이 동작하게 함
*/
  const da = 
  {
    "AI": "상권",
    "region": "data.dongname",
    "area_1": "삼성역",
    "area_2": "대치2동",
    "business": "한식음식점",
    "funds": 100000,
    "sales_23_2q": 12535,
    "esti_23_3q": 14312,
    "pred_23_4q": 14675,
    "top_influ": {
    "전년도_점포별_평균_매출_금액": 56885564,
    "아파트_평균_시가": 3699240,
    "주중_평균_유동인구": 2314867,
    "폐업_점포_수": 1830457,
    "비_아파트_가구_수": 1693257
    },
    "bottom_influ": {
    "연령대_20_유동인구_수": -7984035,
    "연령대_30_유동인구_수": -3222768,
    "연령대_20_상주인구_수": -2905194,
    "시간대_00_06_유동인구_수": -1545656,
    "시간대_14_17_유동인구_수": -1379407
    },
    "sim_result": "양호",
    "avg_sale_comp": 112,
    "sale_updown": "증가",
    "market_active": "활성화",
    "opening_updown": "감소",
    "area_growth": "쇠퇴",
    "fpeople_updown": "증가",
    "simil_area_name_1": "남영동 먹자골목",
    "simil_area_esti_1": 14200,
    "simil_area_diff_1": 112,
    "simil_area_name_2": "사당역 11번(사당역먹자골목)",
    "simil_area_esti_2": 13830,
    "simil_area_diff_2": 512,
    "rent_fee": 285,
    "posi_fran_num": 597,
    "franchise_rec_1": {
    "브랜드명": "소플러스",
    "평균매출금액": 177100,
    "가맹금액": 1320,
    "교육금액": 3630,
    "보증금액": 2000,
    "기타금액": 57500,
    "합계금액": 64450
    },
    "franchise_rec_2": {
    "브랜드명": "고창면옥",
    "평균매출금액": 144201,
    "가맹금액": 550,
    "교육금액": 330,
    "보증금액": 2000,
    "기타금액": 51965,
    "합계금액": 58000
    },
    "user": 12
    }

/*
  const circle1 = {
    "name": "",
    "children" : [
    {
      "name": Object.keys(useda.top_influ)[0],
      "loc": useda.top_influ[Object.keys(useda.top_influ)[0]]
    },
    {
      "name": Object.keys(useda.top_influ)[1],
      "loc": useda.top_influ[Object.keys(useda.top_influ)[1]]
    },
    {
      "name": Object.keys(useda.top_influ)[2],
      "loc": useda.top_influ[Object.keys(useda.top_influ)[2]]
    },
    {
      "name": Object.keys(useda.top_influ)[3],
      "loc": useda.top_influ[Object.keys(useda.top_influ)[3]]
    },
    {
      "name": Object.keys(useda.top_influ)[4],
      "loc": useda.top_influ[Object.keys(useda.top_influ)[4]]
    }
  ]
  }
  */
  /*
  const CircleGraph1 = () => (
    
    <div style={{ height: '500px'}}>
    <ResponsiveCirclePacking
      data={circle1}
      margin={{ top: 20, right: 20, bottom: 20, left: 20 }}
      id="name"
      value="loc"
      enableLabels={true}
      colors={({ depth }) => (depth === 0 ? 'white' : 'hsl(200, 70%, ' + (70 - 20 * depth) + '%)')}
      borderColor={({ depth }) => (depth === 0 ? 'white' : 'hsl(200, 70%, 50%)')}
    />
  </div>
);
*/
const CircleGraph1 = () => {
  // useda가 유효한지 확인
  if (!useda || !useda.top_influ) {
    // useda가 로드되지 않았다면 로딩 메시지 또는 대체 UI 표시
    return <div>Loading...</div>;
  }

  // useda가 유효하면, 여기서 circle1 데이터를 구성
  const circle1 = {
    "name": "",
    "children" : [
    {
      "name": Object.keys(useda.top_influ)[0],
      "loc": useda.top_influ[Object.keys(useda.top_influ)[0]]
    },
    {
      "name": Object.keys(useda.top_influ)[1],
      "loc": useda.top_influ[Object.keys(useda.top_influ)[1]]
    },
    {
      "name": Object.keys(useda.top_influ)[2],
      "loc": useda.top_influ[Object.keys(useda.top_influ)[2]]
    },
    {
      "name": Object.keys(useda.top_influ)[3],
      "loc": useda.top_influ[Object.keys(useda.top_influ)[3]]
    },
    {
      "name": Object.keys(useda.top_influ)[4],
      "loc": useda.top_influ[Object.keys(useda.top_influ)[4]]
    }
  ]
  }

  return (
    <div style={{ height: '500px'}}>
      <ResponsiveCirclePacking
        data={circle1}
        margin={{ top: 20, right: 20, bottom: 20, left: 20 }}
        id="name"
        value="loc"
        enableLabels={true}
        colors={({ depth }) => (depth === 0 ? 'white' : 'hsl(200, 70%, ' + (70 - 20 * depth) + '%)')}
        borderColor={({ depth }) => (depth === 0 ? 'white' : 'hsl(200, 70%, 50%)')}
      />
    </div>
  );
};

/*
const circle2 = {
  "name": "",
  "children" : [
  {
    "name": Object.keys(useda.bottom_influ)[0],
    "loc": Math.abs(useda.bottom_influ[Object.keys(useda.bottom_influ)[0]])
  },
  {
    "name": Object.keys(useda.bottom_influ)[1],
    "loc": Math.abs(useda.bottom_influ[Object.keys(useda.bottom_influ)[1]])
  },
  {
    "name": Object.keys(useda.bottom_influ)[2],
    "loc": Math.abs(useda.bottom_influ[Object.keys(useda.bottom_influ)[2]])
  },
  {
    "name": Object.keys(useda.bottom_influ)[3],
    "loc": Math.abs(useda.bottom_influ[Object.keys(useda.bottom_influ)[3]])
  },
  {
    "name": Object.keys(useda.bottom_influ)[4],
    "loc": Math.abs(useda.bottom_influ[Object.keys(useda.bottom_influ)[4]])
  }
]
}

const CircleGraph2 = () => (
  <div style={{ height: '500px'}}>
    <ResponsiveCirclePacking
      data={circle2}
      margin={{ top: 20, right: 20, bottom: 20, left: 20 }}
      id="name"
      value="loc"
      enableLabels={true}
      colors={({ depth }) => (depth === 0 ? 'white' : 'hsl(0, 70%, 60%)')}
      borderColor={({ depth }) => (depth === 0 ? 'white' : 'hsl(200, 70%, 50%)')}
    />
  </div>
);
*/

const CircleGraph2 = () => {
  // useda가 유효한지 확인
  if (!useda || !useda.bottom_influ) {
    // useda가 로드되지 않았다면 로딩 메시지 또는 대체 UI 표시
    return <div>Loading...</div>;
  }

  // useda가 유효하면, 여기서 circle2 데이터를 구성
  const circle2 = {
    "name": "",
    "children": Object.keys(useda.bottom_influ).map(key => ({
      "name": key,
      "loc": Math.abs(useda.bottom_influ[key])
    }))
  };

  return (
    <div style={{ height: '500px'}}>
      <ResponsiveCirclePacking
        data={circle2}
        margin={{ top: 20, right: 20, bottom: 20, left: 20 }}
        id="name"
        value="loc"
        enableLabels={true}
        colors={({ depth }) => (depth === 0 ? 'white' : 'hsl(0, 70%, 60%)')}
        borderColor={({ depth }) => (depth === 0 ? 'white' : 'hsl(200, 70%, 50%)')}
      />
    </div>
  );
};


  const data2 = [
    {
      "id": '',
      "ranges": [0, 25, 50, 75, 100],
      "measures": [66],
      "markers": [null], // markers는 필요에 따라 추가
    },
  ];

  /*
  const data3 = [
    { id: useda.simil_area_name_1, value: useda.simil_area_esti_1, color: '#236cff' },
    { id: useda.simil_area_name_2, value: useda.simil_area_esti_2, color: '#FF6B00' },
    { id: useda.area_1, value: useda.esti_23_3q, color: '#9B9B9B' },
  ];
  */
  const data3 = [
    { id: useda?.new_simil_area_name_1 || 'Default Name 1', value: useda?.new_simil_area_esti_1 || 0, color: '#236cff' },
    { id: useda?.new_simil_area_name_2 || 'Default Name 2', value: useda?.new_simil_area_esti_2 || 0, color: '#FF6B00' },
    { id: useda?.new_area_1 || 'Default Area 1', value: useda?.new_esti_23_3q || 0, color: '#9B9B9B' },
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
        { x: '2023년 2분기', y: useda?.sales_23_2q || 0 },
        { x: '2023년 3분기', y: useda?.esti_23_3q || 0 },
        { x: '2023년 4분기', y: useda?.pred_23_4q || 0 },
      ],
    },
  ];
  
  
  const BumpGraph = () => (
    <div style={{ height: '450px', padding : 10, mt : 15}}>
    <Box sx={{display : 'flex', justifyContent : 'space-between', mt : 2, ml : 3, mr : 7}}>
        <Typography sx={{fontSize : 20, fontWeight : 'bold'}}>매출액 추이</Typography>
        <Typography sx={{fontSize : 15, fontWeight : 'bold'}}>단위 : 만원 / 점포당 평균 월 매출</Typography>
    </Box>
    <ResponsiveLine
      data={data4}
      margin={{ top: 30, right: 60, bottom: 110, left: 60 }}
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



  const user = 'jinwon97'

  const TitleType = ({children}) => {
    const fontSize = 30;
    const mt = 2;
  
    return (
      <Typography style={{ fontSize, marginTop: mt, fontWeight : 'bold' }}>
        {children}
      </Typography>
    );
  };

  const ContentsType = ({children}) => {
    const fontSize = 20;
    const mt = 2;
  
    return (
      <Typography style={{ fontSize, marginTop: mt }}>
        {children}
      </Typography>
    );
  };
  


  return (
    
    <>
    {loading ? (
      // 로딩 중일 때 표시할 내용
      < LoadingPage />
    ) : (
      
    <div className="container">  
    
    <Button variant='contained' href= '/SimulReport2' sx={{mt : 4, color: '#ffffff', paddingY: 1, borderRadius: 0, width : '150px', bgcolor:"#C5C1C1"}}><span style={{fontSize : 18}}>분석 보고서</span></Button>
    <Button variant='contained' sx={{mt : 4, color : '#FFFFFF', bgcolor : '#012A5B',  paddingY: 1, borderRadius: 0}}><span style={{fontSize : 18}}>시뮬레이션 리포트</span></Button>
      <StyledPaper sx={{ height : 'auto', padding : 5, minWidth : '1200px'}}>
          <Box sx={{ml: 4, mb: 3, width: 'fit-content', height: 'auto' }}> 
            <Typography style={{ fontSize : 40, fontWeight : 'bold' }}><span style={{ color : '#FFFFFF' }}> SAI 창업 시뮬레이션 리포트</span></Typography>
          </Box>
          <Paper border="1px solid black" borderRadius={8} sx={{ height: 'auto', mb: 3, ml : 4, mr : 4, padding : 8, borderRadius : 8}}>
            <TitleType> 선택 값을 반영해 SAI로 분석한</TitleType>
            <TitleType> {user} 님 매장의 추정 / 예상 매출이에요.</TitleType>
            <DivLine />
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: 10, marginBottom : 20 }}>
            <Typography fontSize={24} sx={{ml : 20, mt : 5, fontWeight : 'bold'} }>지역 <span style={{ color : '#6474C8', fontWeight : 'bold'}}>{useda.region} {useda.area_2} {useda.area_1}</span></Typography>
            <Typography fontSize={24} sx={{mt : 5, fontWeight : 'bold'}}>업종 <span style={{ color : '#6474C8', fontWeight : 'bold' }}>{useda.business}</span></Typography>
            <Typography fontSize={24} sx={{mt : 5, mr : 20, fontWeight : 'bold'}}>창업준비금 <span style={{ color : '#6474C8', fontWeight : 'bold'}}>{useda.funds.toLocaleString()}만원</span></Typography>
            </div>
            <BumpGraph />

            <Box>
              <Typography fontSize={30} sx={{ml : 1, mt : 10, mr : 10, fontWeight : 'bold'}}>창업 전망 : <span style={{ color : '#236cff', fontWeight : 'bold' }}>{useda.sim_result}</span> </Typography>
              <Box bgcolor={'primary.gray'} sx={{ display: 'flex', justifyContent: 'center', height: '12vh', marginTop:5,  }}>
              <ResponsiveBullet
                data={data2}
                margin={{left : 10, right : 10, top: 30, bottom: 30}}
                title="Bullet Chart Example"
                rangeColors={['#ffd9d3']} // 옅은 분홍색
                measureColors={['#236cff']} // 파란색
                measureBorderWidth={5}
                rangeBorderWidth={5}
              />
              </Box>
              <Box sx={{ mt : 2, mb : 14, bgcolor : '#F5F5F5', padding : 3, borderRadius : 3}}>
              <ContentsType><span style={{ color : '#6474C8', fontWeight : 'bold' }}>{useda.region} {useda.area_2}</span>에서 <span style={{ color : '#6474C8', fontWeight : 'bold' }}>{useda.business}</span> 업종 창업은 <span style={{ fontWeight: 'bold' }}>서울시 내 동종 업종의 평균 추정 매출 대비</span> {useda.avg_sale_comp}%입니다.</ContentsType>
              <ContentsType><span style={{ color : '#6474C8', fontWeight : 'bold' }}>{useda.region} {useda.area_2}</span>에서 <span style={{ color : '#6474C8', fontWeight : 'bold' }}>{useda.business}</span> 업종 창업은 자치구에 비해 <span style={{ fontWeight: 'bold' }}>매출</span>이 <span style={{ fontWeight: 'bold', color:'#236cff'}}>{useda.sale_updown}</span> 추세예요. 인근 지역에 비해 <span style={{ fontWeight: 'bold', color:'#236cff'}}>{useda.market_active}</span> 된 상권이에요. 경쟁 관계에 유의하세요.</ContentsType>
              <ContentsType><span style={{ color : '#6474C8', fontWeight : 'bold' }}>{useda.region} {useda.area_2}</span>에서 <span style={{ color : '#6474C8', fontWeight : 'bold' }}>{useda.business}</span> 업종의 <span style={{ fontWeight: 'bold' }}>점포수</span>가 전년 동기에 비해 <span style={{ fontWeight: 'bold', color:'#236cff'}}>{useda.opening_updown}</span>하고 있어요. 상권이 <span style={{ fontWeight: 'bold', color:'#236cff'}}>{useda.area_growth}</span>하는 시기인 경우 입지 선정에 신중하셔야 해요.</ContentsType>
              <ContentsType><span style={{ color : '#6474C8', fontWeight : 'bold' }}>{useda.region} {useda.area_2}</span>은 전년 동분기에 비해 <span style={{ fontWeight: 'bold' }}>유동인구</span>가 <span style={{ fontWeight: 'bold', color:'#236cff'}}>{useda.fpeople_updown}</span>하고 있는 지역이에요. 마케팅이 중요한 상권이에요.</ContentsType>
              </Box>
            </Box>
            <Grid container spacing={2}>
             <Grid item xs={6}>
              <TitleType>비슷한 지역 추천</TitleType>
              <br></br>
              <Typography style={{ fontSize: '22px'}}><span style={{ color : '#6474C8', fontWeight : 'bold'}}>{useda.region} {useda.area_2} {useda.business}</span> 업종과 비슷한 추정 매출을 보이는 곳은 <span style={{ color : '#FF6B00', fontWeight : 'bold'  }}>{useda.simil_area_name_1}, {useda.simil_area_name_2}</span>이 있어요.</Typography>
              <br></br>
              <ContentsType><span style={{ fontWeight : 'bold', fontSize: '24px'}}>{useda.simil_area_name_1}</span></ContentsType>
              <ContentsType><span style={{ color : '#9B9B9B'}}>2023년도 3,4분기 평균 추정 매출</span></ContentsType>
              <ContentsType><span style={{ color : '#FF6B00', fontWeight : 'bold'}}>{useda.simil_area_esti_1.toLocaleString()}만원</span> <span style={{fontSize:'15px', fontWeight : 'bold', backgroundColor:'#FFCCA7'}}>차이 : {useda.simil_area_diff_1.toLocaleString()}만원</span></ContentsType>
              <br></br>
              <br></br>
              <ContentsType><span style={{ fontWeight : 'bold', fontSize: '24px'}}>{useda.simil_area_name_2}</span></ContentsType>
              <ContentsType><span style={{ color : '#9B9B9B'}}>2023년도 3,4분기 평균 추정 매출</span></ContentsType>
              <ContentsType><span style={{ color : '#FF6B00', fontWeight : 'bold'}}>{useda.simil_area_esti_2.toLocaleString()}만원</span> <span style={{fontSize:'15px', fontWeight : 'bold', backgroundColor:'#FFCCA7'}}>차이 : {useda.simil_area_diff_2.toLocaleString()}만원</span></ContentsType>
              </Grid>
              <Grid item xs={6}>
                <BarGraph />
              </Grid>
            </Grid>
            <Box sx={{mt : 14}}>
              <TitleType>매출 영향 요인 분석</TitleType>
              <br></br>
              <Typography style={{ fontSize: '23px'}}>SAI로 분석한 {user}님의 매장의 추정 매출의 영향 요인이에요.</Typography>
              <br></br>
            </Box>
            <Grid container spacing={2}>
             <Grid item xs={6}>
              <CircleGraph1 />
             </Grid>
             <Grid item xs={6}>
              <CircleGraph2 />
             </Grid>
             </Grid>
            <Box>
              <br></br>
              <ContentsType>분석된 <span style={{ color : '#0500FF', fontWeight : 'bold'}}>파란색 요인</span>은 매출을 증가시키는데 기여할 수 있어요.</ContentsType>
              <ContentsType>분석된 <span style={{ color : '#FF0000', fontWeight : 'bold'}}>빨간색 요인</span>은 매출을 증가시키는데 기여할 수 있어요.</ContentsType>
              <ContentsType>창업시 매장의 높은 매출을 위해서는 해당 요인들을 관리하는 것을 고려하시는 것이 좋아요.</ContentsType>
            </Box>

            <Box sx={{mt : 14, mb : 10}}>
                <Typography fontSize={30} sx={{fontWeight : 'bold'}}>프랜차이즈 창업 비용</Typography>
                <br />
                <Typography style={{ fontSize: '23px'}}>비슷한 창업 비용으로 가능한 <span style={{ color : '#647AC5', fontWeight : 'bold'}}>{useda.business}</span> 업종 프랜차이즈 목록이에요.</Typography>
              <Box sx = {{bgcolor:'primary.gray', mt : 5, mb : 5, padding : 3}}>
                <Typography fontSize={23}>💡 <span style={{ fontWeight : 'bold'}}>참고 도움말</span></Typography>
                <ContentsType><span style={{ color : '#5F5F5F' }}>추천된 목록은 입력하신 자본금으로 창업 가능한 브랜드 중 매출이 가장 높은 곳이에요.</span></ContentsType>
                <ContentsType><span style={{ color : '#5F5F5F' }}>좋은 자리라면 평균 임대료에 권리금이 추가로 더 발생할 수 있어요.</span></ContentsType>
                <ContentsType><span style={{ color : '#647AC5', fontWeight : 'bold'}}>{useda.region} {useda.area_2}</span> <span style={{ color : '#5F5F5F' }}>의 평균 임대 면적은 </span><span style={{ color : '#647AC5',fontWeight : 'bold'}}>58.7m^2</span><span style={{ color : '#5F5F5F' }}>이고, 평균 임대료는 ^2 당</span> <span style={{ color : '#647AC5',fontWeight : 'bold'}}>{useda.rent_fee}만원</span><span style={{ color : '#5F5F5F' }}>이에요.</span> </ContentsType>
              </Box>
              <Box sx={{marginTop : 5}}>
                <Typography fontSize={23} sx = {{fontWeight : 'bold', fontSize: '26px'}}>{useda.franchise_rec_1.브랜드명}</Typography>
                <Typography fontSize={23}>예상 창업 비용<span style={{color : '#9B9B9B'}}>(임대료 및 보증금 포함)</span></Typography>
                <Typography fontSize={23} sx = {{fontWeight : 'bold'}}><span style={{color : '#FF6B00'}}>{useda.franchise_rec_1.합계금액.toLocaleString()}만원</span> <span style={{fontSize:'15px', fontWeight : 'bold', backgroundColor:'#FFCCA7'}}></span></Typography>
                <br />
                <hr></hr>
                <Grid container spacing={10}>
                  <Grid item xs={6}>
                    <Box sx={{display : 'flex', justifyContent : 'space-between', marginLeft : 5, marginRight : 5}}>
                      <Typography>가입비</Typography>
                      <Typography sx={{fontWeight : 'bold'}}>{useda.franchise_rec_1.가맹금액.toLocaleString()}만원</Typography>
                    </Box>
                    </Grid>
                    <Grid item xs={6}>
                    <Box sx={{display : 'flex', justifyContent : 'space-between', marginLeft : 5, marginRight : 5}}>
                      <Typography>교육비</Typography>
                      <Typography sx={{fontWeight : 'bold'}}>{useda.franchise_rec_1.교육금액.toLocaleString()}만원</Typography>
                    </Box>
                    </Grid>
                </Grid>
                <hr></hr>
                <Grid container spacing={10}>
                  <Grid item xs={6}>
                    <Box sx={{display : 'flex', justifyContent : 'space-between', marginLeft : 5, marginRight : 5}}>
                      <Typography>보증금</Typography>
                      <Typography sx={{fontWeight : 'bold'}}>{useda.franchise_rec_1.보증금액.toLocaleString()}만원</Typography>
                    </Box>
                    </Grid>
                    <Grid item xs={6}>
                    <Box sx={{display : 'flex', justifyContent : 'space-between', marginLeft : 5, marginRight : 5}}>
                      <Typography>기타비용</Typography>
                      <Typography sx={{fontWeight : 'bold'}}>{useda.franchise_rec_1.기타금액.toLocaleString()}만원</Typography>
                    </Box>
                    </Grid>
                </Grid>
                <hr></hr>
                <Grid container spacing={10}>
                  <Grid item xs={6}>
                    <Box sx={{display : 'flex', justifyContent : 'space-between', marginLeft : 5, marginRight : 5}}>
                      <Typography>첫 월 임대료</Typography>
                      <Typography sx={{fontWeight : 'bold'}}>{useda.rent_fee}만원</Typography>
                    </Box>
                    </Grid>
                    <Grid item xs={6}>
                    <Box sx={{display : 'flex', justifyContent : 'space-between', marginLeft : 5, marginRight : 5}}>
                      <Typography>임대 보증금(월 보증금 X 10개월)</Typography>
                      <Typography sx={{fontWeight : 'bold'}}>{useda.rent_fee}0만 원</Typography>
                    </Box>
                    </Grid>
                </Grid>
              </Box>
              <Box sx={{mt : 10, mb : 5}}>
              <Typography fontSize={23} sx = {{fontWeight : 'bold', fontSize: '26px'}}>{useda.franchise_rec_2.브랜드명}</Typography>
                <Typography fontSize={23}>예상 창업 비용<span style={{color : '#9B9B9B'}}>(임대료 및 보증금 포함)</span></Typography>
                <Typography fontSize={23} sx = {{fontWeight : 'bold'}}><span style={{color : '#FF6B00'}}>{useda.franchise_rec_2.합계금액.toLocaleString()}만원</span> <span style={{fontSize:'15px', fontWeight : 'bold', backgroundColor:'#FFCCA7'}}></span></Typography>
                <br />
                <hr></hr>
                <Grid container spacing={10}>
                  <Grid item xs={6}>
                    <Box sx={{display : 'flex', justifyContent : 'space-between', marginLeft : 5, marginRight : 5}}>
                      <Typography>가입비</Typography>
                      <Typography sx={{fontWeight : 'bold'}}>{useda.franchise_rec_2.가맹금액.toLocaleString()}만원</Typography>
                    </Box>
                    </Grid>
                    <Grid item xs={6}>
                    <Box sx={{display : 'flex', justifyContent : 'space-between', marginLeft : 5, marginRight : 5}}>
                      <Typography>교육비</Typography>
                      <Typography sx={{fontWeight : 'bold'}}>{useda.franchise_rec_2.교육금액.toLocaleString()}만원</Typography>
                    </Box>
                    </Grid>
                </Grid>
                <hr></hr>
                <Grid container spacing={10}>
                  <Grid item xs={6}>
                    <Box sx={{display : 'flex', justifyContent : 'space-between', marginLeft : 5, marginRight : 5}}>
                      <Typography>보증금</Typography>
                      <Typography sx={{fontWeight : 'bold'}}>{useda.franchise_rec_2.보증금액.toLocaleString()}만원</Typography>
                    </Box>
                    </Grid>
                    <Grid item xs={6}>
                    <Box sx={{display : 'flex', justifyContent : 'space-between', marginLeft : 5, marginRight : 5}}>
                      <Typography>기타비용</Typography>
                      <Typography sx={{fontWeight : 'bold'}}>{useda.franchise_rec_2.기타금액.toLocaleString()}만원</Typography>
                    </Box>
                    </Grid>
                </Grid>
                <hr></hr>
                <Grid container spacing={10}>
                  <Grid item xs={6}>
                    <Box sx={{display : 'flex', justifyContent : 'space-between', marginLeft : 5, marginRight : 5}}>
                      <Typography>첫 월 임대료</Typography>
                      <Typography sx={{fontWeight : 'bold'}}>{useda.rent_fee}만원</Typography>
                    </Box>
                    </Grid>
                    <Grid item xs={6}>
                    <Box sx={{display : 'flex', justifyContent : 'space-between', marginLeft : 5, marginRight : 5}}>
                      <Typography>임대 보증금(월 보증금 X 10개월)</Typography>
                      <Typography sx={{fontWeight : 'bold'}}>{useda.rent_fee}0만 원</Typography>
                    </Box>
                    </Grid>
                </Grid>

              </Box>

            </Box>
            <Box sx={{display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                justifyContent: 'center',
                }}
            >
                <Button variant='contained' href = '/SimulReport2' sx={{ mt: 8, width: '300px', height : '50px', bgcolor : '#012A5B', color : '#FFFFFF', borderRadius:3 }}>
                <Typography sx={{fontSize : 20}}>분석 보고서 보러가기</Typography>
                </Button>
            </Box>
        </Paper>
        <Box sx={{mt : 7, ml : 5, mb : 5, mr : 7}}>
            <Typography><span style={{color : '#5F5F5F'}}>SAI 제공 정보는 각 제공 업체로부터 받는 정보로 참고용으로 이용해 주시길 바랍니다. SAI의 추정 매출은 각 매장의 실제 매출이 아니며, 일정 부분 오차가 존재합니다. 이점을 양해하여 주시기 바라며, 추정 매출의 절댓값보다는 각 매장들의 매출 추이에 더 집중해서 창업 시뮬레이션에 활용해 주시기 바랍니다. 더 양질의 서비스 제공을 위해 앞으로 더 많은 데이터를 수집하고, AI 모델을 정교화하여 정확도를 높여가겠습니다. 또한, 사용자는 그 어떤 정보도 재배포 할 수 없으며 서면 동의 없이 상업적 목적으로 사용될 수 없습니다.</span></Typography>
        </Box>
      </StyledPaper>
    </div>
    )}
    </>
  );
};

export default SimulReport;
