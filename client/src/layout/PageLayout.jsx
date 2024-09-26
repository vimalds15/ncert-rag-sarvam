import React from "react";
import { Footer, Header, Input } from "../components";

const PageLayout = ({ children }) => {
  return (
    <>
      <Header />
      <div className="flex min-h-[calc(100vh-8rem)] pt-10  justify-center">
        <div className="w-[90%] max-w-4xl">{children}</div>
      </div>
      <Footer />
    </>
  );
};

export default PageLayout;
