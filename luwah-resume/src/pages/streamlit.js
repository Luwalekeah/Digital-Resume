// Place this content in src/pages/streamlit.js
import React from "react";
import Layout from "../components/layout";
import Iframe from "react-iframe";

const StreamlitPage = () => (
    <Layout>
        <Iframe
            url="/streamlit"
            width="100%"
            height="800px"
            frameBorder="0"
        />
    </Layout>
);

export default StreamlitPage;
