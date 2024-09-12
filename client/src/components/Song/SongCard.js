import { Link } from "react-router-dom";

function SongCard({ song = {}, onDelete }) {
    const { name, length, lyrics, genre, release_dt, image, id } = song;


    return (
        <li className="card" style={{maxWidth: "300px"}} id={id}>
            <figure className="image">
                <img src={image || "default-image.jpg"} /> 
            </figure>
            <section className="details">
                <Link to={`/songs/${id}`}>
                    <h2>{name}</h2>
                </Link>
                <p>{genre}</p>
                <p>{length}</p>
                <p>{release_dt}</p>
                <p>{lyrics}</p>

                <button className="delete-btn" onClick={( ) => onDelete(song.id)}>
                    Delete
                </button>
            </section>
        </li>
    );
}

export default SongCard;
