import React, { useState } from 'react';
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
import imgLogo from './logo.png';
import { Button, Dialog, DialogTitle, DialogContent, DialogActions, TextField} from '@mui/material';
import axios from 'axios';
import { useAuth } from '../Auth/AuthContext';

// 상단 네비게이션 바 컴포넌트

function NavBarElements() {
  const [openFeedback, setOpenFeedback] = useState(false);
  const [feedbackTitle, setFeedbackTitle] = useState('');
  const [feedbackContent, setFeedbackContent] = useState('');
  const name = 'test'
  const { isLogin, logoutHandler } = useAuth();

  const handleOpenFeedback = () => {
    setOpenFeedback(true);
  };

  const handleCloseFeedback = () => {
    setOpenFeedback(false);
  };

  const handleSendFeedback = () => {
    const title = feedbackTitle
    const contents = feedbackContent
    axios.post("http://127.0.0.1:8000/suggestions/suggestions/createpost", {
      title,
      contents,
      name
    })
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
    setOpenFeedback(false);
    setFeedbackTitle('');
    setFeedbackContent('');
    })}

  return (
      <>
        <Navbar style={{ background: '#EAEAEA' }} data-bs-theme="light">
          <Container className="justify-content-between">
            <Navbar.Brand href="/Home">
              <img
                src={imgLogo}
                width="23"
                height="30"
                className="d-inline-block align-top"
                alt="React Bootstrap logo"
              />
            </Navbar.Brand>
          {isLogin ? (
            <Nav>
              <Nav.Link href="/Home">창업도우미</Nav.Link>
              <NavDropdown title="커뮤니티" id="basic-nav-dropdown">
                <NavDropdown.Item href="/FAQ">FAQ</NavDropdown.Item>
                <NavDropdown.Item href="/Notice">공지사항</NavDropdown.Item>
                <NavDropdown.Item href="/Board1">창업 정보</NavDropdown.Item>
                <NavDropdown.Item href="/Board2">창업 게시판</NavDropdown.Item>
              </NavDropdown>
              <NavDropdown title="마이페이지" id="basic-nav-dropdown">
                <NavDropdown.Item href="/MyinfoCheck">내 정보 수정</NavDropdown.Item>
                <NavDropdown.Item onClick={handleOpenFeedback}>개선의견</NavDropdown.Item>
              </NavDropdown>
              <Nav.Link href="/" onClick={logoutHandler}>Logout</Nav.Link>
            </Nav>
          ) : ( 
          <Nav>
          <Nav.Link href="/login">로그인</Nav.Link>
          <Nav.Link href="/Signup">회원가입</Nav.Link>
          </Nav>
          )}
          </Container>
        </Navbar>
        

        <Dialog open={openFeedback} onClose={handleCloseFeedback}>
          <DialogTitle>개선의견 제출</DialogTitle>
          <DialogContent>
            <TextField
              label="제목"
              variant="outlined"
              fullWidth
              margin="normal"
              value={feedbackTitle}
              onChange={(e) => setFeedbackTitle(e.target.value)}
            />
            <TextField
              label="내용"
              variant="outlined"
              fullWidth
              margin="normal"
              multiline
              rows={4}
              value={feedbackContent}
              onChange={(e) => setFeedbackContent(e.target.value)}
            />
          </DialogContent>
          <DialogActions>
            <Button onClick={handleCloseFeedback}>취소</Button>
            <Button onClick={handleSendFeedback}>보내기</Button>
          </DialogActions>
        </Dialog>
      </>
  );
}

export default NavBarElements;