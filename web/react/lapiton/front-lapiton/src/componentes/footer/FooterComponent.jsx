import React from 'react';
import '../css/FooterComponent.css';
import { Link } from 'react-router-dom';
import Logo  from "../../assets/imagenLogoPiton.png"
function FooterComponent() {
  return (
    <footer>
      <nav>
        <Link to="#" className='nav-item'>Lo mas jugado</Link>
        <Link to="#" className='nav-item'>Lo mas nuevo</Link>
      </nav>
      <div className="iconos-social">
        <a href='#'><img width="50" height="50" src="https://img.icons8.com/ios-filled/50/meta.png" alt="meta"/></a>
        <a href='#'><img width="50" height="50" src="https://img.icons8.com/ios/50/instagram-new--v1.png" alt="instagram-new--v1"/></a>
        <a href='#'><img width="50" height="50" src="https://img.icons8.com/ios-filled/50/tiktok--v1.png" alt="tiktok--v1"/></a>
        <a href='#'><img width="50" height="50" src="https://img.icons8.com/ios/50/twitterx--v2.png" alt="twitterx--v2"/></a>
      </div>
      <div className="logo-footer">
        <p>laPiton</p>
        <img src={Logo} alt="logo" />
      </div>
    </footer>
  )
}

export default FooterComponent;