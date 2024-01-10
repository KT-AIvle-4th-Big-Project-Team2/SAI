import React from "react";

export const Testimonials = (props) => {
  return (
    <div id="testimonials">
      <div className="container">
        <div className="section-title text-center">
          <h2 style={{fontWeight : 'bold', fontSize : 43}}>예비 사장님, 그동안 궁금하셨죠?</h2>
        </div>
        <div className="row">
          {props.data
            ? props.data.map((d, i) => (
                <div key={`${d.name}-${i}`} className="col-12 col-md-6 col-lg-6 mb-4">
                  <div className="testimonial">
                    <div className="testimonial-image">
                      {d.img ? (
                          <img src={d.img} alt="" />
                        ) : ""}
                    </div>
                    <div style={{marginTop : '20px'}}>
                      <h4 style={{fontSize : 25}}>{d.text}</h4>
                      <div className="testimonial-meta">{d.name}</div>
                    </div>
                  </div>
                </div>
              ))
            : "loading"}
        </div>
      </div>
    </div>
  );
};