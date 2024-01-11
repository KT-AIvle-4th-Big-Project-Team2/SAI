import React, { useState, useEffect } from "react";
import { Header } from "./Index/header"
import { Features } from "./Index/features";
import { About } from "./Index/about";
import { Testimonials } from "./Index/testimonials";
import { About2 } from "./Index/about2";
import { About3 } from "./Index/about3";
import JsonData from "./data/data.json";
import SmoothScroll from "smooth-scroll";
import Footer from '../components/footer'
import "./Index.css"

// 스크롤 속도 지정
export const scroll = new SmoothScroll('a[href*="#"]', {
  speed: 1000,
  speedAsDuration: true,
});

const Index = () => {
  const [landingPageData, setLandingPageData] = useState({});
  useEffect(() => {
    setLandingPageData(JsonData);
  }, []);

  return (
    <div>
      <Header data={landingPageData.Header} />
      <Testimonials data={landingPageData.Testimonials} />
      <Features data={landingPageData.Features} />
      <About data={landingPageData.About} />
      <About2 data={landingPageData.About2} />
      <About3 data={landingPageData.About3} />
      <Footer />
    </div>
  );
};

export default Index;
