import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import 'bootstrap/dist/css/bootstrap.min.css';
import Layout from './Layout'
import Home from './screens/Home';
import Index from './screens/Index';
import Board from './screens/Board/Board';
import Questions from './screens/Questions';
import ReactsDoc from './screens/ReactsDoc';
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

function App() {
  return (
    <Router>
      <NavBarElements />
        <Routes>
          <Route path = "/" element = { <Index /> } />
          <Route path = "/Notice" element = { <Notice /> } />
          <Route path = "/Home" element = { <Home /> } />
          <Route path = "/Board" element = { <Board /> } />
          <Route path = "/Questions" element = { <Questions /> } />
          <Route path = "/ReactsDoc" element = { <ReactsDoc /> } />
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

      </Routes>
    </Router>
  );
}

export default App;
