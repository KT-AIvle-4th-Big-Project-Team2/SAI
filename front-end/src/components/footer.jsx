import React, {useState} from 'react'
import {Box, Typography } from "@mui/material/";
import { Link } from 'react-router-dom';
import Service from './Service';
import PrivacyPolicy from './PrivacyPolicy';


const Footer = () => {
  const scrollToTop = () => {
    window.scrollTo(0, 0);
  };

  const [isServiceModalOpen, setServiceModalOpen] = useState(false);
  const [isPrivacyModalOpen, setPrivacyModalOpen] = useState(false);

  const openServiceModal = () => setServiceModalOpen(true);
  const closeServiceModal = () => setServiceModalOpen(false);

  const openPrivacyModal = () => setPrivacyModalOpen(true);
  const closePrivycyModal = () => setPrivacyModalOpen(false);

  return (
    <>
      <Box sx={{ bgcolor: '#012A5B', width: '100%', height: '180px', color: 'white' }}>
        <div className='container'>
          <Box sx={{ display: 'flex', justifyContent: 'space-between', width: '28%', paddingTop: 3 }}>
          <Link to="/" style={{ textDecoration: 'none', color : 'white' }} onClick={scrollToTop}>
            <Typography sx={{fontSize : 15}}>
              서비스 소개
            </Typography >
          </Link>
            <Typography sx={{fontSize : 15}} onClick={() => openServiceModal()} style={{ cursor: 'pointer' }}>
                이용 약관
            </Typography>
          <Typography sx={{fontSize : 15}} onClick={() => openPrivacyModal()} style={{ cursor: 'pointer' }}>
            개인정보 처리 방침
          </Typography>
          </Box>
          <Box sx={{ marginTop: 3}}>
            <Typography sx={{fontSize : 15}}>SAI</Typography>
            <Typography sx={{fontSize : 15}}>
              KT AIVLE SCHOOL 4기 2조ㅣ오진원 김수현 김수환 신진한 안예린 윤경상 이웅희 | E-mail : aivle4team2@gmail.com
            </Typography>
            <br />
            <Typography sx={{fontSize : 15}}>Copyright© 2024 KT AIVLE SHCOOL TEAM2’ All rights reserved.</Typography>
          </Box>
        </div>
      </Box>

      {/* Service 모달 */}
      <Service open={isServiceModalOpen} onClose={closeServiceModal} />
      <PrivacyPolicy open={isPrivacyModalOpen} onClose={closePrivycyModal} />
    </>
  );
};

export default Footer;