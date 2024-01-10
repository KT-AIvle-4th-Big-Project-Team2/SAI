import React from 'react';
import Dialog from '@mui/material/Dialog';
import DialogTitle from '@mui/material/DialogTitle';
import DialogContent from '@mui/material/DialogContent';
import DialogActions from '@mui/material/DialogActions';
import Button from '@mui/material/Button';
import Accordion from '@mui/material/Accordion';
import AccordionSummary from '@mui/material/AccordionSummary';
import AccordionDetails from '@mui/material/AccordionDetails';
import Typography from '@mui/material/Typography';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';

const TermsModal = ({ open, onClose }) => {
  return (
    <Dialog open={open} onClose={onClose} fullWidth maxWidth="md">
      <DialogTitle>이용약관</DialogTitle>
      <DialogContent>
            <Typography>개인정보 수집 및 이용 동의서</Typography>
            <br></br>
            <Typography>SAI 서비스 이용과 관련하여 SAI에서 개인정보를 처리하는 것에 동의합니다.</Typography>
            <br></br>
            <Typography>처리하는 개인정보</Typography>
            <Typography>이메일, 비밀번호, 닉네임, 성명, 휴대전화번호, 생년월일, 성별</Typography>
            <br></br>
            <Typography>개인정보 처리 목적</Typography>
            <Typography>본인확인 및 본인 인증, 서비스 제공, 서비스 민원처리, 서비스 품질 개선 및 신규 서비스 개발을 위한 통계관리</Typography>
            <br/>
            <Typography>개인정보 이용 보유기간</Typography>
            <Typography>회원탈퇴 시 까지</Typography>
            <br/>
            <Typography>위 개인정보 처리에 동의하십니까?</Typography>
            <Typography>□ 동의하지않음     □ 동의함</Typography>
            <br/>
            <Typography>동의를 거부할 수 있습니다.</Typography>
            <Typography>다만, 개인정보 수집 동의 거부 시 SAI 회원가입에 제한이 발생합니다.</Typography>
            <Typography>공고 일자: 2024. 01. 12</Typography>
            <Typography>시행 일자: 2024. 01. 12</Typography>
      </DialogContent>
      <DialogActions>
        <Button onClick={onClose} color="primary">
          닫기
        </Button>
      </DialogActions>
    </Dialog>
  );
};

export default TermsModal;