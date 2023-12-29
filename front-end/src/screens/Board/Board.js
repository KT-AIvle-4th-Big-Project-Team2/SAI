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
  Box
} from '@mui/material/';
import SearchIcon from '@mui/icons-material/Search';

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
      <SearchIcon style={{ fill: 'blue' }} />
    </IconButton>
  </form>
);

export default function BasicTable() {
  const [searchQuery, setSearchQuery] = useState('');
  const [rows, setRows] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);

  useEffect(() => {
    // Replace this URL with your actual API endpoint
    const apiUrl = 'https://jsonplaceholder.typicode.com/posts';

    fetch(apiUrl)
      .then((response) => {
        console.log(response)
        response.json()
      })
      .then((data) => {
        // You may need to map the data structure from your actual API
        const formattedData = data.map((item) => ({
          name: item.id,
          surname: item.title,
          birthCity: item.userId,
          birthYear: item.id,
        }));
        setRows(formattedData);
      })
      .catch((error) => console.error('Error fetching data:', error));
  }, []);

  // Calculate the index range for the current page
  const startIndex = (currentPage - 1) * ITEMS_PER_PAGE;
  const endIndex = startIndex + ITEMS_PER_PAGE;

  // Get the current page items using the slice method
  const currentItems = rows.slice(startIndex, endIndex);

  // Calculate the total number of pages
  const totalPages = Math.ceil(rows.length / ITEMS_PER_PAGE);

  return (
    <>
    <Box sx={{ mt: 3, mb: 3 }}>
    <h2>창업 게시판</h2>
    </Box>
    <Paper className="Paper" style={{ height: '100%', overflow: 'auto' }}>
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
            {currentItems.map((row) => (
              <TableRow
                key={row.name}
                sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
              >
                <TableCell component="th" scope="row">
                  {row.name}
                </TableCell>
                <TableCell numeric component="a" href="/BoardView ">
                  {row.surname}
                </TableCell>
                <TableCell align="right">{row.birthCity}</TableCell>
                <TableCell align="right">{row.birthYear}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
      
    </Paper>
      <Pagination
        count={totalPages}
        page={currentPage}
        onChange={(event, value) => setCurrentPage(value)}
        showFirstButton
        showLastButton
      />
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: 10 }}>
        <div>
          <SearchBar setSearchQuery={setSearchQuery} />
        </div>
        <div>
          <Button variant="contained" href="/BoardWrite">
            글쓰기
          </Button>
        </div>
      </div>
    </>
  );
}
