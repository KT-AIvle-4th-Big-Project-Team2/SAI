import React from 'react'
import Accordion from 'react-bootstrap/Accordion';
import Box from '@mui/material/Box';
import { Divider, Typography } from '@mui/material';
import DivLine from '../../components/Styles/DivLine';

const FAQ = () => (
  <div className="container">
    <Box sx={{ height: '100%', mt: 5, mb: 5, width: 'fit-content' }}>
        <span style={{fontSize : 30, fontWeight : 'bold', color : '#012A5B'}}>FAQ</span>
    </Box>
    <Accordion>
      <Accordion.Item eventKey="0">
        <Accordion.Header><Typography sx={{ fontSize: 23 }}>🙋‍♀️ SAI는 어떤 서비스인가요?</Typography></Accordion.Header>
        <Accordion.Body>
          <Typography sx={{ fontSize: 20 }}>SAI는 Start your store with AI의 약자로, AI를 활용해 창업에 필요한 정보와 시뮬레이션을 제공하는 서비스예요.</Typography>
          <Typography sx={{ fontSize: 20 }}>다양한 지역, 업종에 대한 분석 결과를 리포트로 볼 수 있어요.</Typography>
        </Accordion.Body>
      </Accordion.Item>
      <Accordion.Item eventKey="1">
        <Accordion.Header><Typography sx={{ fontSize: 23 }}>🙋‍♂️ 매출 예측은 어떤 날짜 기준인가요?</Typography></Accordion.Header>
        <Accordion.Body>
          <Typography sx={{ fontSize: 20 }}>SAI는 분기별 매출 예측을 제공하고 있어요.</Typography>
          <Typography sx={{ fontSize: 20 }}>현재 서비스는 2023년 3분기까지의 데이터를 사용해 2023년 4분기 예측이 가능해요!</Typography>
        </Accordion.Body>
      </Accordion.Item>
      <Accordion.Item eventKey="2">
        <Accordion.Header><Typography sx={{ fontSize: 23 }}>🙋‍♀️ 서비스 제공 지역을 알고 싶어요.</Typography></Accordion.Header>
        <Accordion.Body>
          <Typography sx={{ fontSize: 20 }}>서울시 내 행정동 423개, 발달 상권 214개에 대해 서비스가 제공됩니다.</Typography>
          <Typography sx={{ fontSize: 20 }}>강동구 둔촌 1동과 구로구 항동은 준비 중이에요!</Typography>
        </Accordion.Body>
      </Accordion.Item>
      <Accordion.Item eventKey="3">
        <Accordion.Header><Typography sx={{ fontSize: 23 }}>🙋‍♂️ 서비스 제공 업종을 알고 싶어요.</Typography></Accordion.Header>
        <Accordion.Body>
          <Typography sx={{ fontSize: 20 }}>서비스 제공 업종은 총 16종이에요. 추가 업종은 준비 중이에요!</Typography>
          <br></br>
          <Typography sx={{ fontSize: 20 }}>[ 제공업종 ]</Typography>
          <Typography sx={{ fontSize: 20 }}>- 외식업(10): 한식 음식점, 커피-음료, 분식전문점, 호프-간이주점, 치킨전문점, 중식 음식점, 패스트푸드점, 제과점, 일식 음식점, 양식 음식점</Typography>
          <Typography sx={{ fontSize: 20 }}>- 소매업(4): 편의점, 일반 의류, 화장품, 의약품</Typography>
          <Typography sx={{ fontSize: 20 }}>- 서비스업(2): 일반 교습학원, 미용실</Typography>
        </Accordion.Body>
      </Accordion.Item>
      <Accordion.Item eventKey="4">
        <Accordion.Header><Typography sx={{ fontSize: 23 }}>🙋‍♀️ 데이터 업데이트 주기는 어떻게 되나요?</Typography></Accordion.Header>
        <Accordion.Body>
          <Typography sx={{ fontSize: 20 }}>데이터는 분기별 1회 업데이트돼요!</Typography>
        </Accordion.Body>
      </Accordion.Item>
      
    </Accordion>
  </div>
)

export default FAQ