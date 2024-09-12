import { useParams, Link, useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";

function ArtistDetail() {
    const [artist, setArtist] = useState({
        discography: []
    });
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [comment, setComment] = useState(""); // State for the new comment
    const [comments, setComments] = useState([]); // State for the list of comments
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

    const { id, name, gender, birth_date, birth_place, biography, image, songs } = artist;

    const handleCommentChange = (e) => {
        setComment(e.target.value);
    };

    const handleCommentSubmit = (e) => {
        e.preventDefault();
        if (comment.trim()) {
            setComments([...comments, comment]);
            setComment(""); // Clear the input field after submitting
        }
    };

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
                        {songs.map((song) => (
                            <li key={song.id}>
                                <img
                                    width="100px"
                                    src={song.image || "default-image.jpg"} // Fallback image
                                    alt={song.name}
                                />
                                <div className="song-member">
                                    <Link to={`/songs/${song.id}`}>
                                        <p className="artist-name">{song.name}</p>
                                    </Link>
                                </div>
                            </li>
                        ))}
                    </ul>
                </section>
            </div>

            <section className="comments">
                <h2>Submit your review!</h2>
                <form onSubmit={handleCommentSubmit}>
                    <textarea
                        value={comment}
                        onChange={handleCommentChange}
                        placeholder="Add a comment"
                        rows="4"
                        style={{ width: "100%" }}
                    />
                    <button type="submit">Submit</button>
                </form>
                <ul>
                    {comments.map((com, index) => (
                        <li key={index}>{com}</li>
                    ))}
                </ul>
            </section>
        </div>
    );
}

export default ArtistDetail;
