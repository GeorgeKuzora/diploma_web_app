import React from 'react';
import {NavLink} from "react-router-dom"
import BtnDarkMode from "../btnDarkMode/BtnDarkMode";
import "./style.css";
import logo from "../../img/logo/logo.svg"

const Navbar = () => {

    const activeLink = 'nav-list__link nav-list__link--active'
    const normalLink = 'nav-list__link'

    return (
        <nav className="nav">
            <div className="container">
                <div className="nav-row">
                    <NavLink to="/" className="logo">
                        <img src={logo} alt="Логотип компании Jobs-Tops"/>
                        <h1>
                            <strong>Jobs</strong>
                            <p>Tops</p>
                        </h1>
                    </NavLink>

                    <BtnDarkMode />

                    <NavLink to="/" className={({isActive}) => isActive? activeLink : normalLink}>
                        Home
                    </NavLink>
                    <NavLink to="/projects" className={({isActive}) => isActive? activeLink : normalLink}>
                        Projects
                    </NavLink>
                    <NavLink to="/contacts" className={({isActive}) => isActive? activeLink : normalLink}>
                        Contacts
                    </NavLink>
                </div>
            </div>
        </nav>
    );
};

export default Navbar;