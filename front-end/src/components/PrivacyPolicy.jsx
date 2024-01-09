import React from 'react'
import {Box, Typography } from "@mui/material/";
import Dialog from '@mui/material/Dialog';
import DialogTitle from '@mui/material/DialogTitle';
import DialogContent from '@mui/material/DialogContent';
import DialogActions from '@mui/material/DialogActions';
import Button from '@mui/material/Button';
import Accordion from '@mui/material/Accordion';
import AccordionSummary from '@mui/material/AccordionSummary';
import AccordionDetails from '@mui/material/AccordionDetails';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';


const PrivacyPolicy = ({open, onClose}) => {
  return (
    <Dialog open={open} onClose={onClose}>
      <DialogTitle>이용약관</DialogTitle>
      <DialogContent>
        <Accordion>
          <AccordionSummary
            expandIcon={<ExpandMoreIcon />}
            aria-controls="panel1a-content"
            id="panel1a-header2"
          >
            <Typography>개인정보 처리 방침</Typography>
          </AccordionSummary>
          <AccordionDetails>
            <Typography>주식회사 SAI(이하 “회사” 또는 “사이”라 함)는 이용자의 개인정보를 매우 중요하게 생각하며, 「개인정보 보호법」, 「정보통신망 이용 촉진 및 정보보호 등에 관한 법률」 등 관련 법령을 준수하여 이용자의 개인정보에 대한 권익을 보호하고 개인정보와 관련한 이용자의 고충을 원활하게 처리할 수 있도록 다음과 같이 개인정보 처리방침을 수립 및 공개합니다.</Typography>
            <br></br>
            <Typography>본 개인정보 처리방침은 이용자의 개인정보를 안전하게 보호하기 위한 회사의 정책을 알려드리기 위해 마련되었으며, 이용하고 계신 회사의 웹사이트에서 언제든 확인하실 수 있습니다.</Typography>
            <br></br>
            <Typography>회사는 개인정보보호와 관련한 법률 또는 지침의 변경, 회사 정책의 변경에 의해 본 개인정보 처리방침을 개정하는 경우 웹사이트에 게시하고 공지할 것입니다.</Typography>
            <br></br>
            <Typography> 제1조 (개인정보의 처리 목적)</Typography>
            <br></br>
            <Typography>1. 회사는 서비스 제공을 위하여 필요한 최소한의 개인정보를 수집하고 있으며 목적 이외의 용도로 개인정보를 이용하거나 제3자에게 제공하지 않습니다. 수집항목이나 수집∙이용 목적이 변경되는 경우에는 별도의 동의를 받는 등 필요한 조치를 이행할 것입니다.</Typography>
            <br></br>
            <Typography> 제2조 (개인정보의 수집 항목)</Typography>
            <br></br>
            <Typography>1. 회사의 서비스 이용자는 개인정보 수집과 이용 동의를 거부할 수 있습니다.</Typography>
            <br></br>
            <Typography>단, 필수 항목의 수집∙이용 동의를 거부할 경우, 회사 서비스 회원가입 및 이용이 불가합니다.</Typography>
            <br></br>
            <Typography>1. 마케팅 동의 등 선택 동의를 거부하여도 회사 서비스는 정상적으로 이용할 수 있습니다.</Typography>
            <Typography>2. 수집하는 개인정보 항목</Typography>
            <br></br>
            <Typography>| 구분 | 수집 항목 |</Typography>
            <br></br>
            <Typography>| 회원 가입 및 관리 | [필수] 이메일, 비밀번호, 닉네임, 성명, 휴대전화번호, 생년월일, 성별 |</Typography>
            <Typography>1. 서비스 이용과정에서 서비스 이용내역, 불량 이용 기록, 접속 로그, 쿠키, 접속IP 주소 등의 정보가 자동으로 생성되어 수집됩니다.</Typography>
            <Typography>2. 이용자의 개인정보는 아래 방법을 통해 수집합니다.</Typography>
            <br></br>
            <Typography>가. 이용자가 회사 서비스를 이용하면서 직접 입력</Typography>
            <br></br>
            <Typography>나. 그 밖에 서비스 이용 시 자동 생성되는 정보를 수집하는 경우</Typography>
            <br></br>
            <Typography> 제3조 (개인정보의 처리 및 보유기간)</Typography>
            <br></br>
            <Typography>1. 회사는 법령에 따른 개인정보 보유기간 또는 이용자로부터 개인정보를 수집 시에 동의 받은 보유기간 내에서 개인정보를 처리 및 보관합니다.</Typography>
            <br></br>
            <Typography>가. SAI 회원 가입 및 서비스 이용 : 회원 탈퇴 시까지</Typography>
            <br></br>
            <Typography>나. 부정 이용 기록(부정가입, 규정 위반 기록, 비정상적인 서비스 이용 기록) : 회원 탈퇴 시까지</Typography>
            <br></br>
            <Typography>다만 다음의 사유에 해당하는 경우에는 해당 사유 종료 시까지 보관 후 파기합니다.</Typography>
            <br></br>
            <Typography>가. 관계 법령 위반에 따른 수사/조사 등이 진행 중인 경우에는 해당 수사/조사 종료 시까지</Typography>
            <br></br>
            <Typography>나. 타 법령에 따라 보유가 필요한 경우에는 해당 기간 종료 시까지</Typography>
            <br></br>
            <Typography>| 「전자상거래 등에서의 소비자보호에 관한 법률」 | 계약 또는 청약철회 등에 관한 기록 | 5년 |</Typography>
            <Typography>|  | 소비자의 불만 또는 분쟁처리에 관한 기록 | 3년 |</Typography>
            <Typography>| 「통신비밀보호법」 | 로그인 기록(로그기록 자료, 접속자의 추적 자료) | 3개월 |</Typography>
            <Typography>1. 회사는 개인정보 보호법 제39조의6에 따라 마지막 로그인 후 1년의 기간 동안 로그인을하지 않은 이용자의 개인정보를 보호하기 위하여 해당 이용자의 개인정보를 별도로 저장 및 관리합니다. 회사는 위 유효기간 만료 30일 전까지 기간 만료일, 개인정보가 파기되는 사실, 해당 개인정보 항목을 문자 또는 이와 유사한 방법 중 어느 하나의 방법으로 이용자에게 알려드립니다. 명시한 기한 내에 로그인을 하지 않는 경우, 회사는 이용자의 회원자격을 상실시킬 수 있습니다.</Typography>
            <br></br>
            <Typography> 제4조 (개인정보의 제3자 제공)</Typography>
            <br></br>
            <Typography>1. 회사는 원칙적으로 이용자의 개인정보 처리목적으로 명시한 범위 내에서만 처리하며, 이용자의 별도의 사전 동의 없이는 범위를 초과하여 이용하거나 제3자에게 제공하지 않습니다.</Typography>
            <Typography>2. 회사는 다음 경우에 한하여 이용자의 동의 없이 개인정보를 제공할 수 있습니다.</Typography>
            <br></br>
            <Typography>가. 타 법령의 규정에 의거하거나, 수사, 조사목적으로 법령에 정해진 절차와 방법에 따라</Typography>
            <br></br>
            <Typography>수사기관 및 감독당국의 요구가 있는 경우</Typography>
            <br></br>
            <Typography>나. 기존 동의한 목적 또는 이용 범위 내에서 고객 정보의 정확성, 최신성을 유지하기 위한 경우</Typography>
            <br></br>
            <Typography>다. 서비스 제공 또는 요금 정산을 위해 필요한 경우</Typography>
            <br></br>
            <Typography>라. 이용자 또는 제3자의 급박한 생명, 신체, 재산의 이익을 위하여 필요함에도 불구하고 동의를 받을 수 없는 경우</Typography>
            <br></br>
            <Typography> 제5조 (개인정보 처리 위탁)</Typography>
            <br></br>
            <Typography>1. 회사는 원활한 업무처리를 위하여 다음과 같이 개인정보 처리업무를 외부에 위탁하고 있습니다.</Typography>
            <br></br>
            <Typography>| Amazon Web Services Inc. | 클라우드 서비스 | 회원탈퇴 및 위탁 계약 종료 시 |</Typography>
            <Typography>1. 회사는 관련 법령에 의거하여 수탁자를 정기적으로 감독하고 있습니다.</Typography>
            <Typography>2. 위탁업무의 내용이나 수탁자가 변경되는 경우 지체없이 본 개인정보처리방침을 통해 공개하겠습니다.</Typography>
            <br></br>
            <Typography> 제6조 (개인정보의 파기절차 및 파기 방법)</Typography>
            <br></br>
            <Typography>회사는 이용자의 개인정보 보유기간 경과, 처리 목적 달성 등 개인정보가 불필요하게 되거나 이용자의 요청이 있을 경우에 지체 없이 해당 개인정보를 복구 및 재생되지 않도록 파기합니다.</Typography>
            <br></br>
            <Typography>회사의 개인정보 파기절차 및 방법은 아래와 같습니다.</Typography>
            <br></br>
            <Typography>1. 파기절차</Typography>
            <br></br>
            <Typography>이용자의 개인정보가 관련 법령 또는 내부 방침에 의해 보존해야만 하는 경우 별도의 DB로 옮겨져(종이의 경우 별도의 서류함) 일정 기간 보관한 후 파기</Typography>
            <br></br>
            <Typography>1. 파기 방법</Typography>
            <br></br>
            <Typography>가. 종이에 출력된 개인정보는 분쇄기로 분쇄하거나 소각을 통하여 파기</Typography>
            <br></br>
            <Typography>나. 전자적 파일 형태로 저장된 개인정보는 기록을 재생할 수 없는 기술적 방법을 사용하여 삭제</Typography>
            <br></br>
            <Typography> 제7조 (개인정보의 안전성 확보조치)</Typography>
            <br></br>
            <Typography>회사는 이용자의 개인정보를 안전하게 관리하기 위하여 최선을 다하며 「개인정보 보호법」, 「정보통신망 이용 촉진 및 정보보호 등에 관한 법률」 등 관련 법령에서 요구하는 사항을 철저히 준수하고 있습니다. 회사의 과실로 개인정보의 도난, 분실, 변조, 유출 또는 훼손되는 경우 회사는 즉시 이용자에게 사실을 알리고 적절한 대책과 보상을 강구할 것입니다. 개인정보 보호를 위한 기술적, 관리적, 물리적 대책은 아래와 같습니다.</Typography>
            <br></br>
            <Typography>1. 기술적 대책</Typography>
            <br></br>
            <Typography>가. 개인정보에 대한 불법적인 접근을 차단하기 위한 침입차단시스템 및 침입탐지시스템의 설치 및 운영하고 있습니다.</Typography>
            <br></br>
            <Typography>나. 접속기록의 위조, 변조 방지를 위하여 다음과 같은 조치를 취하고 있습니다.</Typography>
            <br></br>
            <Typography>- 개인정보를 처리하는 직원이 이용자의 개인정보를 처리할 수 있도록 체계적으로 구성한 데이터베이스시스템(이하 “개인정보처리시스템”이라 함)에 접속하여 개인정보를 처리한 경우 접속일시, 처리내역 등의 저장 및 이의 확인, 감독</Typography>
            <Typography>- 개인정보처리시스템에 대한 접속기록을 별도 저장장치에 백업 보관</Typography>
            <br></br>
            <Typography>다. 개인정보를 안전하게 저장, 전송할 수 있는 암호화기술 등을 이용한 보안조치로 다음과 같은 조치 등을 취하고 있습니다.</Typography>
            <br></br>
            <Typography>- 비밀번호 및 중요 데이터 암호화 저장</Typography>
            <Typography>- 암호화 통신(SSL)으로 이용자의 개인정보 및 인증정보를 안전하게 전송하는 조치</Typography>
            <br></br>
            <Typography>라. 개인정보처리시스템 및 개인정보취급자가 개인정보 처리에 이용하는 정보기기에 컴퓨터 바이러스, 스파이웨어 등 악성프로그램의 침투 여부를 항시 점검, 치료할 수 있는 백신 소프트웨어를 설치하고 이를 주기적으로 갱신, 점검</Typography>
            <br></br>
            <Typography>마. 이용자의 개인정보를 처리하는 직원을 최소한으로 지정하여 운영하고 있습니다.</Typography>
            <br></br>
            <Typography>1. 관리적 대책</Typography>
            <br></br>
            <Typography>가. 개인정보의 안전한 관리 및 처리를 위한 개인정보 내부관리계획을 수립 및 시행하고 있습니다.</Typography>
            <br></br>
            <Typography>나. 개인정보처리시스템 비밀번호 생성 및 변경 주기 등의 기준 수립 및 운영하고 있습니다.</Typography>
            <br></br>
            <Typography>다. 개인정보처리시스템에 대한 접근권한의 부여, 변경, 말소 등에 관한 기준 수립 및 시행하고 있습니다.</Typography>
            <br></br>
            <Typography> 제8조 (개인정보 자동수집장치의 설치 운영 및 그 거부에 관한 사항)</Typography>
            <br></br>
            <Typography>회사는 이용자에게 개별적인 맞춤 서비스를 제공하기 위해 이용정보를 저장하고 수시로 불러오는 쿠키(cookie)와 세션(session)을 사용합니다.</Typography>
            <br></br>
            <Typography>1. “쿠키”는 앱 또는 웹사이트 서버가 이용자의 브라우저에 보내는 소량의 정보이며 이용자들 단말 기기에 저장됩니다.</Typography>
            <Typography>2. 이용자가 SAI 웹사이트에 접속한 경우 사이트에서 이용자의 기기에 저장되어 있는 쿠키 정보를 확인하여 이용자의 이용 형태, 보안접속 여부 등을 파악하여 이용자에게 최적화된 서비스 제공을 위해 사용됩니다.</Typography>
            <Typography>3. 이용자는 쿠키 설치 운영을 거부할 수 있으며, 저장을 원하지 않으시면 아래 설정 방법을 통해 쿠키 허용을 제한할 수 있습니다. 단, 쿠키 저장을 제한하는 경우 맞춤형 서비스 이용에 어려움이 발생할 수 있습니다.</Typography>
            <br></br>
            <Typography>| 크롬 | 상단 맞춤설정 및 제어 - 설정 - 개인정보 및 보안 -  쿠키 및 기타 사이트 데이터 |</Typography>
            <Typography>| --- | --- |</Typography>
            <Typography>| 사파리 | 환경설정 - 개인정보 보호 |</Typography>
            <Typography>| 엣지 | 상단 설정 및 기타 - 설정  - 쿠키 및 사이트 권한 |</Typography>
            <br></br>
            <Typography> 제9조 (개인정보보호 책임자 및 담당부서)</Typography>
            <br></br>
            <Typography>1. 회사는 이용자의 개인정보를 보호하고 개인정보와 관련한 고충 처리를 위하여 다음과 같이 개인정보보호 책임자를 지정하고 있습니다.</Typography>
            <br></br>
            <Typography>가. 개인정보보호 책임자(정보관리 보호인)</Typography>
            <br></br>
            <Typography>- 성명: 오진원(PM)</Typography>
            <Typography>- 소속: AIVLE SCHOOL</Typography>
            <Typography>- 이메일: a041174@aivle.kt.co.kr</Typography>
            <Typography>1. 이용자는 회사의 서비스(또는 사업)을 이용하시면서 발생한 모든 개인정보보호관련 문의, 불만처리, 열람청구, 피해구제 등에 관한 사항을 개인정보보호 책임자 및 담당부서로 문의할 수 있습니다. 회사는 이용자의 문의에 대하여 지체없이 답변 및 처리해드릴 것입니다.</Typography>
            <br></br>
            <Typography> 제10조 (이용자 및 법정대리인의 권리 의무 및 그 행사방법)</Typography>
            <br></br>
            <Typography>1. 이용자는 언제든지 자신의 개인정보 열람, 오류 등이 있을 경우 정정, 삭제, 처리 정지 등 개인정보 보호 관련 권리를 행사할 수 있습니다.</Typography>
            <br></br>
            <Typography>가. 개인정보 수정 : 홈페이지의 메뉴 - 내 정보 수정 - 수정</Typography>
            <br></br>
            <Typography>나. 회원 탈퇴 : 홈페이지의 메뉴 - 내 정보 수정 - 회원탈퇴</Typography>
            <br></br>
            <Typography>또한, 회사의 담당부서(정보보안팀)에게 이메일로 요청 시 지체 없이 조치를 취하겠습니다.</Typography>
            <br></br>
            <Typography>1. 회사는 만 14 세 미만 아동의 개인정보를 보호하기 위해 본 서비스의 회원가입을 제한하고 있습니다.</Typography>
            <Typography>2. 이용자는 개인정보를 최신의 상태로 정확하게 입력하여 불의의 사고를 예방해 주시기 바랍니다. 입력한 부정확한 정보로 인해 발생하는 사고의 책임은 이용자에게 있으며 타인 정보의 도용 등 허위정보를 입력할 경우 회원 자격이 상실될 수 있습니다.</Typography>
            <Typography>3. 회사는 타인의 ID 또는 기타 개인정보를 도용하여 회원가입 한 자 또는 서비스를 이용한 자를 발견할 경우 지체 없이 해당 아이디에 대한 서비스 이용 정지 또는 회원 탈퇴 등 필요한 조치를 취합니다.</Typography>
            <Typography>4. 회사는 이용자 개인의 실수나 기본적인 인터넷의 위험성 때문에 일어나는 일들에 대해서는 책임을 지지 않습니다. 이용자는 본인의 개인정보를 보호하기 위해 자신의 ID와 비밀번호를 적절하게 관리하고 이에 대한 책임을 져야 할 의무가 있습니다. 또한 다른 사람이 추측될 수 있는 쉬운 비밀번호는 사용을 피하시기를 권장하며, 정기적으로 비밀번호를 변경하는 것이 바람직합니다.</Typography>
            <br></br>
            <Typography> 제11조 (권익침해 구제방법)</Typography>
            <br></br>
            <Typography>이용자는 아래의 기관에 대해 개인정보 침해에 대한 피해 구제, 상담 등을 문의하실 수 있습니다. 개인정보 침해에 대한 신고나 상담이 필요한 경우에 아래 기관에 문의하시기 바랍니다.</Typography>
            <br></br>
            <Typography>가. 개인정보 분쟁 조정위원회 ([www.kopico.go.kr](https://www.kopico.go.kr/) / [1833-6972](tel:+82-1833-6972))</Typography>
            <br></br>
            <Typography>나. 개인정보 침해 신고센터 ([https://privacy.kisa.or.kr](https://privacy.kisa.or.kr/) / [118](tel:+82-118))</Typography>
            <br></br>
            <Typography>다. 대검찰청 사이버범죄수사단 ([www.spo.go.kr](https://www.spo.go.kr/) / [1301](tel:+82-1301))</Typography>
            <br></br>
            <Typography>라. 경찰청 사이버범죄 신고([https://ecrm.cyber.go.kr](https://ecrm.cyber.go.kr/) / [182](tel:+82-182))</Typography>
            <br></br>
            <Typography> 제12조 (본 개인정보처리방침 적용 범위)</Typography>
            <br></br>
            <Typography>회사는 이용자에게 서비스 제공을 위해서 다른 회사의 웹사이트 또는 자료에 대한 링크를 제공할 수 있습니다. 이 경우 회사는 외부사이트 및 자료에 대한 아무런 통제권이 없으므로 그로부터 제공받는 서비스나 자료의 유용성에 대해 책임질 수 없습니다.</Typography>
            <br></br>
            <Typography>회사가 포함하고 있는 링크를 클릭하여 타 웹사이트의 페이지로 옮겨갈 경우 해당 웹사이트의 개인정보보호 정책은 회사와 무관하므로 새로 방문함 웹사이트의 정책을 확인하시기 바랍니다.</Typography>
            <br></br>
            <Typography> 제13조 (개인정보처리방침의 변경에 관한 사항)</Typography>
            <br></br>
            <Typography>위 개인정보처리방침의 내용 추가, 삭제 및 수정이 있을 경우 사전에 게시판 등을 통해 고지할 것입니다.</Typography>
            <br></br>
            <Typography>공고 일자 : 2024.01.12</Typography>
            <br></br>
            <Typography>시행 일자 : 2024.01.12
            </Typography>
          </AccordionDetails>
        </Accordion>
        </DialogContent>
      <DialogActions>
        <Button onClick={onClose} color="primary">
          닫기
        </Button>
      </DialogActions>
    </Dialog>
  )
}

export default PrivacyPolicy