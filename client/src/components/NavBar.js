import React from "react";
import { Link } from "react-router-dom";


function NavBar() {
  return (
    <nav className="NavBar">
      <ul>
        <li>
          <Link to="/">Home</Link>
        </li>
        <li>
          <Link to="/artist/new">Add New Artist</Link>
        </li>
        {/* Optionally, you can add more links for artist and song details */}
        {/* <li>
          <Link to="/artist/1">Artist 1</Link>
        </li>
        <li>
          <Link to="/song/1">Song 1</Link>
        </li> */}
      </ul>
    </nav>
  );
}

export default NavBar;
