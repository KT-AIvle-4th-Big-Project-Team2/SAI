import React, {} from 'react';
import TextField from '@mui/material/TextField';
import { styled } from '@mui/system';
import { Button } from '@mui/material';
import CloudUploadIcon from '@mui/icons-material/CloudUpload';

const VisuallyHiddenInput = styled('input')({
  clip: 'rect(0 0 0 0)',
  clipPath: 'inset(50%)',
  height: 1,
  overflow: 'hidden',
  position: 'absolute',
  bottom: 0,
  left: 0,
  whiteSpace: 'nowrap',
  width: 1,
});

const BoardWrite = () => {
  return (
    <>
    <h4 sx={{mb : 5}}>글쓰기</h4>
    <hr />
    <div align = 'center'>
        <Button component="label" variant="contained" startIcon={<CloudUploadIcon />} align = 'center'>
          Upload file
          <VisuallyHiddenInput type="file" />
        </Button>
        <p></p>
        <div>
            <TextField sx={{width: { sm: 500}}} id='boardTitle' label='Title' name='boardTitle'/>
        </div>
        &nbsp;
        <div>
            <TextField sx={{width: { sm: 500},"& .MuiInputBase-root": {height: 200}}} id='boardTitle' label='content' name='boardTitle'/>
        </div>
        <p></p>
      <Button variant="contained" href="/Board">글쓰기</Button>
      <Button variant="contained" sx={{m : 5}} href="/Board">취소</Button>
    </div>
    </>
  );
};

export default BoardWrite;