import React from 'react'
import { Container } from 'react-bootstrap'
import KakaoMap from './KakaoMap'

const Home = () => {
  return (
    <Container fluid style={{ padding: 0 }}>
      <h1>Home </h1>
      <KakaoMap></KakaoMap>
    </Container>
  )
}

export default Home