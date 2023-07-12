import React, {useState} from 'react';
import styles from './FormValidation.module.css'
import {Button} from "react-bootstrap";

const FormValidation = () => {

    // Состояние для хранения введенных данных
    const [formData, setFormData] = useState({
        username:"",
        password:""
    });

    // Обработчики событий для полей формы
    function handleUsernameChange(event) {
        setFormData({...formData, username: event.target.value });
    }
    function handlePasswordChange(event) {
        setFormData({...formData, password: event.target.value});
    }

    // Функция для отправки формы
    const handleSubmit = event => {
        event.preventDefault();
    // Здесь можно выполнить какие-то действия после отправки формы
    };

    return (
        <form className={styles.formValidation} onSubmit={handleSubmit}>
        <div className={styles.formGroup}>
        <label className={styles.label} htmlFor="username">Username</label>
        <input
            type="text"
            className={styles.form__control}
            id="username"
            placeholder="Enter username"
            value={formData.username}
            onChange={handleUsernameChange}
        />
        </div>

        <div className={styles.formGroup}>
        <label className={styles.label} htmlFor="password">Password</label>
        <input
            type="password"
            className={styles.form__control}
            id="password"
            placeholder="Enter password"
            value={formData.password}
            onChange={handlePasswordChange}
        />
        </div>
            <Button type="submit">
                Login
            </Button>
        </form >
    );
};

export default FormValidation;