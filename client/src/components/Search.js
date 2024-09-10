import React, { useState } from "react";

function Search({ searchArtist, searchSong }) {
    const [form, setForm] = useState('');

    // Function to handle input change
    const handleChange = (e) => {
        setForm(e.target.value);
    };

    // Function to handle form submission
    const handleSubmit = (e) => {
        e.preventDefault();
        if (form.trim()) {
            // Call the appropriate callback based on your requirements
            if (searchArtist) {
                searchArtist(form);
            }
            if (searchSong) {
                searchSong(form);
            }
        }
    };

    return (
        <div className="searchbar">
            <form onSubmit={handleSubmit}>
                <label htmlFor="search">Search Songs, Artists, or Reviews:</label>
                <input
                    type="text"
                    id="search"
                    placeholder="Type to search..."
                    value={form}
                    onChange={handleChange}
                />
                <button type="submit">Search</button>
            </form>
        </div>
    );
}

export default Search;
