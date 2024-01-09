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


const service = (open, onClose) => {
  return (
    <Dialog open={open} onClose={onClose} fullWidth maxWidth="md">
      <DialogTitle>이용약관</DialogTitle>
      <DialogContent>
        <Accordion>
          <AccordionSummary
            expandIcon={<ExpandMoreIcon />}
            aria-controls="panel1a-content"
            id="panel1a-header1"
          >
            <Typography>서비스 이용 약관</Typography>
          </AccordionSummary>
          <AccordionDetails>
            <Typography>제1장 총칙</Typography>
            <br></br>
            <Typography>제1조 목적</Typography>
            <br></br>
            <Typography>이 상권분석 서비스 이용약관(이하 ‘본 약관’)은 SAI(이하 ‘회사’)와 회사의 상권분석서비스를 이용하는 이용자 사이의 권리, 의무 및 책임사항 기타 필요한 사항을 규정함을 목적으로 합니다.</Typography>
            <br></br>
            <Typography>제2조 용어의 정의</Typography>
            <br></br>
            <Typography>1. 본 약관에서 사용하는 용어의 의미는 아래와 같습니다.</Typography>
            <Typography>2. ‘상권분석서비스’라 함은 신규창업, 점포확대 및 마케팅 기획을 목적으로 하는 개인 및 기업을 대상으로 상권 등을 체계적인 기법으로 파악하여, 그 분석정보를 솔루션 또는 서비스로 제공하는 유상 또는 무상의 서비스를 말합니다.</Typography>
            <Typography>3. ‘무상서비스’라 함은 상권분석서비스 중 회사가 별도의 금전적 대가를 받지 않고 제공하는 부분을 말합니다.</Typography>
            <Typography>4. ‘이용자’라 함은 본 약관에서 정의한 ‘회원’과 ‘비회원’을 말합니다.</Typography>
            <Typography>5. ‘회원’이라 함은 상권분석서비스에 자신의 정보를 회원등록을 한 개인 또는 기업으로서, 상권분석서비스를 계속적으로 이용할 수 있는 자를 말합니다.</Typography>
            <Typography>6. ‘아이디(ID)’라 함은 회원의 식별과 서비스 이용을 정하여 회원이 정하고, 회사가 승인하는 문자와 숫자의 조합을 말합니다.</Typography>
            <Typography>7. ‘비밀번호’라 함은 회원이 본인임을 확인하고, 회원에 대한 비밀보호를 정한 문자 또는 숫자의 조합을 말합니다.</Typography>
            <Typography>8. ‘해지(탈퇴)’라 함은 중앙회 또는 회원이 서비스 개통 후 이용계약을 해약하는 것</Typography>
            <Typography>9. 본 약관에서 사용하는 용어 중 본 약관에서 별도로 정하지 아니한 것은 관련 법령에서 정하는 바에 따르며, 그 외에는 일반적인 상관례에 따릅니다.</Typography>
            <br></br>
            <Typography>제3조 이용약관의 효력 및 약관변경 승인</Typography>
            <br></br>
            <Typography>1. 회사는 상권분석서비스 초기화면에 본 약관을 게시하고, 이용자가 본 약관의 중요한 내용을 확인할 수 있도록 합니다.</Typography>
            <Typography>2. 회사는 이용자가 본 약관의 내용에 대한 설명을 요청하는 경우 다음 각 호의 어느 하나의 방법으로 이용자에게 본 약관의 중요내용을 설명합니다.</Typography>
            <Typography>3. 약관의 중요내용을 이용자에게 직접 설명</Typography>
            <Typography>4. 약관의 중요내용에 대한 설명을 전자적 장치를 통하여 이용자가 알기 쉽게 표시하고 이용자로부터 해당 내용을 충분히 인지하였다는 의사표시를 전자적 장치를 통하여 수령</Typography>
            <Typography>5. 회사가 본 약관을 변경하고자 하는 경우에는 적용일자 및 변경사유를 명시하여 적용일자 7일 전부터 적용일자 전일까지 상권분석서비스 초기화면에 공지합니다. 다만, 회원에게 불리하거나 중요한 사항을 변경하는 경우에는 적용일자 30일 이전에 공지하고 회원에게 개별 통지합니다.</Typography>
            <Typography>6. 회사는 제3항의 공지 또는 통지를 할 경우 "회원이 변경에 동의하지 아니한 경우 공지된 날 또는 통지를 받은 날로부터 30일 이내에 계약을 해지할 수 있으며, 계약해지의 의사표시를 하지 아니한 경우에는 변경에 동의한 것으로 본다."라는 취지의 내용을 함께 공지하거나 통지합니다.</Typography>
            <Typography>7. 회원은 약관의 변경 내용이 게시되거나 통지가 발송된 날로부터 변경 약관의 적용일자 전까지 이용계약을 해지할 수 있고, 변경 약관의 적용일자 전까지 계약 해지의 의사표시를 하지 않은 경우에는 약관의 변경에 동의한 것으로 간주합니다.</Typography>
            <br></br>
            <Typography>제4조 서비스의 가입 및 이용계약의 성립</Typography>
            <br></br>
            <Typography>1. 자발적인 의사로 회원가입을 신청하고 상권분석서비스를 이용하는 회원 또는 본 약관에 동의하고 상권분석서비스를 이용하는 비회원의 경우, 본 약관에 동의한 것으로 봅니다.</Typography>
            <Typography>2. 회사는 제1항에 따라 본 약관에 동의한 회원 및 비회원에게 상권분석서비스를 제공합니다.</Typography>
            <Typography>3. 다음의 경우에는 임의적으로 회원가입 또는 상권분석서비스 이용을 인정하지 않거나 가입자격을 박탈할 수 있습니다.</Typography>
            <Typography>4. 회원가입 또는 상권분석서비스 이용 신청 시 해당정보가 허위로 기재되거나 타인의 정보인 경우</Typography>
            <Typography>5. 만 14세 미만의 자가 이용신청을 하는 경우</Typography>
            <Typography>6. 상권분석서비스를 이용함에 있어 부당한 방법으로 허용된 목적 범위 외의 행위를 하거나 할 위험이 있다고 판단되는 경우</Typography>
            <Typography>7. 부도덕한 행위로 회사와 상권분석서비스의 지위 또는 이미지를 손상시키거나 손상시킬 위험이 있다고 판단되는 경우</Typography>
            <Typography>8. 회사는 다음 각 호에 해당하는 경우 그 사유가 해소될 때까지 이용계약의 성립을 유보할 수 있습니다.</Typography>
            <Typography>9. 회사가 설비의 여유가 없는 경우</Typography>
            <Typography>10. 회사의 기술상 또는 지장이 있는 경우</Typography>
            <Typography>11. 기타 회사의 귀책 사유로 회원가입이나 상권분석서비스 이용 승낙이 곤란한 경우</Typography>
            <Typography>12. 회사는 제3항 및 제4항에 따라 회원가입이 거부되거나 회원가입을 유보하는 경우 이를 이용자에게 통지하여야 합니다.</Typography>
            <Typography>13. 회사는 본 약관이 정한 상권분석서비스 외에 추가적인 서비스를 제공하기 위해 이용자에게 별도의 추가적인 약관 동의, 정보 수집 및 이용 동의 등 절차의 이행을 요청할 수 있으며, 이러한 절차가 완료되지 않는 경우 해당 이용자가 추가적인 서비스의 전부 또는 일부를 이용하지 못할 수 있습니다.</Typography>
            <Typography>14. 이용자가 제6항에 따라 추가 서비스를 이용할 경우, 각 서비스 별로 추가되는 이용약관 또는 안내내용과 본 약관의 내용이 상이한 경우 본 약관보다 추가적으로 적용되는 개별 약관 또는 안내내용이 우선 적용됩니다.</Typography>
            <br></br>
            <Typography>제5조 서비스의 중단 및 변경</Typography>
            <br></br>
            <Typography>1. 회사는 일시적인 서비스 중단 사유가 발생하는 경우 해당 사유가 해소될 때까지 서비스 제공을 중단할 수 있고, 해당 사유가 소멸되는 경우 최대한 빠른 시간 내에 서비스 제공을 재개하도록 합니다.</Typography>
            <Typography>2. 회사는 관련 법규의 제∙개정, 정책변화, 행정기관의 처분 등 사유에 따라 상권분석서비스의 제공을 중단하거나 변경할 수 있습니다.
            <Typography>3. 회사는 제1항 또는 제2항에 따라 서비스의 이용을 중단 또는 변경하는 경우 그 사유와 내용을 회원에게 사전에 통지합니다. 다만, 회사가 사전에 통지할 수 없는 부득이한 사유가 있는 경우에는 사후에 알릴 수 있으며, 비회원에게는 통지를 생략합니다.</Typography>
            <br></br>
            <Typography>제6조 서비스의 해지 및 제한 등</Typography>
            <br></br>
            <Typography>1. 회원은 언제든지 상권분석서비스 이용계약 해지신청을 할 수 있으며, 회사는 관련 법령 등이 정하는 바에 따라 이를 즉시 처리합니다.</Typography>
            <Typography>2. 회원이 상권분석서비스를 해지할 경우, 회사는 관련 법령 및 개인정보처리방침에 따라 회사가 이용자 정보를 보유하는 경우를 제외하고는 해지 즉시 이용자의 모든 데이터를 소멸하여야 합니다.</Typography>
            <Typography>3. 회사는 다음 각 호의 어느 하나의 경우에는 이용계약을 해지하거나 이용자의 상권분석서비스 이용을 제한 또는 중단할 수 있습니다.</Typography>
            <Typography>4. 제4조 제3항 각 호 중 하나에 해당하는 경우</Typography>
            <Typography>5. 이용자가 서비스의 운영을 고의로 방해하거나 시도하는 경우</Typography>
            <Typography>6. 회사가 제공하는 서비스 이용방법에 의하지 아니하고 비정상적인 방법으로 서비스를 이용하거나 회사의 시스템에 접근하는 행위를 한 경우</Typography>
            <Typography>7. 본 약관을 위반하거나, 회사 또는 다른 이용자의 정당한 이익을 침해하거나 법령에 위배되는 행위를 한 경우</Typography>
            <Typography>8. 이용자가 법령 또는 선량한 풍속 기타 사회질서에 위배되는 행위를 한 경우</Typography>
            <Typography>9. 중대한 사정변경으로 인하여 이용자에게 계속하여 서비스를 제공하는 것이 불가능하거나 곤란한 경우</Typography>
            <Typography>10. 회사가 이용계약을 해지하거나 서비스의 이용을 제한 또는 중단하는 경우 회사는 이용자에게 사전 통지하며, 이용자는 이의를 신청할 수 있습니다. 다만, 회사가 긴급하게 이용계약을 해지하거나 서비스 이용을 제한할 필요성이 있는 경우에는 사후에 통지할 수 있습니다.</Typography>
            <Typography>11. 이용자가 본 조의 금지행위를 하는 경우 상권분석서비스 이용을 제한함과 별도로 손해배상의 청구, 사법당국에 대한 고발 등 법적 조치를 취할 수 있으며, 필요한 경우 이용계약의 임의 해지를 일정 기간 제한할 수 있습니다.</Typography>
            <br></br>
            <Typography>제7조 저작권 등 권리의 귀속</Typography>
            <br></br>
            <Typography>1. 상권분석서비스와 관련된 일체의 지식재산권(서비스 화면, 편집저작물 및 데이터베이스 등을 말하며, 이에 한정되지 아니함. 이하 ‘SAI지식재산권’)은 회사에 귀속됩니다. 단, 이용자의 게시물은 제외합니다.</Typography>
            <Typography>2. 회사는 게시된 내용을 사전 통지 없이 편집, 이동시킬 수 있으며, 다음의 경우 사전 통지 없이 삭제할 수 있습니다.</Typography>
            <Typography>3. 본 약관에 저촉되는 경우</Typography>
            <Typography>4. 타인의 지식재산권을 침해하는 내용인 경우</Typography>
            <Typography>5. 타인을 비방하거나 명예를 훼손하는 내용인 경우</Typography>
            <Typography>6. 공공질서를 해칠 우려가 있는 내용인 경우</Typography>
            <Typography>7. 탈퇴한 회원이 등록한 게시물인 경우</Typography>
            <Typography>8. 기타 관계 법령에 위배되는 경우</Typography>
            <Typography>9. 이용자는 SAI 지식재산권 등 상권분석서비스를 이용하여 얻은 정보를 이용자 본인의 상권분석 외의 용도로 사용하거나 제3자에게 이용하게 할 수 없습니다. 단, 이용의 범위를 정하여 회사의 사전 동의를 받은 경우 및 법령상 허용되는 경우는 예외로 합니다.</Typography>
            <Typography>10. 이용자가 상권분석서비스를 통하여 취득한 정보를 활용하는 경우(제3항 단서의 경우를 포함함), 제5항에 따른 방법으로 출처를 명시하여야 합니다.</Typography>
            <Typography>11. 출처를 명시할 때에는 서비스명(‘SAI’ 등) 및 접속경로(www.SAI.com)를 필수로 표기하여야 하며, 표시상의 제한사항이 없는 한 참조일자(연/월/일)를 함께 표시하는 것을 원칙으로 합니다.</Typography>
            <br></br>
            <Typography>제7조의2 저작권 등의 예외적 이용허락</Typography>
            <br></br>
            <Typography>제7조 제3항에도 불구하고, SAI 지식재산권은 아래 각 호의 조건을 모두 충족하는 경우 이용자 본인의 상권분석 외의 용도로 이용이 허락됩니다.</Typography>
            <br></br>
            <Typography>1. 이용자는 SAI 지식재산권을 불특정 다수를 대상으로 제공되는 서비스에는 활용할 수 있으나, 개별 고객에게 제공되는 서비스에는 활용할 수 없습니다.</Typography>
            <Typography>2. 이용자는 SAI 지식재산권 활용시 내용, 형식 및 제호의 동일성을 변경하여서는 안 됩니다. 구체적으로는, 상권분석서비스 화면을 캡쳐 또는 녹화 등의 방식으로 제공하는 경우 수치 및 결과에 대한 변경 또는 변형이 있어서는 안 되며, 상권분석서비스의 분석내용을 인용하는 경우 관련 수치 및 내용의 본질적 부분에 있어서의 차이가 발생하면 안 됩니다.</Typography>
            <Typography>3. 제2호에도 불구하고, SAI 지식재산권의 본질적인 내용을 변경하지 않는 범위 내에서 SAI에게 그 사실을 사전에 고지한 후 사소한 수정 및 편집을 하는 것은 허용됩니다.</Typography>
            <Typography>4. 이용자가 SAI 지식재산권 및 그에 따라 제작된 편집저작물 및 2차적 저작물을 복제, 배포, 공중송신 등 이용하는 경우, 이용자는 제7조 제5항의 방법[서비스명(‘SAI’) 및 접속경로() 표시 등]으로 출처를 명시하여야 합니다.</Typography> 
            <br></br>
            <Typography>   [www.SAI.com](http://www.sai.com/)</Typography>
            <br></br>
            <br></br>
            <Typography>제8조 이용자의 의무</Typography>
            <br></br>
            <Typography>1. 이용자는 아래 각 호에 해당하는 행위를 하여서는 안 됩니다.</Typography>
            <Typography>2. 본 약관 및 전자상거래법 등 상권분석서비스 이용에 관련된 관계법령을 위반하는 행위</Typography>
            <Typography>3. 서비스를 제공받기 위해 이용 신청 또는 변경 신청 시 허위 사실을 기재하거나 타인의 정보를 도용하는 등 정상적인 서비스 운영을 고의로 방해하는 일체의 행위</Typography>
            <Typography>4. 여하 한 방법으로 회사가 정상적으로 제공하는 방법이 아닌 다른 방법으로 회사가 보유하고 있는 정보를 탈취, 저장, 공개 또는 부정한 목적으로 사용하는 행위</Typography>
            <Typography>5. 회사의 또는 제3자의 지식재산권 등 기타 권리를 침해하거나, 회사의 동의 없이 회원 또는 제3자의 상업적인 목적을 위하여 본 서비스 구성요소의 전부 또는 일부의 내용에 관하여 이를 복사, 복제, 판매, 재판매 또는 양수도하는 행위 (단, 제7조 및 제7조의2에 따라 허용되는 경우는 제외함)</Typography>
            <Typography>6. 기타 범죄 또는 법령이 금지하는 행위와 관련되었다고 의심받을 수 있는 일체의 행위</Typography>
            <Typography>7. 회사가 게시한 정보를 변경하는 행위</Typography>
            <Typography>8. 「정보통신망 이용촉진 및 정보보호 등에 관한 법률」 등 관련 법령에 의하여 그 전송 또는 게시가 금지되는 정보(컴퓨터 프로그램 등)를 전송하거나 게시하는 행위</Typography>
            <Typography>9. 회사 및 기타 제3자의 명예를 손상시키거나 업무를 방해하는 행위</Typography>
            <Typography>10. 서비스와 관련된 설비의 오동작이나 정보 등의 파괴 및 혼란을 유발시키는 컴퓨터 바이러스 감염 자료를 등록 또는 유포하는 행위</Typography>
            <Typography>11. 회사의 서비스를 해킹하거나 해킹에 이용하는 일체의 행위</Typography>
            <Typography>12. 기타 불법적이거나 부당한 행위</Typography>
            <Typography>13. 이용자는 상권분석서비스 이용시 다음의 사항을 준수하여야 합니다.</Typography>
            <Typography>14. 이용자는 상권분석, 시장조사 등 상업적·비상업적 통계·연구의 목적(상권분석, 시장조사 등)으로 이용합니다.</Typography>
            <Typography>15. 이용자는 상권분석서비스를 특정 개인을 식별하기 위한 목적 및 방식(특정 개인의 정보를 확인하기 위하여 SAI 상권분석서비스를 통해 취득하는 정보를 다른 정보와 결합하는 행위 등)으로 활용하지 않습니다.</Typography>
            <Typography>16. 이용자는 상권분석서비스를 활용하여 특정 개인을 식별할 만한 정보를 보유하지 않습니다.</Typography>
            <Typography>17. 이용자는 특정 개인에게 경제적, 비경제적 손해를 발생시킬 우려가 있는 방식으로 상권분석서비스를 이용하지 않습니다.</Typography>
            <Typography>18. 만일 이용자가 상권분석서비스 이용 과정에서 제3호에 따른 식별가능성, 제4호에 따른 손해 발생 가능성을 인지하게 된 경우, 이용자는 즉시 서비스 이용을 중단하고 관련 정보를 파기합니다.</Typography>
            <Typography>19. 이용자는 관계법령, 본 약관의 규정, 서비스와 관련하여 공지한 주의사항, 회사가 통지하는 사항 등을 준수하여야 합니다.</Typography>
            <br></br>
            <Typography>제8조의2 면책</Typography>
            <br></br>
            <Typography>회사는 아래 각 호의 경우에 대하여 책임을 지지 않습니다.</Typography>
            <br></br>
            <Typography>1. 이용자가 본인의 개인정보 및 접속정보(ID, 비밀번호 등)에 대한 관리소홀 등에 의한 손해가 발생할 경우</Typography>
            <Typography>2. 전쟁, 천재지변 등 불가항력적인 사유로 상권분석서비스를 제공하지 못하는 경우</Typography>
            <Typography>3. 통신기기, 통신회선 또는 회사가 직접 통제할 수 없는 장애에 의한 업무처리 지연이나 불능이 발생한 경우</Typography>
            <Typography>4. 이용자가 바이러스 침투, 불법 소프트웨어 설치 등 컴퓨터 관리소홀 및 부주의, 키보드 보안을 포함한 회사의 보안프로그램 미설치로 본인의 정보 등이 노출되어 손해가 발생한 경우</Typography>
            <Typography>5. 이용자가 제8조를 준수하지 않아 손해가 발생한 경우</Typography>
            <Typography>6. 이용자의 동의를 얻어 제3자에게 제공한 정보가 제3자에 의해 누출이 된 경우</Typography>
            <Typography>7. 회사는 이용자 또는 기타 제휴사가 제공하는 서비스의 내용상의 완전성 및 질에 대하여 보장하지 않습니다. 따라서 회사는 이용자가 위 내용을 이용함으로 인하여 입게 된 모든 종류의 손실이나 손해에 대하여 책임을 부담하지 아니합니다.</Typography>
            <Typography>8. 기타 회사의 과실로 인하여 발생한 사고가 아닌 경우</Typography>
            <br></br>
            <Typography>제9조 개인(신용)정보 보호 및 처리</Typography>
            <br></br>
            <Typography>1. 회사는 관련 법령이 정하는 바에 따라 회원의 개인(신용)정보를 보호하기 위해 노력합니다.</Typography>
            <Typography>2. 회사는 회원의 개인(신용)정보를 처리하기 위해 사전에 처리목적, 제공목적 등을 명시하며, 회원의 동의없이 처리, 제공 또는 목적 외로 활용하지 않습니다. 다만, 다음의 경우에는 예외로 합니다.</Typography>
            <Typography>3. 법령에서 개인(신용)정보의 이용과 제3자 제공을 허용하고 있는 경우</Typography>
            <Typography>4. 회원임을 확인할 수 없도록 가명처리 후 통계 작성, 과학적 연구, 공익적 기록보존 등의 목적으로 활용하는 경우</Typography>
            <Typography>5. 회원이 동의하는 경우 회사는 회원의 개인(신용)정보를 회사의 다른 업무에 이용하거나 제휴 서비스 제공기관 등 제3자에게 제공할 수 있습니다.</Typography>
            <Typography>6. 회사는 회원에게 필요하다고 생각되는 유용한 정보(광고를 포함)를 제9조의 방법으로 제공할 수 있습니다. 회원은 해당 정보의 수신을 거부할 수 있습니다.</Typography>
            <Typography>7. 회사의 개인(신용)정보의 보호 및 이용에 대한 사항은 회사의 개인정보처리방침을 통해 안내드립니다.</Typography>
            <br></br>
            <Typography>제10조 위치정보의 보호 및 이용</Typography>
            <br></br>
            <Typography>1. 회사는 서비스의 제공과 관련하여, 위치정보 서비스에 관한 약관 및 정보 제공 동의 등 필요한 요건을 구비한 회원으로부터 위치정보를 수집 및 이용할 수 있습니다.</Typography>
            <Typography>2. 회사는 회원의 위치 정보를 이용하는 경우, 위치정보의 보호 및 이용 등에 관한 법률 등 관련 법령이 정하는 바에 따라서 회원의 개인위치정보를 보호하기 위하여 노력합니다.</Typography>
            <Typography>3. 위치정보의 수집 및 이용에 관하여는 회사가 제시하는 별도의 약관에 정한 바에 따릅니다.
            <br></br>
            <Typography>제11조 맞춤형 광고 안내</Typography>
            <br></br>
            <Typography>1. 회사는 회원에게 유용한 정보를 안내하기 위해 맞춤형 광고를 제공할 수 있으며, 맞춤형 광고를 위해 최소한의 정보만 수집·처리합니다.</Typography>
            <Typography>2. 회사는 회원에게 적절한 맞춤형 광고를 제공하기 위해 다음 정보를 수집·처리할 수 있습니다.</Typography>
            <Typography>3. 광고 식별정보(ADID)</Typography>
            <Typography>4. 상권분석서비스 방문기록 또는 활동기록</Typography>
            <Typography>5. 기타 상권분석서비스 이용에 대한 행태정보</Typography>
            <Typography>6. 맞춤형 광고를 위해 수집한 정보는 제3자에게 제공하거나, 다른 정보와 결합하여 사용하지 않으며, 일반 개인(신용)정보와 동일한 보안 기준을 가지고 안전하게 관리합니다.</Typography>
            <Typography>7. 회사는 맞춤형 광고에 대해 만 14세 미만을 회원의 정보를 일체 처리하지 않고, 광고를 제공하지 않습니다.</Typography>
            <br></br>
            <Typography>제12조 게시물 등에 관한 관리</Typography>
            <br></br>
            <Typography>1. 회사는 상권분석서비스에 청소년유해매체물 등이 게재/광고되어 있는 경우 지체 없이 그 내용을 삭제합니다.</Typography>
            <Typography>2. 이용자가 상권분석서비스 이용 과정에서 게시한 게시물 등이 타인의 사생활을 침해하거나 명예를 훼손하는 등 권리를 침해하는 경우, 그 침해받은 자는 회사에 해당 게시물 등의 게시중단 및 삭제 등을 요청할 수 있으며, 회사는 「정보통신망 이용촉진 및 정보보호 등에 관한 법률」 및 「저작권법」 등 관련 법령 및 회사의 정책에 따라 조치를 취합니다.
            <Typography>3. 제2항에서 정하는 임시조치의 세부 절차는 관련 법령규정의 목적범위 내에서 회사가 별도로 정하는 절차에 따릅니다.</Typography>
            <br></br>
            <Typography>제13조 분쟁처리 및 분쟁조정</Typography>
            <br></br>
            <Typography>1. 이용자는 회사의 고객센터를 통하여 상권분석서비스와 관련한 의견 및 불만의 제기 등의 분쟁처리를 요구할 수 있습니다.</Typography>
            <br></br>
            <Typography>고객센터(인터넷접수) : a041174@aivle.kt.co.kr</Typography>
            <br></br>
            <Typography>1. 이용자가 회사에 대하여 분쟁처리를 신청한 경우에는 회사는 영업일 기준 15일 이내에 이에 대한 조사 또는 처리 결과를 이용자에게 안내합니다.</Typography>
            <br></br>
            <Typography>제14조 약관의 해석</Typography>
            <br></br>
            <Typography>1. 회사와 이용자 사이에 개별적으로 합의한 사항이 본 약관에 정한 사항과 다를 때에는, 그 합의사항을 본 약관에 우선하여 적용합니다.</Typography>
            <Typography>2. 본 약관의 내용 중 관련 법령의 강행규정과 배치되는 부분이 있는 경우, 그 부분에 한하여 본 약관의 해당 규정은 무효로 합니다.</Typography>
            <br></br>
            <Typography>제15조 준용규정</Typography>
            <br></br>
            <Typography>1. 회사는 개별 서비스에 적용될 사항의 규정을 위해 개별약관을 사용하거나 이용정책을 구분하여 운영할 수 있으며, 본 약관에서 정한 내용이 다른 약관과 충돌하는 경우 상권분석서비스에 관하여는 본 약관이 우선합니다.</Typography>
            <Typography>2. 본 약관에서 정하지 아니한 사항에 대해서는 「SAI 서비스 이용 약관」 및 기타 회사의 개별 서비스 약관, 「신용정보의 이용 및 보호에 관한 법률」, 「전자금융거래법」, 「약관의 규제에 관한 법률」, 「정보통신망 이용촉진 및 정보보호 등에 관한 법률」, 「콘텐츠산업진흥법」, 「콘텐츠이용자보호지침」 등 관련 법령 및 상관습 등에 따릅니다.</Typography>
            <br></br>
            <Typography>제16조 재판권 및 준거법</Typography>
            <br></br>
            <Typography></Typography>본 약관은 대한민국 법률에 따라 규율되고 해석되며, 회사와 이용자 간에 발생한 분쟁으로 소송이 제기되는 경우 해당 분쟁의 해결은 민사소송법에 따라 관할을 가지는 법원의 판결에 따르기로 합니다.</Typography>
            <br></br>
            <Typography></Typography>공고 일자 : 2024.01.12</Typography>
            <br></br>
            <Typography></Typography>시행 일자 : 2024.01.12</Typography>
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

export default service