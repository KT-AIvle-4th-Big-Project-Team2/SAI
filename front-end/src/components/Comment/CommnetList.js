import React from "react";
import Comment from "./Comment";

const comments = [
    {
        name: "박서준",
        comment: "안녕하세요. 반갑습니다~!",
    },
    {
        name: "한소희",
        comment: "영화가 멋지네요!",
    },
    {
        name: "나영석",
        comment: "내용이 슬퍼요ㅠㅠ",
    },
    {
        name: "송강호",
        comment: "저도 오늘 영화보러 갈거에요:)",
    }
]

function CommentList(props) {
    return (
        <div>
            {comments.map((comment) => {
                return (
                    <Comment name={comment.name} comment={comment.comment} />
                );
            })}
        </div>
    );
}

export default CommentList;