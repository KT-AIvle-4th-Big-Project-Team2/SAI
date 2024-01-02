const { createProxyMiddleware } = require("http-proxy-middleware");

module.exports = (app) => {
  app.use(
    createProxyMiddleware("/api/v1/refund", {
      target: "http://localhost:8000",
      changeOrigin: true,
    }),
  );
  app.use(
    createProxyMiddleware("/apis/v1/rental/modify", {
      target: "http://localhost:8000",
      changeOrigin: true,
    }),
  );
};