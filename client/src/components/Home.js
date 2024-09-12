import { useState, useEffect } from "react";
import About from "./About";

function Home() {
    const [songs, setSongs] = useState([]);
    const [error, setError] = useState(null); 

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
            setError(err.message); 
            console.error(err);
        });
    }, []);

    if (error) {
        return <div>Error: {error}</div>; 
    }

    return (
        <div>
            <section>
                <About />
            </section>
            
        </div>
    );
}

export default Home;
