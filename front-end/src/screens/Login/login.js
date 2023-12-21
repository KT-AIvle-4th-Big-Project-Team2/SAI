import React from 'react'
import 'mdb-react-ui-kit/dist/css/mdb.min.css';
import "@fortawesome/fontawesome-free/css/all.min.css";
import {
  MDBBtn,
  MDBContainer,
  MDBRow,
  MDBCol,
  MDBIcon,
  MDBInput
}
from 'mdb-react-ui-kit';

const login = () => {
  return (
    <MDBContainer fluid>
      <MDBRow>

        <MDBCol sm='6'>

          <div className='d-flex flex-row ps-5 pt-5'>
            <MDBIcon fas icon="crow fa-3x me-3" style={{ color: '#709085' }}/>
            <span className="h1 fw-bold mb-0">Logo</span>
          </div>

          <div className='d-flex flex-column justify-content-center h-custom-2 w-75 pt-4'>

            <h3 className="fw-normal mb-3 ps-5 pb-3" style={{letterSpacing: '1px'}}>로그인</h3>

            <MDBInput wrapperClass='mb-4 mx-5 w-100' label='Email address' id='formControlLg' type='email' size="lg"/>
            <MDBInput wrapperClass='mb-3 mx-5 w-100' label='Password' id='formControlLg' type='password' size="lg"/>
            <p className="small mb-4 pb-lg-3 ms-5"><a class="text-muted">비밀번호는 영문, 숫자, 특수문자를 포함한 8~12자리입니다.</a></p>
            <MDBBtn className="mb-4 px-5 mx-5 w-100" color='info' size='lg'>Login</MDBBtn>
            <p className="small mb-5 pb-lg-3 ms-5"><a class="text-muted" href="/FindID">비밀번호를 잊으셨나요?</a></p>
            <p className='ms-5'>계정이 없으신가요? <a href="/SignUp" class="link-info">회원가입</a></p>

          </div>

        </MDBCol>

        <MDBCol sm='6' className='d-none d-sm-block px-0'>
          <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-login-form/img3.webp"
            alt="Login image" className="w-100" style={{objectFit: 'cover', objectPosition: 'left'}} />
        </MDBCol>

      </MDBRow>

    </MDBContainer>
  )
}

export default login