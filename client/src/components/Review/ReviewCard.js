
import { Link } from "react-router-dom";


function ReviewCard({ review }) {
    const { id, content, rating, artist_id, song_id, user_id, created_at, updated_at } = review;

    return (
        <li className="card" id={id}>
            <figure className="review">
                <img src={image || "default-image.jpg"} /> 
            </figure>
            <section className="details">
                <Link to={`/review/${id}`}>
                    <h2>{rating}, {content}</h2>
                    <h2>{artist_id}, {song_id}</h2>
                </Link>
                <p>
                    {user_id}, {created_at}, {updated_at}
                </p>
            </section>
        </li>
    );
}

export default ReviewCard;