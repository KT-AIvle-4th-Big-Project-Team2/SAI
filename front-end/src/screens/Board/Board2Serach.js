import React, { useState, useEffect } from 'react';
import { useParams, Link, useNavigate } from 'react-router-dom';
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
import axios from 'axios';

const ITEMS_PER_PAGE = 10;

// 창업 게시판 글 검색

const Board2Search = () => {
  const [currentPage, setCurrentPage] = useState(1);
  const [boardList, setBoardList] = useState([]);
  const [post_num, setPost_num] = useState('');
  const [Target, setSearchTarget] = useState('title');
  const [Keyword, setSearchKeyword] = useState('');
  const navigate = useNavigate();
  const {searchTarget} = useParams();
  const {searchKeyword} = useParams();

// 검색에 맞는 게시글 호출

  function getBoard() {
    axios.get(`http://subdomain.storeaivle.com/consultboard/postlist/searchpost/${searchTarget}/${searchKeyword}`)
      .then((response) => {
        setBoardList([...response.data]);
        console.log(response.data);
      })
      .catch(function (error) {
        console.log(error);
      });
  };

  useEffect(() => {
    getBoard();
  }, []);


  // Post_Num 관리

  const handleLinkClick = (postId) => {
    setPost_num(postId);
  };

  const handleSearch = () => {
    const encodedSearchTarget = encodeURIComponent(Target);
    const encodedSearchKeyword = encodeURIComponent(Keyword);

    navigate(`/Board2Search/${encodedSearchTarget}/${encodedSearchKeyword}`)
    window.location.reload();
  };

  //페이지 관련 변수
  const startIndex = (currentPage - 1) * ITEMS_PER_PAGE;
  const endIndex = startIndex + ITEMS_PER_PAGE;
  const currentItems = boardList.slice(startIndex, endIndex);
  const totalPages = Math.ceil(boardList.length / ITEMS_PER_PAGE);

  return (
    <div className="container">
      <Box sx={{ height: '100%', mt: 5, mb: 5, width: 'fit-content' }}>
          <span style={{fontSize : 30, fontWeight : 'bold', color : '#012A5B'}}>창업 게시판</span>
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
                    <Link to={`/Board2View/${row.post_id}`} onClick={() => handleLinkClick(row.post_id)}>{row.title}</Link>
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
          <Button variant="contained" href="/Board2Write">
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
            value={Target}
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
        value={Keyword}
        onChange={(e) => setSearchKeyword(e.target.value)}
      />
    <IconButton type="submit" aria-label="search" onClick={handleSearch} >
      <SearchIcon />
    </IconButton>
      </Box>
    </div>
  );
}

export default Board2Search;