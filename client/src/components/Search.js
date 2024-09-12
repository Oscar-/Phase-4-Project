import React, { useState } from "react";

function Search({ searchArtist, searchSong }) {
    const [form, setForm] = useState('');

    
    const handleChange = (e) => {
        setForm(e.target.value);
    };

    
    const handleSubmit = (e) => {
        e.preventDefault();
        if (form.trim()) {
            
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
