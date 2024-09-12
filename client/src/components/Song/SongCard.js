import { Link } from "react-router-dom";

function SongCard({ song = {}, onDelete }) {
    const { name, length, lyrics, genre, release_dt, image, id } = song;

    // const handleDelete = () => {
    //     fetch(`http://127.0.0.1:5555/song/${id}`, {
    //         method: 'DELETE',
    //     })
    //     .then(res => {
    //         if (res.ok) {
    //             // Call the onDeleteSong function passed as a prop to update the UI
    //             onDeleteSong(id);
    //         } else {
    //             return res.json().then(data => {
    //                 throw new Error(data.error || 'Failed to delete song');
    //             });
    //         }
    //     })
    //     .catch(err => console.error(err)); // Error handling
    // };

    return (
        <li className="card" style={{maxWidth: "300px"}} id={id}>
            <figure className="image">
                <img src={image || "default-image.jpg"} alt={name} /> {/* Fallback image */}
            </figure>
            <section className="details">
                <Link to={`/songs/${id}`}>
                    <h2>{name}</h2>
                </Link>
                <p>{genre}</p>
                <p>{length}</p>
                <p>{release_dt}</p>
                <p>{lyrics}</p>

                {/* Delete Button */}
                <button className="delete-btn" onClick={( ) => onDelete(song.id)}>
                    Delete
                </button>
            </section>
        </li>
    );
}

export default SongCard;
