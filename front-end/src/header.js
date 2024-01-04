import React, { useState, useEffect } from 'react';
import axios from 'axios'

const Header = () => {
    const [csrf, setCsrf] = useState('');
    function getCsrfToken() {
      axios
        .get(`http://127.0.0.1:8000/accounts/getcsrf/`)
        .then((response) => {
          const csrfToken = response.data; // 단일 값으로 변경
          setCsrf(csrfToken);
          console.log(csrfToken);
          // 성공적으로 업데이트된 경우 페이지 이동
        })
        .catch((error) => {
          console.error(error);
          // 오류 발생 시 처리
        });
    }
  
    useEffect(() => {
      getCsrfToken(); // CSRF 토큰 조회 함수 호출
    }, []);


  return (
    <div>header</div>
  )
}

export default Header