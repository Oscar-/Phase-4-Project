import React, { useState } from "react";

function Search({ searchArtist, searchSong }) {
    const [form, setForm] = useState('');

    // Function to handle input change
    function handleChange(e) {
        setForm(e.target.value);
    }

    // Function to handle form submission
    function handleSubmit(e) {
        e.preventDefault();
        // Here you can choose which callback to call based on your requirements
        if (form.trim()) { // Check if input is not empty
            searchArtist(form); // Call searchArtist if that's what you need
            // searchSong(form); // Uncomment this if you want to call searchSong
        }
    }

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
                <button type="submit">Search</button> {/* Add a submit button */}
            </form>
        </div>
    );
}

export default Search;