import React, { useState, useEffect } from "react";
import { Header } from "./Index/header"
import { Features } from "./Index/features";
import { About } from "./Index/about";
import { Testimonials } from "./Index/testimonials";
import { Team } from "./Index/Team";
import { Contact } from "./Index/contact";
import { About2 } from "./Index/about2";
import { About3 } from "./Index/about3";
import JsonData from "./data/data.json";
import SmoothScroll from "smooth-scroll";
import "./Index.css"

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
      <Team data={landingPageData.Team} />
      <Contact data={landingPageData.Contact} />
    </div>
  );
};

export default Index;
