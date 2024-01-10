import React, { createContext, useContext, useState } from 'react';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const storedIsLogin = localStorage.getItem('isLogin');
  const [isLogin, setIsLogin] = useState(storedIsLogin === 'true');
  const [userData, setUserData] = useState(null);

  const loginHandler = () => {
    setIsLogin(true);
    localStorage.setItem('isLogin', 'true');
  };

  const logoutHandler = () => {
    setIsLogin(false);
    setUserData(null);
    localStorage.removeItem('isLogin');
    localStorage.removeItem('userData');
  };

  const setUserInfo = (data) => {
    setUserData(data);
    // userData를 localStorage에 저장
    localStorage.setItem('userData', JSON.stringify(data));
  };

  const contextValue = {
    isLogin,
    loginHandler,
    logoutHandler,
    userData,
    setUserInfo,
  };

  return <AuthContext.Provider value={contextValue}>{children}</AuthContext.Provider>;
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};

// useAuth 사용법
// const { userData, setUserInfo } = useAuth();

// useEffect(() => {
//   // 컴포넌트가 마운트될 때 localStorage에서 userData를 불러와서 상태에 업데이트
//   const storedUserData = localStorage.getItem('userData');
//   if (storedUserData) {
//     setUserInfo(JSON.parse(storedUserData));
//   }
// }, []); // 두 번째 매개변수로 빈 배열을 전달하여 컴포넌트가 마운트될 때 한 번만 실행

// // 나머지 컴포넌트 렌더링 로직...