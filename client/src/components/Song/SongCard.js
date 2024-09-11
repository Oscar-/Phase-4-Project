import { Link } from "react-router-dom";

function SongCard({ song = {} }) {
	const { name, length, lyrics, genre, release_dt, image, id } = song;

	return (
		<li className="card" style={{maxWidth: "300px"}} id={id}>
			<figure className="image">
				<img src={image} alt={name} />
			</figure>
			<section className="details">
				<Link to={`/song/${id}`}>
					<h2>{name}</h2>
				</Link>
                <p>{genre}</p>
                <p>{length}</p>
                <p>{release_dt}</p>
				<p>{lyrics}</p>
			</section>
		</li>
	);
}

export default SongCard;