import React from 'react';
import "./modal.css"

const ModalRegistration = ({ active, setActive, children }) => {
    return (
        <div
            className={active ? "modal active" : "modal"}
            onClick={() => setActive(false)}
        >
            <div
                className={active ? "modal_content active" : "modal_content"}
                onClick={(e) => e.stopPropagation()}
            >
                {children}
            </div>
        </div>
    );
};

export default ModalRegistration;

// import React, { useState, useEffect } from "react";
// import { Modal, Form, Button} from "react-bootstrap"
//
// const ModalRegistration = () => {
//
//     const [show, setShow] = useState(false);
//     const onHide = () => setShow(false);
//
//     useEffect(() => {
//         // Выполняем какие-то инициализации при открытии модального окна
//     }, []);
//
//         // Обработчик отправки формы
//     const handleSubmit = (event) => {
//         event.preventDefault();
//
//         // Отправляем данные формы на сервер
//     };
//
//     return (
//         <div>
//             {/*Модальное окно*/}
//             <Modal show={show} onHide={onHide}>
//                 <Modal.Header closeButton>
//                     <Modal.Title>Регистрация</Modal.Title>
//                 </Modal.Header>
//                 <Modal.Body>
//                     {/ Форма регистрации */}
//                     <Form onSubmit={handleSubmit}>
//                         <input
//                             type="email"
//                             name="email"
//                             label="Email"
//                             placeholder="Введите email"
//                             />
//                         <br />
//                         <input type="password" name="password" label="Пароль" />
//                         <Button type="submit">Зарегистрироваться</Button>
//                 </Form>
//             </Modal.Body>
//         </Modal>
//         </div>
//     );
// };
//
// export default ModalRegistration;