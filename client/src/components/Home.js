import { useState, useEffect } from "react";
import SongCard from "./Song/SongCard";


function Home() {

    //const [mostPlayedSongs, setMostPlayedSongs] = useState([])
    const [songs, setSongs] = useState([])

    useEffect(() => {
        // UPDATE FETCH REQUEST 
        fetch("http://127.0.0.1:5555/songs")
        .then(res => {
            if(res.ok) {
                return res.json()
            } else {
                // UPDATE FETCH REQUEST 
                console.error("fetch http://127.0.0.1:5555/songs went wrong")
            }
        })
        .then(data => setSongs(data))
    }, []) 

    return (
        <div>
            <section>
                <h2>Song Selection!</h2>
            </section>
            <ul
                style={{
                    display: "flex",
                    flexWrap: "wrap",
                    justifyContent: "center",
                }}
            >
                {songs.map((el) => (
                    <section style={{ display: "flex", flexDirection: "column" }}>
                        <h3>{el.length} minutes</h3>

                        <SongCard key={el.id} artist={el} />
                    </section>
                ))}
            </ul>

            <section>
            </section>
        </div>
    );

}




export default Home;