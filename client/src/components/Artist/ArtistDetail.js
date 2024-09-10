import { useParams, Link, useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";


function ArtistDetail() {
    const [artist, setArtist] = useState({
        discography: []
    });
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const params = useParams();
    const navigate = useNavigate();

    useEffect(() => {
        fetch(`http://127.0.0.1:5555/artist/${params.id}`)
            .then(res => {
                if (!res.ok) {
                    throw new Error("Failed to fetch artist");
                }
                return res.json();
            })
            .then(data => {
                setArtist(data);
                setLoading(false);
            })
            .catch(() => {
                setError("Artist not found");
                setLoading(false);
                // Optionally navigate to a not-found page
                // navigate("/not-found");
            });
    }, [params.id, navigate]);

    if (loading) {
        return <p>Loading...</p>;
    }

    if (error) {
        return <p>{error}</p>;
    }

    const { id, name, gender, birth_date, birth_place, biography, image } = artist;

    return (
        <div className="artist-detail" id={id}>
            <h1>{name}</h1>
            <p>{biography}</p>
            <div className="artist-card">
                <figure className="image">
                    <img src={image || "default-image.jpg"} alt={name} /> {/* Fallback image */}
                    <section>
                        <p>Gender: {gender}</p>
                        <p>Birth Date: {birth_date}</p>
                        <p>Birth Place: {birth_place}</p>
                    </section>
                </figure>
                <section className="details">
                    <h3>Discography:</h3>
                    <ul className="songs">
                        {artist.discography.map((song) => (
                            <li key={song.id}>
                                <img
                                    width="100px"
                                    src={song.artist.image || "default-image.jpg"} // Fallback image
                                    alt={song.artist.name}
                                />
                                <div className="song-member">
                                    <Link to={`/artist/${song.artist.id}`}>
                                        <p className="artist-name">{song.artist.name}</p>
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
