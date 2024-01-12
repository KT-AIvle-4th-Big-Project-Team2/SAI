import React, { createContext, useContext, useState } from 'react';

const AuthContext = createContext();

//유저 정보 관리 컴포넌트

export const AuthProvider = ({ children }) => {
  const storedIsLogin = localStorage.getItem('isLogin');
  const [isLogin, setIsLogin] = useState(storedIsLogin === 'true');
  const [userData, setUserData] = useState(null);

  //로그인 상태 관리
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

  //유저 정보 저장
  const setUserInfo = (data) => {
    setUserData(data);
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