import React from "react";
import Layout from "../components/layout";
import Iframe from "react-iframe";

const StreamlitPage = () => (
  <Layout>
    {/* <h1>Daniel Cooke's Digital CV</h1> */}
    <Iframe
      url="https://luwah-cv.onrender.com"
      width="100%"
      height="800px"
      frameBorder="0"
    />
  </Layout>
);

export default StreamlitPage;
