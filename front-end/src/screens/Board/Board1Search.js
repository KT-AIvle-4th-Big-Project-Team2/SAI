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
import DivLine from '../../components/Styles/DivLine';
import axios from 'axios';

const ITEMS_PER_PAGE = 10;

const Board1Search = () => {
  const [rows, setRows] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [boardList, setBoardList] = useState([]);
  const [post_num, setPost_num] = useState('');
  const [Target, setSearchTarget] = useState('');
  const [Keyword, setSearchKeyword] = useState('');

  const {searchTarget} = useParams();
  const {searchKeyword} = useParams();

  function getNotice() {
    axios.get(`https://subdomain.storeaivle.com/board/postlist/searchpost/${searchTarget}/${searchKeyword}`)
      .then((response) => {
        setBoardList([...response.data]);
        console.log(response.data);
      })
      .catch(function (error) {
        console.log(error);
      });
  };

  useEffect(() => {
    getNotice(); // 1) 게시글 목록 조회 함수 호출
  }, []);

  console.log(boardList);

  const handleLinkClick = (postId) => {
    setPost_num(postId);
  };

  const handleSearch = () => {
    // Perform search based on searchTarget and searchKeyword
    console.log("Search Target:", searchTarget);
    console.log("Search Keyword:", searchKeyword);

    // You can call the setSearchQuery function here if needed
  };

  // Calculate the index range for the current page
  const startIndex = (currentPage - 1) * ITEMS_PER_PAGE;
  const endIndex = startIndex + ITEMS_PER_PAGE;

  // Get the current page items using the slice method
  const currentItems = boardList.slice(startIndex, endIndex);

  // Calculate the total number of pages
  const totalPages = Math.ceil(boardList.length / ITEMS_PER_PAGE);

  return (
    <>

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
          <Button variant="outlined" href="/Board1Write" style={{ color: 'black' }}>
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
    </>
  );
}

export default Board1Search;