import { useState, useEffect } from "react";
import SongCard from "./Song/SongCard";
import About from "./About";

function Home() {
    const [songs, setSongs] = useState([]);
    const [error, setError] = useState(null); // Added state to handle errors

    useEffect(() => {
        fetch("http://127.0.0.1:5555/song")
        .then(res => {
            if (res.ok) {
                return res.json();
            } else {
                throw new Error("Failed to fetch songs");
            }
        })
        .then(data => {
            if (Array.isArray(data)) {
                setSongs(data);
            } else {
                throw new Error("Unexpected data format");
            }
        })
        .catch(err => {
            setError(err.message); // Set error message
            console.error(err);
        });
    }, []);

    if (error) {
        return <div>Error: {error}</div>; // Display error message if there's an error
    }

    return (
        <div>
            <section>
                <About />
            </section>
            {/* <ul
                style={{
                    display: "flex",
                    flexWrap: "wrap",
                    justifyContent: "center",
                }}
            >
                {songs.map((el) => (
                    <section
                        key={el.id}
                        style={{ display: "flex", flexDirection: "column" }}
                    >
                        <h3>{el.length} minutes</h3>
                        <SongCard artist={el} />
                    </section>
                ))}
            </ul> */}
            <section></section>
        </div>
    );
}

export default Home;
