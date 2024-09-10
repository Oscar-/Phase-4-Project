import { useParams, Link } from "react-router-dom";
import { useEffect, useState } from "react";

function ArtistDetail() {
    const [artist, setArtist] = useState({
        discography: []
    });

    // 4a. fetch current production based on params
    // params.id
    const params = useParams();
    
    // 4c. if response is not ok, navigate to /not-found
    useEffect(() => {
        fetch(`http://127.0.0.1:5555/artists/${params.id}`)
            .then(res => {
                if (res.ok) {
                    return res.json();
                }
            })
            .then(data => setArtist(data))
            .catch(() => {
                // Handle fetch errors or navigate to /not-found
                // e.g., navigate("/not-found");
            });
    }, [params.id]);

    // 4b. destructure the values and display them on page
    const { id, name, gender, birth_date, birth_place, biography, image } = artist;

    return (
        <div className="project-detail" id={id}>
            <h1>{name}</h1>
            <p>{biography}</p>
            <div className="project-card">
                <figure className="image">
                    <img src={image} alt={name} />
                    <section>
                        <p>Gender: {gender}</p>
                        <p>Birth Date: {birth_date}</p>
                        <p>Birth Place: {birth_place}</p>
                    </section>
                </figure>
                <section className="details">
                    <h3 style={{ margin: "16px auto" }}>Discography:</h3>
                    <ul className="songs">
                        {artist.discography.map((song) => (
                            <li key={song.id}>
                                <img
                                    width="100px"
                                    src={song.artist.image}
                                    alt={song.artist.name}
                                />
                                <div className="song-member">
                                    <Link to={`/artists/${song.artist.id}`}>
                                        <p style={{ fontStyle: "italic" }}>{song.artist.name}</p>
                                    </Link>
                                    <p>{song.name}</p>
                                </div>
                            </li>
                        ))}
                    </ul>
                </section>
            </div>
        </div>
    );
}

export default ArtistDetail;