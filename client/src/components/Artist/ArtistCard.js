import { Link } from "react-router-dom";

function ArtistCard({ artist, onDelete }) {
    const { id, name, gender, birth_date, birth_place, biography, image } = artist;

    // // Function to handle delete action
    // const handleDelete = () => {
    //     fetch(`http://127.0.0.1:5555/artist/${id}`, {
    //         method: 'DELETE',
    //     })
    //     .then(res => {
    //         if (res.ok) {
    //             // Call the onDelete function passed as a prop to update the UI
    //             onDelete(id);
    //         } else {
    //             throw new Error("Failed to delete artist");
    //         }
    //     })
    //     .catch(err => console.error(err)); // Error handling
    // };

    return (
        <li className="card" id={id}>
            <figure className="image">
                <img src={image || "default-image.jpg"} alt={name} /> {/* Fallback image */}
            </figure>
            <section className="details">
                <Link to={`/artists/${id}`}>
                    <h2>{name}</h2>
                </Link>
                <p>
                    {gender}, {birth_date}, {birth_place}
                </p>
                <p>{biography}</p> {/* Added separate paragraph for biography */}

                {/* Delete Button */}
                <button className="delete-btn" onClick={( ) => onDelete(artist.id)}>
                    Delete
                </button>
            </section>
        </li>
    );
}

export default ArtistCard;
