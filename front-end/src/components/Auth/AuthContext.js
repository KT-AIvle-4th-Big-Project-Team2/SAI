import React, { createContext, useContext, useState } from 'react';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [isLogin, setIsLogin] = useState(true);
  const [userData, setUserData] = useState(null);
  const [csrfToken, setCsrfToken] = useState('');
  const setCsrfTokenHandler = (token) => {
    setCsrfToken(token);
  };

  const loginHandler = () => {
    setIsLogin(true);
  };

  const logoutHandler = () => {
    setIsLogin(false);
    setUserData(null);
  };

  const setUserInfo = (data) => {
    setUserData(data);
  };

  return (
    <AuthContext.Provider value={{ isLogin, loginHandler, logoutHandler, userData, setUserInfo, csrfToken, setCsrfTokenHandler,}}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  return useContext(AuthContext);
};