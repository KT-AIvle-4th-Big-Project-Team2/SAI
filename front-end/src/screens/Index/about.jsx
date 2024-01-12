import React from "react";
import {Box, Typography } from "@mui/material/";

// Index 특성 상세 설명 컴포넌트 1


export const About = (props) => {
  return (
  
    <Box sx={{bgcolor : '#F6F6F6'}}>
    <div id="about">
      <div className="container">
        <div className="row">
          <div className="col-12 col-md-6">
            <img src="img/about1.png" className="img-fluid" alt="" />
          </div>
          <div className="col-12 col-md-6">
            <div className="about-text">
              <h2 style={{fontWeight : 'bold'}}>창업을 고민하고 있는 입지와 <br />업종 분석 결과를 리포트로 제공해드려요.</h2>
              <div style={{marginBottom : '20px'}}>
              <Typography style={{fontSize : 20}}>창업을 위해 꼭 알아야 할 내용만 제공하는 분석리포트를 통해 </Typography>
              <Typography style={{fontSize : 20}}>더 빠른 위치 선정이 가능해요.</Typography>
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