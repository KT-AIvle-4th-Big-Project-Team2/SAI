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

function App() {
  return (
    <Router>
      <NavBarElements />
        <Routes>
          <Route path = "/" element = { <Index /> } />
          <Route path = "/Home" element = { <Home /> } />
          <Route path = "/Board" element = { <Board /> } />
          <Route path = "/Questions" element = { <Questions /> } />
          <Route path = "/ReactsDoc" element = { <ReactsDoc /> } />
          <Route path = "/Login" element = { <Login /> } />
          <Route path = "/signup" element = { <SignUp /> } />
          <Route path = "/BoardView" element = { <BoardDetail /> } />
          <Route path = "/BoardWrite" element = { <BoardWrite /> } />
      </Routes>
    </Router>
  );
}

export default App;
