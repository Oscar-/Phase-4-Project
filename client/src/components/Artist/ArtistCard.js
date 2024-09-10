import { Link } from "react-router-dom";


function ArtistCard({ artist }) {
    const { id, name, gender, birth_date, birth_place, biography, image } = artist;

    return (
        <li className="card" id={id}>
            <figure className="image">
                <img src={image || "default-image.jpg"} alt={name} /> {/* Fallback image */}
            </figure>
            <section className="details">
                <Link to={`/artist/${id}`}>
                    <h2>{name}</h2>
                </Link>
                <p>
                    {gender}, {birth_date}, {birth_place}
                </p>
                <p>{biography}</p> {/* Added separate paragraph for biography */}
            </section>
        </li>
    );
}

export default ArtistCard;
