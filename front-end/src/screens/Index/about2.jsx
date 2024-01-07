import React from "react";

export const About2 = (props) => {
  return (
    <div id="about">
      <div className="container">
        <div className="row">
          <div className="col-12 col-md-6">
            <div className="about-text">
              <h2 style={{fontWeight : 'bold'}}>AI를 통해 창업 후 매장 매출을 미리 예측해드려요.</h2>
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
          
          <div className="col-12 col-md-6">
            <img src="img/about2.png" className="img-fluid" alt="" />
          </div>
        </div>
      </div>
    </div>
  );
};