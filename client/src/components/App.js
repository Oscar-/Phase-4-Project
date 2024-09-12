import React, { useEffect, useState } from "react";
import { Route, Routes } from "react-router-dom";

import Home from "./Home";
import ArtistForm from "./Artist/ArtistForm";
import ArtistContainer from "./Artist/ArtistContainer";
import ArtistDetail from "./Artist/ArtistDetail";
import SongContainer from "./Song/SongContainer";
import SongForm from "./Song/SongForm";
import SongDetail from "./Song/SongDetail";

import NavBar from "./NavBar";
import Header from "./Header";

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



  const onDeleteArtist = (id) => {
    fetch(`http://127.0.0.1:5555/artist/${id}`, {
        method: 'DELETE',
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        } else {
            return response.json().then(data => {
                throw new Error(data.error || 'Failed to delete artist');
            });
        }
    })
    .then(data => {
        console.log(data.message)
        if (data.message === 'Artist deleted successfully') {
            setArtists(prevArtists => prevArtists.filter(artist => artist.id !== id));
        } else {
            console.error('Failed to delete artist:', data.error);
        }
    })
    .catch(error => console.error('Error:', error));
};

const onDeleteSong = (id) => {
    fetch(`http://127.0.0.1:5555/song/${id}`, {
        method: 'DELETE',
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        } else {
            return response.json().then(data => {
                throw new Error(data.error || 'Failed to delete song');
            });
        }
    })
    .then(data => {
        if (data.message === 'Song deleted successfully') {
            setSongs(prevSongs => prevSongs.filter(song => song.id !== id));
        } else {
            console.error('Failed to delete song:', data.error);
        }
    })
    .catch(error => console.error('Error:', error));
};

const addArtist = (artist) => setArtists((prev) => [...prev, artist]);
const addSong = (song) => setSongs((prev) => [...prev, song]);

  return (
    <div className="App light">
      <Header />
      <NavBar />
      <Routes>
        <Route path="/artist/new" element={<ArtistForm addArtist={addArtist} />} />
        <Route path="/artists" element={<ArtistContainer artists={artists} onDeleteArtist={onDeleteArtist} />} />
        <Route path="/artists/:id" element={<ArtistDetail />} />
        <Route path="/song/new" element={<SongForm addSong={addSong}/>} />
        <Route path="/songs" element={<SongContainer songs={songs} onDeleteSong={onDeleteSong}/>} />
        <Route path="/songs/:id" element={<SongDetail />} />
        <Route path="/" element={<Home />} />
      </Routes>
    </div>
  );
}

export default App;

