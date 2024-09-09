import { useState, useEffect } from "react";
import ArtistCard from "./artist/ArtistCard";


function Home() {

    const [mostPlayedSongs, setMostPlayedSongs] = useState([])

    useEffect(() => {
        // UPDATE FETCH REQUEST 
        fetch("http://127.0.0.1:5555/longest-movies")
        .then(res => {
            if(res.ok) {
                return res.json()
            } else {
                // UPDATE FETCH REQUEST 
                console.error("fetch http://127.0.0.1:5555/longest-movies went wrong")
            }
        })
        .then(data => setMostPlayedSongs(data))
    }, []) 

    return (
        <div>
            <section>
                <h2>Most Played</h2>
            </section>
            <ul
                style={{
                    display: "flex",
                    flexWrap: "wrap",
                    justifyContent: "center",
                }}
            >
                {mostPlayedSongs.map((el) => (
                    <section style={{ display: "flex", flexDirection: "column" }}>
                        <h3>{el.length} minutes</h3>

                        <ArtistCard key={el.id} artist={el} />
                    </section>
                ))}
            </ul>

            <section>
                <h2>Top 10</h2>
            </section>
        </div>
    );

}




export default Home;