import React from 'react'
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
import imgLogo from './logo.png';
import "./NavBarElements.css";

function NavBarElements() {
  return (
    <>
      <Navbar bg="dark" data-bs-theme="dark">
        <Container>
          <Navbar.Brand href="/">
              <img
                src={imgLogo}
                width="30"
                height="30"
                className="d-inline-block align-top"
                alt="React Bootstrap logo"
              />
            </Navbar.Brand>
          <Nav className="me-auto">
            <NavDropdown title="알림마당" id="basic-nav-dropdown">
                <NavDropdown.Item href="/Notice">공지사항</NavDropdown.Item>
                <NavDropdown.Item href="/FAQ">FAQ</NavDropdown.Item>
                <NavDropdown.Divider />
                <NavDropdown.Item href="#action/3.3">개선의견</NavDropdown.Item>
            </NavDropdown>
            <NavDropdown title="시뮬레이션" id="basic-nav-dropdown">
                <NavDropdown.Item href="#action/3.1">시뮬레이션</NavDropdown.Item>
                <NavDropdown.Item href="#action/3.2">시뮬레이션 리포트</NavDropdown.Item>
            </NavDropdown>
            <NavDropdown title="창업분석" id="basic-nav-dropdown">
                <NavDropdown.Item href="#action/3.1">지역 분석</NavDropdown.Item>
                <NavDropdown.Item href="#action/3.2">업종 분석</NavDropdown.Item>
            </NavDropdown>
            <NavDropdown title="게시판" id="basic-nav-dropdown">
                <NavDropdown.Item href="/Board">창업 정보</NavDropdown.Item>
                <NavDropdown.Item href="/Board">창업 게시판</NavDropdown.Item>
            </NavDropdown>
            <NavDropdown title="마이페이지" id="basic-nav-dropdown">
                <NavDropdown.Item href="/Myinfo">내 정보 수정</NavDropdown.Item>
                <NavDropdown.Item href="/Myboard">내가 쓴 글</NavDropdown.Item>
            </NavDropdown>
            <Nav.Link href="/login">Log out</Nav.Link>
            
          </Nav>
        </Container>
      </Navbar>
    </>
  );
}

export default NavBarElements;

function NavBarElements2() {
  return (
    <>
      <Navbar bg="dark" data-bs-theme="dark">
        <Container>
          <Navbar.Brand href="#home">
              <img
                src={imgLogo}
                width="30"
                height="30"
                className="d-inline-block align-top"
                alt="React Bootstrap logo"
              />
            </Navbar.Brand>
          <Nav className="me-auto">
            <Nav.Link href="#home">Index</Nav.Link>
            <Nav.Link href="#home">Home</Nav.Link>
            <Nav.Link href="#home">Login</Nav.Link>
            
          </Nav>
        </Container>
      </Navbar>
    </>
  );
}