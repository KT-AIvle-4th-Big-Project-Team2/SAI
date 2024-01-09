import React from "react";
import {Box, Typography } from "@mui/material/";

export const About2 = (props) => {
  return (
    <div id="about">
      <div className="container">
        <div className="row">
        <div className="col-12 col-md-6">
            <div className="about-text">
              <h2 style={{fontWeight : 'bold'}}>AI를 통해 <br />창업 후 매장 매출을 미리 예측해드려요.</h2>
              <div style={{marginBottom : '20px'}}>
              <Typography style={{fontSize : 20}}>창업을 고민 중인 매장의 매출을 미리 알아보고,</Typography>
              <Typography style={{fontSize : 20}}>매출 영향 요인을 분석해 매장 운영을 미리 예상해보세요.</Typography>
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
          
          <div className="col-12 col-md-6">
            <img src="img/about2.png" className="img-fluid" alt="" />
          </div>
        </div>
      </div>
    </div>
  );
};