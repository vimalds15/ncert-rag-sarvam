import React from "react";
import Logo from "../assets/ncert.png";

const Header = () => {
  return (
    <div className="flex items-center justify-center px-16 h-16 shadow-xl cursor-default">
      <img src={Logo} alt="logo" className="h-14" />
      <p className="text-lg text-zinc-600 font-bold">NCERT AI</p>
    </div>
  );
};

export default Header;
