import React from "react";
import {Box, Typography } from "@mui/material/";

// Index 상세 설명 컴포넌트 3

export const About3 = (props) => {
  return (
  
    <Box sx={{bgcolor : '#F6F6F6'}}>
    <div id="about">
      <div className="container">
        <div className="row">
          <div className="col-12 col-md-6">
            <img src="img/about3.png" className="img-fluid" alt="" />
          </div>
          <div className="col-12 col-md-6">
            <div className="about-text">
              <h2 style={{fontWeight : 'bold'}}>준비된 자본금으로  <br />가장 높은 매출을 낼 수 있는 <br /> 프랜차이즈 가맹 정보를 알려드려요.</h2>
              <div style={{marginBottom : '20px'}}>
              <Typography style={{fontSize : 20}}>창업을 고민 중인 입지와 자본금 내에서</Typography>
              <Typography style={{fontSize : 20}}>창업이 가능한 프랜차이즈 정보와 예상 창업비용을 확인해보세요.</Typography>
              </div>
              <div style={{marginBottom : '10px', marginTop : '40px'}}>
              <Typography style={{fontSize : 18, fontWeight : 'bold'}}>제공 기능</Typography>
              </div>
              <div className="list-style row">
                <div className="col-lg-8 col-md-6 col-sm-12">
                    {props.data
                      ? props.data.Why.map((d, i) => (
                          <li key={`${d}-${i}`}>{d}</li>
                        ))
                      : "loading"}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    </Box>
  );
};