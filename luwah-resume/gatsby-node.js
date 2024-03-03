const path = require("path");

exports.onCreateWebpackConfig = ({ actions }) => {
    actions.setWebpackConfig({
        resolve: {
            alias: {
                streamlit: path.resolve(__dirname, "src/pages/streamlit"),
            },
        },
    });
};
