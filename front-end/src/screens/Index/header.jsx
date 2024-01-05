import React from "react";

export const Header = (props) => {

  return (
    <header id="header">
      <div className="intro">
        <div className="overlay">
          <div className="container">
            <div className="row">
              <div className="col-md-8 offset-md-2 intro-text">
                <h1 className="display-4">
                  {props.data ? props.data.title : "Loading"}
                  <span></span>
                </h1>
                <p className="lead">
                  {props.data ? props.data.paragraph : "Loading"}
                </p>
                <a
                  href="#features"
                  className="btn btn-primary btn-lg page-scroll"
                >
                  Learn More
                </a>{" "}
              </div>
            </div>
          </div>
        </div>
      </div>
    </header>
  );
};