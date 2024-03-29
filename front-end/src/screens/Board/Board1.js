import React, { useState, useEffect } from 'react';
import {
  Table,
  TableBody,
  TableContainer,
  TableHead,
  TableRow,
  TableCell,
  Paper,
  Pagination,
  Button,
  FormControl,
  InputLabel,
  Select,
  MenuItem,
  TextField,
  Box,
  IconButton
} from '@mui/material/';
import SearchIcon from '@mui/icons-material/Search';
import { Link, useNavigate } from 'react-router-dom';

const ITEMS_PER_PAGE = 10;

const Board1 = () => {

  const navigate = useNavigate();
  const [currentPage, setCurrentPage] = useState(1);
  const [boardList, setBoardList] = useState([]);
  const [post_num, setPost_num] = useState('');
  const [searchTarget, setSearchTarget] = useState('title');
  const [searchKeyword, setSearchKeyword] = useState('');

  // 게시판 글 조회 함수

  function getBoard() {
    fetch("http://subdomain.storeaivle.com/board/postlist/")
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        setBoardList([...data]);
        console.log(data);
      })
      .catch((error) => {
        console.log(error);
      });
  }
  
  useEffect(() => {
    getBoard();
  }, []);

  console.log(boardList);

  const handleLinkClick = (postId) => {
    setPost_num(postId);
  };

  const handleSearch = () => {
    console.log("Search Target:", searchTarget);
    console.log("Search Keyword:", searchKeyword);
  
    // URL 인코딩 적용
    const encodedSearchTarget = encodeURIComponent(searchTarget);
    const encodedSearchKeyword = encodeURIComponent(searchKeyword);

    // URL을 동적으로 생성하여 이동
    const searchUrl = `/Board1Search/${encodedSearchTarget}/${encodedSearchKeyword}`;
  
    console.log("Encoded Search Target:", encodedSearchTarget);
    console.log("Encoded Search Keyword:", encodedSearchKeyword);
  
    navigate(searchUrl);
  };

  // 페이지 관련 변수들
  
  const startIndex = (currentPage - 1) * ITEMS_PER_PAGE;
  const endIndex = startIndex + ITEMS_PER_PAGE;
  const currentItems = boardList.slice(startIndex, endIndex);
  const totalPages = Math.ceil(boardList.length / ITEMS_PER_PAGE);



  return (
    <div className="container">      
    <Box sx={{ height: '100%', mt: 5, mb: 5, width: 'fit-content' }}>
        <span style={{fontSize : 30, fontWeight : 'bold', color : '#012A5B'}}>창업 정보</span>
    </Box>

      <Paper className="Paper" border={1} p={2} style={{ height: '100%', overflow: 'auto' }}>
        <TableContainer component={Paper} style={{ height: '100%' }}>
          <Table sx={{ minWidth: 650 }} aria-label="simple table">
            <TableHead>
              <TableRow>
                <TableCell>번호</TableCell>
                <TableCell>글 제목</TableCell>
                <TableCell align="right">작성자</TableCell>
                <TableCell align="right">작성일</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {currentItems.map((row) => (
                <TableRow
                  key={row.post_id}
                  sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                >
                  <TableCell component="th" scope="row">
                    {row.post_id}
                  </TableCell>
                  <TableCell numeric='true'>
                    <Link to={`/Board1View/${row.post_id}`} onClick={() => handleLinkClick(row.post_id)}>{row.title}</Link>
                  </TableCell>
                  <TableCell align="right">{row.name}</TableCell>
                  <TableCell align="right">{row.date}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </Paper>

      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: 10 }}>
        <Pagination
          count={totalPages}
          page={currentPage}
          onChange={(event, value) => setCurrentPage(value)}
          showFirstButton
          showLastButton
          color='primary'
        />

        <div>
          <Button variant="contained" href="/Board1Write">
            글쓰기
          </Button>
        </div>
      </div>

      
      <Box>
        <FormControl>
          <InputLabel id="search-target-label">검색 대상</InputLabel>
          <Select
            labelId="search-target-label"
            id="search-target"
            value={searchTarget}
            label="검색 대상"
            onChange={(e) => setSearchTarget(e.target.value)}
          >
            <MenuItem value="title">제목</MenuItem>
            <MenuItem value="name">작성자</MenuItem>
          </Select>
        </FormControl>
        <TextField
        id="search-keyword"
        label="검색어"
        value={searchKeyword}
        onChange={(e) => setSearchKeyword(e.target.value)}
      />
    <IconButton type="submit" aria-label="search" onClick={handleSearch} >
    <Link to={`/Board1Search/${searchTarget}/${searchKeyword}`}>
      <SearchIcon />
      </Link>
    </IconButton>
      </Box>
    </div>
  );
}

export default Board1;