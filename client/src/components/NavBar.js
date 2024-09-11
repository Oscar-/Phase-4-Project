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
        <Link to="/artists"> All Artists </Link>
        </li>
        <li>
        <Link to="/songs"> All Songs </Link>
        </li>
        <li>
          <Link to="/artist/new">Add New Artist</Link>
        </li>
        <li>
          <Link to="/song/new">Add New Song</Link>
        </li>

      </ul>
    </nav>
  );
}

export default NavBar;
