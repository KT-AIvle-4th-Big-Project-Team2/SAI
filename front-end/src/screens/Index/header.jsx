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
                  <br></br>
                  {props.data ? props.data.title2 : "Loading"}
                  <span></span>
                </h1>
                <p className="lead">
                  {props.data ? props.data.paragraph : "Loading"}
                </p>
                <a
                  href="/login"
                  className="btn btn-lg page-scroll"
                  style={{
                    fontSize : '25px',
                    width: '300px', // 원하는 가로 크기로 조절
                    backgroundColor: 'white', // 배경색을 흰색으로 변경
                    color: '#012A5B', // 글자색을 파란색으로 변경
                    fontWeight: 'bold',
                  }}
                >
                  지금 바로 이용하기
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </header>
  );
};