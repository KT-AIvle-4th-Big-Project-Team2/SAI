import React from "react";

export const About3 = (props) => {
  return (
    <div id="about">
      <div className="container">
        <div className="row">
          <div className="col-12 col-md-6">
            <img src="img/about.jpg" className="img-fluid" alt="" />
          </div>
          <div className="col-12 col-md-6">
            <div className="about-text">
              <h2 style={{fontWeight : 'bold'}}>준비된 자본금으로 가장 높은 매출을 낼 수 있는 프랜차이즈 가맹 정보를 알려드려요.</h2>
              <p>{props.data ? props.data.paragraph : "loading..."}</p>
              <h3>제공 기능</h3>
              <div className="list-style row">
                <div className="col-lg-8 col-md-6 col-sm-12">
                  <ul>
                    {props.data
                      ? props.data.Why.map((d, i) => (
                          <li key={`${d}-${i}`}>{d}</li>
                        ))
                      : "loading"}
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};