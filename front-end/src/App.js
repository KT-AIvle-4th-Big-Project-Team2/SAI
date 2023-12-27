import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import 'bootstrap/dist/css/bootstrap.min.css';
import Home from './screens/Home';
import Index from './screens/Index';
import Board from './screens/Board/Board';
import Login from './screens/Login/login';
import NavBarElements from './components/NavBar/NavBarElements';
import SignUp from './screens/Login/SignUp';
import BoardDetail from './screens/Board/BoardView';
import BoardWrite from './screens/Board/BoardWrite';
import Notice from './screens/Notice/Notice';
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

function App() {
  return (
    <Router>
      <NavBarElements />
      
      <Container>
        <Routes>
          <Route path = "/" element = { <Index /> } />
          <Route path = "/Notice" element = { <Notice /> } />
          <Route path = "/FAQ" element = { <FAQ /> } />
          <Route path = "/Home" element = { <Home /> } />
          <Route path = "/Board" element = { <Board /> } />
          <Route path = "/Login" element = { <Login /> } />
          <Route path = "/signup" element = { <SignUp /> } />
          <Route path = "/BoardView" element = { <BoardDetail /> } />
          <Route path = "/BoardWrite" element = { <BoardWrite /> } />
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
      </Container>
    </Router>
  );
}

export default App;
