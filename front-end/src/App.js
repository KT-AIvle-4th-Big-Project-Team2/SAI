import './App.css';
import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import Home from './screens/Home';
import Index from './screens/Index';
import Board1 from './screens/Board/Board1';
import Board1Mod from './screens/Board/Board1Mod';
import Board1View from './screens/Board/Board1View';
import Board1Write from './screens/Board/Board1Write';
import Board1Search from './screens/Board/Board1Search';
import Board2 from './screens/Board/Board2';
import Board2Mod from './screens/Board/Board2Mod';
import Board2View from './screens/Board/Board2View';
import Board2Write from './screens/Board/Board2Write';
import Board2Search from './screens/Board/Board2Serach';
import Login from './screens/Login/login';
import NavBarElements from './components/NavBar/NavBarElements';
import SignUp from './screens/Login/SignUp';
import Notice from './screens/Notice/Notice';
import NoticeMod from './screens/Notice/NoticeMod';
import NoticeView from './screens/Notice/NoticeView';
import NoticeWrite from './screens/Notice/NoticeWrite';
import NoticeSearch from './screens/Notice/NoticeSearch';
import FindID from './screens/Login/FindID';
import Simul from './screens/Simul/Simul';
import Simul2 from './screens/Simul/Simul2';
import SimulReport from './screens/Simul/SimulReport';
import AreaAnaly from './screens/Analysis/AreaAnaly';
import SectorsAnaly from './screens/Analysis/SectorsAnaly';
import Myboard from './screens/Mypage/Myboard';
import Myinfo from './screens/Mypage/Myinfo';
import WithDrawal from './screens/Mypage/WithDrawal';
import Container from 'react-bootstrap/Container'
import FAQ from './screens/Notice/FAQ';
import MyinfoCheck from './screens/Mypage/MyinfoCheck';
import Header from './header';




function App() {
  const [headers, setHeaders] = useState({});


  return (
    <Router>
      <NavBarElements />
      <Header />
        <Routes>
          
          <Route path = "/" element = { <Index /> } />
          <Route path = "/Notice" element = { <Notice /> } />
          <Route path = "/NoticeWrite" element = { <NoticeWrite /> } />
          <Route path = "/NoticeView/:post_num" element={<NoticeView />} />
          <Route path = "/NoticeMod/:post_num" element={<NoticeMod />} />
          <Route path = "/NoticeSearch/:searchTarget/:searchKeyword" element={<NoticeSearch />} />
          <Route path = "/FAQ" element = { <FAQ /> } />
          <Route path = "/Home" element = { <Home /> } />
          <Route path = "/Board1" element = { <Board1 /> } />
          <Route path = "/Board1Write" element = { <Board1Write /> } />
          <Route path = "/Board1View/:post_num" element={<Board1View />} />
          <Route path = "/Board1Mod/:post_num" element={<Board1Mod />} />
          <Route path = "/Board1Search/:searchTarget/:searchKeyword" element={<Board1Search />} />
          <Route path = "/Board2" element = { <Board2 /> } />
          <Route path = "/Board2Write" element = { <Board2Write /> } />
          <Route path = "/Board2View/:post_num" element={<Board2View />} />
          <Route path = "/Board2Mod/:post_num" element={<Board2Mod />} />
          <Route path = "/Board2Search/:searchTarget/:searchKeyword" element={<Board2Search />} />
          <Route path = "/Login" element = { <Login /> } />
          <Route path = "/signup" element = { <SignUp /> } />
          <Route path = "/FindID" element = { <FindID /> } />
          <Route path = "/Simul" element = { <Simul /> } />
          <Route path = "/Simul2" element = { <Simul2 /> } />
          <Route path = "/SimulReport" element = { <SimulReport /> } />
          <Route path = "/Area" element = { <AreaAnaly /> } />
          <Route path = "/Sectors" element = { <SectorsAnaly /> } />
          <Route path = "/Myboard" element = { <Myboard /> } />
          <Route path = "/Myinfo" element = { <Myinfo /> } />
          <Route path = "/WithDrawal" element = { <WithDrawal /> } />
          <Route path = "/MyinfoCheck" element = { <MyinfoCheck /> } />
      </Routes>
    </Router>
  );
}

export default App;
