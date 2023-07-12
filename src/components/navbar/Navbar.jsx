import React, {useState} from 'react';
import {NavLink} from "react-router-dom"
import BtnDarkMode from "../btnDarkMode/BtnDarkMode";
import "./style.css";
import logo from "../../img/logo/logo.svg";
import {Button} from "react-bootstrap";
import ModalRegistration from "./ModalRegistration";
import "./modalForm.css"

const Navbar = () => {

    const activeLink = 'nav-list__link nav-list__link--active'
    const normalLink = 'nav-list__link'


    // const [state, setState] = useState("");

    const [modalActive, setModalActive] = useState(false);


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

                    <Button className="open-btn" onClick={() => setModalActive(true)}>Регистрация</Button>

                    <NavLink to="/login" >
                        <Button variant="primary" onClick={() => setModalActive(false)}>Войти</Button>
                    </NavLink>

                </div>
            </div>
            <ModalRegistration active={modalActive} setActive={setModalActive}>
                <div className="container">
                    <div className="form">
                        <h1>Регистрация</h1>
                        <form>
                            <input
                                type="text"
                                required
                                placeholder="Имя"
                                id="name1"
                                className="input"
                            />
                            <input
                                type="text"
                                required
                                placeholder="Фамилия"
                                id="name2"
                                className="input"
                            />
                            <input
                                type="text"
                                required
                                placeholder="Отчество"
                                id="name3"
                                className="input"
                            />
                            <input
                                type="email"
                                required
                                placeholder="Почта"
                                id="email"
                                className="input"
                            />
                            <input
                                type="password"
                                required
                                placeholder="Пароль"
                                id="pass1"
                                className="input"
                            />
                            <input
                                type="password"
                                required
                                placeholder="Подтвердите пароль"
                                id="pass2"
                                className="input"
                            />
                            <input
                                type="number"
                                required
                                placeholder="Номер телефона"
                                id="tel"
                                className="input"
                            />
                            <button id="btn">Зарегистрироваться</button>
                            <p>Нажимая "Зарегистрироваться", вы подтверждаете, что прочитали и
                            согласны с нашими Условиями Пользования и Политикой
                                Конфиденциальности</p>
                        </form>
                    </div>
                </div>
            </ModalRegistration>
        </nav>
    );
};

export default Navbar;