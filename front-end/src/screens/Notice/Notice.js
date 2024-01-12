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
import axios from 'axios'
import { Link, useNavigate } from 'react-router-dom';

// 페이지 관련 변수 정리

const ITEMS_PER_PAGE = 10;

// 공지사항 보기

const Notice = () => {

  const navigate = useNavigate();
  const [rows, setRows] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [NoticeList, setNoticeList] = useState([]);
  const [post_num, setPost_num] = useState('');
  const [searchTarget, setSearchTarget] = useState('title');
  const [searchKeyword, setSearchKeyword] = useState('');

  // 공지사항 받아오기

  function getNotice() {
    axios.get("http://subdomain.storeaivle.com/announcement/announcementlist/")
      .then((response) => {
        setNoticeList([...response.data]);
        console.log(response.data);
      })
      .catch(function (error) {
        console.log(error);
      });
  };


  
  useEffect(() => {
    getNotice();
  }, []);


  // 페이지 갯수 확인
  const startIndex = (currentPage - 1) * ITEMS_PER_PAGE;
  const endIndex = startIndex + ITEMS_PER_PAGE;
  const currentItems = rows.slice(startIndex, endIndex);
  const totalPages = Math.ceil(rows.length / ITEMS_PER_PAGE);

  // Post_num 관리
  const handleLinkClick = (postId) => {
    setPost_num(postId);
  };

  // 게시판 글 검색

  const handleSearch = () => {
    // Perform search based on searchTarget and searchKeyword
    console.log("Search Target:", searchTarget);
    console.log("Search Keyword:", searchKeyword);
  
    // URL 인코딩 적용
    const encodedSearchTarget = encodeURIComponent(searchTarget);
    const encodedSearchKeyword = encodeURIComponent(searchKeyword);
  
    // URL을 동적으로 생성하여 이동
    const searchUrl = `/announcement/announcementlist/${encodedSearchTarget}/${encodedSearchKeyword}`;
  
  
    // React Router의 history 객체를 사용하여 페이지 이동
    navigate(searchUrl);
  };


  return (
    <div className="container">
      <Box sx={{ height: '100%', mt: 5, mb: 5, width: 'fit-content' }}>
          <span style={{fontSize : 30, fontWeight : 'bold', color : '#012A5B'}}>공지사항</span>
      </Box>
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
                {NoticeList.map((row) => (
                  <TableRow
                    key={row.announcement_id}
                    sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                  >
                    <TableCell component="th" scope="row">
                      {row.announcement_id}
                    </TableCell>
                    <TableCell numeric='true'>
                    <Link to={`/NoticeView/${row.announcement_id}`} onClick={() => handleLinkClick(row.announcement_id)}>{row.title}</Link>
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
            color="primary"
          />
                
        <div>
            {/* <Button variant="contained" href="/NoticeWrite" >
              글쓰기
            </Button> */}
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

export default Notice;