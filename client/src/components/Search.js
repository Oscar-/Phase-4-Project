import React, { useState } from "react";

//Search function
//Pass down cb as prop
function Search({ searchblank }) {
    const [from, setForm] = useState('');
}

//function for handle change
function handleChange(e) {
    setForm(e.target.value);
}

//function for handleSubmit
function handleSubmit(e) {
    e.preventDefault();
    searchblank(form);
}

// add onSubmit
  // add onChange event & value
  return (
    <div className="searchbar">
      <form onSubmit={(e) => handleSubmit(e)}>
        <label htmlFor="search">Search Songs, Artist, or Reviews:</label>
        <input
          type="text"
          id="search"
          placeholder="Type to search..."
          value={form.name}
          onChange={(e) => handleChange(e)}
        />
      </form>
    </div>
  );

export default Search;