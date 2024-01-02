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
  IconButton,
  TextField,
  Box,
} from '@mui/material/';
import SearchIcon from '@mui/icons-material/Search';
import DivLine from '../../components/Styles/DivLine';
import axios from 'axios'
import { Link } from 'react-router-dom';

const ITEMS_PER_PAGE = 10;

const SearchBar = ({ setSearchQuery }) => (
  <form>
    <TextField
      id="search-bar"
      className="text"
      onInput={(e) => {
        setSearchQuery(e.target.value);
      }}
      label="Search"
      variant="outlined"
      placeholder="Search..."
      size="small"
    />
    <IconButton type="submit" aria-label="search">
      <SearchIcon style={{ fill: 'lime' }} />
    </IconButton>
  </form>
);


export default function BasicTable() {
  const [searchQuery, setSearchQuery] = useState('');
  const [rows, setRows] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [boardList, setBoardList] = useState([]);
  const [post_num, setPost_num] = useState('');
  function getNotice() {
    axios.get("http://127.0.0.1:8000/board/postlist/")
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

  console.log(boardList)
  // Calculate the index range for the current page
  const startIndex = (currentPage - 1) * ITEMS_PER_PAGE;
  const endIndex = startIndex + ITEMS_PER_PAGE;

  
  const handleLinkClick = (postId) => {
    setPost_num(postId);
  };

  // Get the current page items using the slice method
  const currentItems = rows.slice(startIndex, endIndex);

  // Calculate the total number of pages
  const totalPages = Math.ceil(rows.length / ITEMS_PER_PAGE);
  console.log(boardList)
  return (
      <>
        <Box sx={{ height: '100%', mt: 3, mb: 3, width: 'fit-content' }}>
          <h2 >공지사항</h2>
        </Box>
        <DivLine />
        <Paper className="Paper" border={1} p={2} style={{ height: '100%', overflow: 'auto' }}>
          <TableContainer component={Paper} style={{ height: '100%' }}>
            <Table sx={{ minWidth: 650 }} aria-label="simple table">
              <TableHead>
                <TableRow>
                  <TableCell>번호</TableCell>
                  <TableCell>글 내용</TableCell>
                  <TableCell align="right">작성자</TableCell>
                  <TableCell align="right">작성일</TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {boardList.map((row) => (
                  <TableRow
                    key={row.post_id}
                    sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                  >
                    <TableCell component="th" scope="row">
                      {row.post_id}
                    </TableCell>
                    <TableCell numeric='true'>
                    <Link to={`/BoardView/${row.post_id}`} onClick={() => handleLinkClick(row.post_id)}>{row.title}</Link>
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
          color = 'primary'
        />
        
        <div>
            <Button variant="outlined" href="/BoardWrite"  style={{ color: 'black' }}>
              글쓰기
            </Button>
          </div>
        </div>
          <div>
            <SearchBar setSearchQuery={setSearchQuery} />
          </div>
      </>
  );
}