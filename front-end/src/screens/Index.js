import React, { useState, useEffect } from "react";
import { Header } from "./Index/header"
import { Features } from "./Index/features";
import { About } from "./Index/about";
import { Services } from "./Index/services";
import { Gallery } from "./Index/gallery";
import { Testimonials } from "./Index/testimonials";
import { Team } from "./Index/Team";
import { Contact } from "./Index/contact";
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
      <Features data={landingPageData.Features} />
      <About data={landingPageData.About} />
      <Services data={landingPageData.Services} />
      <Gallery data={landingPageData.Gallery} />
      <Testimonials data={landingPageData.Testimonials} />
      <Team data={landingPageData.Team} />
      <Contact data={landingPageData.Contact} />
    </div>
  );
};

export default Index;
