import React from 'react'
import Accordion from 'react-bootstrap/Accordion';
import Box from '@mui/material/Box';

const FAQ = () => {
  return (
    <>
    <Box sx = {{mt : 3, mb : 5 }}><h2>자주 묻는 질문</h2></Box>
    <Accordion>
      <Accordion.Item eventKey="0">
        <Accordion.Header>FAQ #1</Accordion.Header>
        <Accordion.Body>
          FAQ 답변 #1
        </Accordion.Body>
      </Accordion.Item>
      <Accordion.Item eventKey="1">
        <Accordion.Header>FAQ #2</Accordion.Header>
        <Accordion.Body>
          FAQ 답변 #2
        </Accordion.Body>
      </Accordion.Item>
      <Accordion.Item eventKey="2">
        <Accordion.Header>FAQ #3</Accordion.Header>
        <Accordion.Body>
          FAQ 답변 #3
        </Accordion.Body>
      </Accordion.Item>
      <Accordion.Item eventKey="3">
        <Accordion.Header>FAQ #4</Accordion.Header>
        <Accordion.Body>
          FAQ 답변 #4
        </Accordion.Body>
      </Accordion.Item>
      <Accordion.Item eventKey="4">
        <Accordion.Header>FAQ #5</Accordion.Header>
        <Accordion.Body>
          FAQ 답변 #5
        </Accordion.Body>
      </Accordion.Item>
    </Accordion>
    </>
  )
}

export default FAQ