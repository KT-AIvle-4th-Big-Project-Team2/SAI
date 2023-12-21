import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import 'bootstrap/dist/css/bootstrap.min.css';
import Home from './screens/Home';
import Index from './screens/Index';
import Board from './screens/Board/Board';
import Questions from './screens/Questions';
import ReactsDoc from './screens/ReactsDoc';
import NavBarElements from './components/NavBar/NavBarElements';

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
      </Routes>
    </Router>
  );
}

export default App;
