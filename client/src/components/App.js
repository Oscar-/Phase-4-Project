import React, { useEffect, useState } from "react";
import { Route, Routes } from "react-router-dom";
import Home from "./Home";
import ArtistForm from "./Artist/ArtistForm";
import ArtistContainer from "./Artist/ArtistContainer";
import SongContainer from "./Song/SongContainer";
import NavBar from "./NavBar"; // Import NavBar
import Header from "./Header"; // Import the Header component

function App() {
  const [songs, setSongs] = useState([]);
  const [artists, setArtists] = useState([]);

  useEffect(() => {
    // Fetch data from backend
    fetch("http://127.0.0.1:5555/song")
      .then((res) => res.ok ? res.json() : Promise.reject("Failed to fetch songs"))
      .then((data) => setSongs(data))
      .catch((error) => console.error(error));

    fetch("http://127.0.0.1:5555/artist")
      .then((res) => res.ok ? res.json() : Promise.reject("Failed to fetch artists"))
      .then((data) => setArtists(data))
      .catch((error) => console.error(error));
  }, []);

  const addArtist = (artist) => setArtists((prev) => [...prev, artist]);

  return (
    <div className="App light">
      <Header />
      <NavBar /> {/* Add NavBar here */}
      <Routes>
        <Route path="/artist/new" element={<ArtistForm addArtist={addArtist} />} />
        <Route path="/artist/:id" element={<ArtistContainer artists={artists} />} />
        <Route path="/song/:id" element={<SongContainer songs={songs} />} />
        <Route path="/" element={<Home />} />
      </Routes>
    </div>
  );
}

export default App;
