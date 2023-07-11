import React from 'react';
import Header from "../components/header/Header";

const Home = () => {
    return (
        <div>
            <Header />
            <main className="section">
                <div className="container">

                    <ul className="content-list">
                        <li className="content-list__item">
                            <h2 className="title-2">Useful Information</h2>
                            <p> Welcome to the home page of our job search site!
                                We are happy to welcome you and offer you a convenient and efficient way to find the right job.
                                On our page you will find many vacancies from different employers. We provide detailed information about each job posting,
                                including experience requirements, salary, location, and other important details.
                                We also offer a convenient keyword search so you can quickly find exactly what you're looking for.
                                Don't put off your job search until later! Use our site to find the perfect job today!
                            </p>
                        </li>
                        <li className="content-list__item">
                            <h2 className="title-2">About Us</h2>
                            <p>More</p>
                        </li>
                    </ul>

                </div>
            </main>
        </div>
    );
};

export default Home;