import React from "react";

export const Features = (props) => {
  return (
    <div id="features" className="text-center" style={{backgroundColor: 'white', marginTop: '100px'}}>
      <div className="container">
        <div className="col-md-10 offset-md-1 section-title">
          <h2>막막한 창업 준비, SAI가 도와드릴께요</h2>
        </div>
        <div className="row" style={{marginTop: '100px', marginBottom: '100px'}}>
          {props.data
            ? props.data.map((d, i) => (
                <div key={`${d.title}-${i}`} className="col-6 col-md-3">
                  <i className={d.icon}></i>
                  <h2 style={{marginTop : '5px'}}>{d.title}</h2>
                  <p>{d.text}</p>
                </div>
              ))
            : "Loading..."}
        </div>
      </div>
    </div>
  );
};