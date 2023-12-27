import React from 'react'
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
import imgLogo from './logo.png';

function NavBarElements() {
  return (
    <>
      <Navbar bg="dark" data-bs-theme="dark" style={{display: 'flex', justifyContent : 'space-between'}}>
        <Container>
          <Navbar.Brand href="/Home">
              <img
                src={imgLogo}
                width="30"
                height="30"
                className="d-inline-block align-top"
                alt="React Bootstrap logo"
              />
            </Navbar.Brand>
            
          <Nav className="me-auto" style={{marginLeft : '50%', minWidth : '600px'}}>
            <NavDropdown title="알림마당" id="basic-nav-dropdown">
                <NavDropdown.Item href="/Notice">공지사항</NavDropdown.Item>
                <NavDropdown.Item href="/FAQ">FAQ</NavDropdown.Item>
                <NavDropdown.Divider />
                <NavDropdown.Item href="#action/3.3">개선의견</NavDropdown.Item>
            </NavDropdown>
            <NavDropdown title="시뮬레이션" id="basic-nav-dropdown">
                <NavDropdown.Item href="/Simul">시뮬레이션</NavDropdown.Item>
                <NavDropdown.Item href="/SimulReport">시뮬레이션 리포트</NavDropdown.Item>
            </NavDropdown>
            <NavDropdown title="창업분석" id="basic-nav-dropdown">
                <NavDropdown.Item href="/Area">지역 분석</NavDropdown.Item>
                <NavDropdown.Item href="/Sectors">업종 분석</NavDropdown.Item>
            </NavDropdown>
            <NavDropdown title="게시판" id="basic-nav-dropdown">
                <NavDropdown.Item href="/Board">창업 정보</NavDropdown.Item>
                <NavDropdown.Item href="/Board">창업 게시판</NavDropdown.Item>
            </NavDropdown>
            <NavDropdown title="마이페이지" id="basic-nav-dropdown">
                <NavDropdown.Item href="/MyinfoCheck">내 정보 수정</NavDropdown.Item>
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