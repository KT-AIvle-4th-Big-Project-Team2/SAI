import * as React from 'react';
import { useState , useEffect } from "react";
import 
{Table,
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
}
from '@mui/material/';
import SearchIcon from "@mui/icons-material/Search";
import axios from "axios";


// const SearchBar = ({setSearchQuery}) => (
//   <form>
//     <TextField
//       id="search-bar"
//       className="text"
//       onInput={(e) => {
//         setSearchQuery(e.target.value);
//       }}
//       label="Search"
//       variant="outlined"
//       placeholder="Search..."
//       size="small"
//     />
//     <IconButton type="submit" aria-label="search">
//       <SearchIcon style={{ fill: "blue" }} />
//     </IconButton>
//   </form>
// );

const rows = [          {name: 'Mehmet', surname: '안녕하세요 ^^ 5-1', birthYear: 1987, birthCity: 63},
{name: 'Zerya Betül', surname: '글 제목입니다.', birthYear: 2017, birthCity: 34},
{name: 'Bread', surname: '게시판 테스트', birthYear: 2011, birthCity: 34},
{name: 'Jonny', surname: 'Material-table 이용하기', birthYear: 2012, birthCity: 17},
{name: 'Sera', surname: '페이징 처리 이용하기', birthYear: 2007, birthCity: 17},
{name: 'Simson', surname: '테스트 데이터 5-2', birthYear: 1999, birthCity: 8},
{name: 'Cerry', surname: '야호 ㅋㅋ!!', birthYear: 1997, birthCity: 53},
{name: 'Zebra', surname: '잘 넘어가나요?', birthYear: 1987, birthCity: 15},
{name: 'M.J.', surname: '오키오키 ', birthYear: 1999, birthCity: 54},
{name: 'K.Son', surname: 'ㅋ아니..', birthYear: 2002, birthCity: 37},
{name: 'Json', surname: '넵 열심히 하겠습니다 5-3', birthYear: 2015, birthCity: 98},
{name: 'Merry', surname: 'MacBook Pro 팔아요', birthYear: 2017, birthCity: 11},
{name: 'Mehmet', surname: '안녕하세요 ^^', birthYear: 1987, birthCity: 63},
{name: 'Zerya Betül', surname: '글 제목입니다.', birthYear: 2017, birthCity: 34},
{name: 'Bread', surname: '게시판 테스트', birthYear: 2011, birthCity: 34},
{name: 'Jonny', surname: 'Material-table 이용하기 5-4', birthYear: 2012, birthCity: 17},
{name: 'Sera', surname: '페이징 처리 이용하기', birthYear: 2007, birthCity: 17},
{name: 'Simson', surname: '테스트 데이터', birthYear: 1999, birthCity: 8},
{name: 'Cerry', surname: '야호 ㅋㅋ!!', birthYear: 1997, birthCity: 53},
{name: 'Zebra', surname: '잘 넘어가나요?', birthYear: 1987, birthCity: 15},
{name: 'M.J.', surname: '오키오키 5-5', birthYear: 1999, birthCity: 54},
{name: 'K.Son', surname: 'ㅋ아니..', birthYear: 2002, birthCity: 37},
{name: 'Json', surname: '넵 열심히 하겠습니다', birthYear: 2015, birthCity: 98},
{name: 'Merry', surname: 'MacBook Pro 팔아요', birthYear: 2017, birthCity: 11},
{name: 'Mehmet', surname: '안녕하세요 ^^', birthYear: 1987, birthCity: 63},
{name: 'Zerya Betül', surname: '글 제목입니다. 5-6', birthYear: 2017, birthCity: 34},
{name: 'Bread', surname: '게시판 테스트', birthYear: 2011, birthCity: 34},
{name: 'Jonny', surname: 'Material-table 이용하기', birthYear: 2012, birthCity: 17},
{name: 'Sera', surname: '페이징 처리 이용하기', birthYear: 2007, birthCity: 17},
{name: 'Simson', surname: '테스트 데이터', birthYear: 1999, birthCity: 8},
{name: 'Cerry', surname: '야호 ㅋㅋ!! 5-7', birthYear: 1997, birthCity: 53},
{name: 'Zebra', surname: '잘 넘어가나요?', birthYear: 1987, birthCity: 15},
{name: 'M.J.', surname: '오키오키 ', birthYear: 1999, birthCity: 54},
{name: 'K.Son', surname: 'ㅋ아니..', birthYear: 2002, birthCity: 37},
{name: 'Json', surname: '넵 열심히 하겠습니다', birthYear: 2015, birthCity: 98},
{name: 'Merry', surname: 'MacBook Pro 팔아요 5-8', birthYear: 2017, birthCity: 11},
{name: 'Mehmet', surname: '안녕하세요 ^^', birthYear: 1987, birthCity: 63},
{name: 'Zerya Betül', surname: '글 제목입니다.', birthYear: 2017, birthCity: 34},
{name: 'Bread', surname: '게시판 테스트', birthYear: 2011, birthCity: 34},
{name: 'Jonny', surname: 'Material-table 이용하기', birthYear: 2012, birthCity: 17},
{name: 'Sera', surname: '페이징 처리 이용하기 5-9', birthYear: 2007, birthCity: 17},
{name: 'Simson', surname: '테스트 데이터', birthYear: 1999, birthCity: 8},
{name: 'Cerry', surname: '야호 ㅋㅋ!!', birthYear: 1997, birthCity: 53},
{name: 'Zebra', surname: '잘 넘어가나요?', birthYear: 1987, birthCity: 15},
{name: 'M.J.', surname: '오키오키 ', birthYear: 1999, birthCity: 54},
{name: 'K.Son', surname: 'ㅋ아니.. 5-10', birthYear: 2002, birthCity: 37},
{name: 'Json', surname: '넵 열심히 하겠습니다', birthYear: 2015, birthCity: 98},
{name: 'Merry', surname: '마지막 데이터입니다!!!!!!!', birthYear: 2017, birthCity: 11}
];

export default function BasicTable() {

  const [boarddata, setboarddata] = useState([]);
//  const [posts, setPosts] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/board')
      .then(response => {
        setboarddata(response.data);
      })
      .catch(error => {
        console.error('Error fetching posts', error);
      });
  }, []);  

  
  console.log(boarddata)

  return (
    <Paper className='Paper'>
    <TableContainer component={Paper}>
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
          {rows.map((rows) => (
            <TableRow
              key={rows.board_id}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell component="th" scope="row" >
                {rows.board_id}
              </TableCell>
              <TableCell numeric component="a" href="/BoardView " >{rows.title}</TableCell>
              <TableCell align="right">{rows.contents}</TableCell>
              <TableCell align="right">{rows.tag}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
    <Pagination count={10} showFirstButton showLastButton />
    <div align = 'right'>
    <Button variant="contained" href = '/BoardWrite'>글쓰기</Button>
    </div>
    <div
      style={{
        display: "flex",
        alignSelf: "center",
        justifyContent: "center",
        flexDirection: "column",
        padding: 20
      }}
    >
      
      <div style={{ padding: 3 }}>
      </div>
    </div>

    </Paper>
  );
}