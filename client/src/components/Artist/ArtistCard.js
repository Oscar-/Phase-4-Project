import { Link } from "react-router-dom";

function ArtistCard({ artist }) {
    const { id, name, gender, birth_date, birth_place, biography, image } = artist;

    return (
        <li className="card" style={{ maxWidth: "300px" }} id={id}>
            <figure className="image">
                <img src={image} alt={name} />
            </figure>
            <section className="details">
                <Link to={`/artists/${id}`}>
                    <h2>{name}</h2>
                </Link>
                <p>
                    {gender}, {birth_date}, {birth_place}, {biography}
                </p>
            </section>
        </li>
    );
}

export default ArtistCard;