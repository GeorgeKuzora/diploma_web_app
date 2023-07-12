import React, { useState } from 'react';
import './style.css'

const Header = () => {
    const [query, setQuery] = useState("")
    const handleSearch = e => {  e.preventDefault()
        setQuery(e.target.value)
    }
    // const filteredJobs = jobs.filter(job => job.title.toLowerCase().includes(query.toLowerCase()))
    return (
        <div className="header">
            <div className="header_wrapper">
                <h1 className="header__title">
                    <strong>Welcome to Job Search!</strong>
                </h1>

                <form className="search_form" onSubmit={handleSearch}>
                    <input className="search-input"
                           type="text"
                           value={query}
                           onChange={e => setQuery(e.target.value)}
                           placeholder="Search for jobs"
                    />
                    <button className="search-button" type="submit">Search</button>
                </form>
            </div>

            {/*<ul> {filteredJobs.map(job => (*/}
            {/*    <li key={job.id}> {job.title} </li>*/}
            {/*))}*/}
            {/*</ul>*/}
        </div>
    );
};

export default Header;