import React, { useEffect, useState } from "react";
import { Route, Routes } from "react-router-dom";
import Home from "./components/Home";
import ArtistForm from "./components/artist/ArtistForm";
import ArtistContainer from "./components/artist/ArtistContainer";
import ReviewContainer from "./components/review /ReviewContainer";
import SongContainer from "./components/song/SongContainer";
import NavBar from "./components/NavBar";

function App() {
  const [songs, setSongs] = useState([]);
  const [artists, setArtists] = useState([]);

  useEffect(() => {
    // Fetch songs with error handling
    fetch("http://127.0.0.1:5555/songs")
      .then((res) => {
        if (!res.ok) {
          throw new Error("Failed to fetch songs");
        }
        return res.json();
      })
      .then((data) => setSongs(data))
      .catch((error) => console.error(error.message));

    // Fetch artists with error handling
    fetch("http://127.0.0.1:5555/artists")
      .then((res) => {
        if (!res.ok) {
          throw new Error("Failed to fetch artists");
        }
        return res.json();
      })
      .then((data) => setArtists(data))
      .catch((error) => console.error(error.message));
  }, []);

  const addArtist = (artist) =>
    setArtists((current) => [...current, artist]);

  return (
    <div className="App light">
      <NavBar />
      <Routes>
        <Route
          path="/artists/new"
          element={<ArtistForm addArtist={addArtist} />}
        />
        <Route path="/artists/:id" element={<ArtistContainer artists={artists} />} />
        <Route path="/reviews/:id" element={<ReviewContainer />} />
        <Route path="/songs/:id" element={<SongContainer songs={songs} />} />
        <Route exact path="/" element={<Home />} />
      </Routes>
    </div>
  );
}

export default App;