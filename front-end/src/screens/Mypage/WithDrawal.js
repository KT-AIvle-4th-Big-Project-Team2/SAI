import React, { useState } from 'react';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Dialog from '@mui/material/Dialog';
import DialogTitle from '@mui/material/DialogTitle';
import DialogContent from '@mui/material/DialogContent';
import DialogActions from '@mui/material/DialogActions';
import Snackbar from '@mui/material/Snackbar';
import MuiAlert from '@mui/material/Alert';

function Alert(props) {
  return <MuiAlert elevation={6} variant="filled" {...props} />;
}

const Withdrawal = () => {
  const [isModalOpen, setModalOpen] = useState(false);
  const [isSnackbarOpen, setSnackbarOpen] = useState(false);

  const handleWithdrawal = () => {
    setModalOpen(true);
  };

  const handleConfirmWithdrawal = () => {
    // 여기에서 실제 회원 탈퇴 로직을 수행할 수 있습니다.
    // ...

    // 회원 탈퇴가 완료되면 알림을 띄우고 모달을 닫습니다.
    setSnackbarOpen(true);
    setModalOpen(false);
  };

  const handleCancelWithdrawal = () => {
    setModalOpen(false);
  };

  const handleSnackbarClose = (event, reason) => {
    if (reason === 'clickaway') {
      return;
    }

    setSnackbarOpen(false);
  };

  return (
    <Box sx={{ display: 'flex', justifyContent: 'flex-end' }}>
      <Button
        variant="contained"
        color="error"
        onClick={handleWithdrawal}
      >
        회원 탈퇴
      </Button>

      {/* 회원 탈퇴 모달 */}
      <Dialog open={isModalOpen} onClose={handleCancelWithdrawal}>
        <DialogTitle>회원 탈퇴</DialogTitle>
        <DialogContent>
          <p>회원 탈퇴 하시겠습니까?</p>
        </DialogContent>
        <DialogActions>
          <Button onClick={handleCancelWithdrawal} color="primary">
            아니오
          </Button>
          <Button onClick={handleConfirmWithdrawal} color="primary">
            예
          </Button>
        </DialogActions>
      </Dialog>

      {/* 회원 탈퇴 알림 */}
      <Snackbar
        open={isSnackbarOpen}
        autoHideDuration={6000}
        onClose={handleSnackbarClose}
      >
        <Alert onClose={handleSnackbarClose} severity="success">
          회원 탈퇴가 완료되었습니다.
        </Alert>
      </Snackbar>
    </Box>
  );
};

export default Withdrawal;