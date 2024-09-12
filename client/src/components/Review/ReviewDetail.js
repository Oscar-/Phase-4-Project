import { useParams, Link, useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";


function ReviewDetail() {
    const [review, setReview] = useState({
        reviews: []
    });
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const params = useParams();
    const navigate = useNavigate();

    useEffect(() => {
        fetch(`http://127.0.0.1:5555/review/${params.id}`)
            .then(res => {
                if (!res.ok) {
                    throw new Error("Failed to fetch review");
                }
                return res.json();
            })
            .then(data => {
                setReview(data);
                setLoading(false);
            })
            .catch(() => {
                setError("Review not found");
                setLoading(false);

            });
    }, [params.id, navigate]);

    if (loading) {
        return <p>Loading...</p>;
    }

    if (error) {
        return <p>{error}</p>;
    }

    updated_at 
    const { id, content, rating, artist_id, song_id, user_id, created_at, updated_at } = review;

    return (
        <div className="review-detail" id={id}>
            <h1>{rating}</h1>
            <p>{content}</p>
            <div className="review-card">
                <figure className="image">
                    <img src={image || "default-image.jpg"} alt={name} /> {/* Fallback image */}
                    <section>
                        <p>Artist: {artist_id}</p>
                        <p>User: {user_id}</p>
                        <p>Song: {song_id}</p>
                        <p>Created: {created_at}</p>
                        <p>Updated: {updated_at}</p>
                    </section>
                </figure>
                <section className="details">
                    <h3>Reviews:</h3>
                    <ul className="songs">
                        {review.reviews.map((reviews) => (
                            <li key={review.id}>
                                <img
                                    width="100px"
                                    src={song.artist.image || "default-image.jpg"} // Fallback image
                                    alt={song.artist.name}
                                />
                                <div className="song-member">
                                    <Link to={`/review/${song.artist.id}`}>
                                        <p className="artist-name">{song.artist.name}</p>
                                    </Link>
                                    <p>{review.content}</p>
                                </div>
                            </li>
                        ))}
                    </ul>
                </section>
            </div>
        </div>
    );
}

export default ReviewDetail;
