import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import Board from '../../components/Board/Board'

const BoardDetail = () => {
  const { idx } = useParams(); // /board/:idx와 동일한 변수명으로 데이터를 꺼낼 수 있습니다.
  const [loading, setLoading] = useState(true);
  const [board, setBoard] = useState({});


  return (
    <div>
      {loading ? (
        <h2>loading...</h2>
      ) : (
        <Board
          idx={board.idx}
          title={board.title}
          contents={board.contents}
          createdBy={board.createdBy}
        />
      )}
    </div>
  );
};

export default BoardDetail;