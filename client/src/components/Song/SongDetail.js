import { useParams, Link, useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";

function SongDetail() {
	const [song, setSong] = useState({});
	const navigate = useNavigate(); // Initialize navigate

	const { id } = useParams();

	useEffect(() => {
		fetch(`http://127.0.0.1:5555/song/${id}`)
			.then(res => {
				if (res.ok) {
					return res.json();
				} else {
					throw new Error("Failed to fetch");
				}
			})
			.then(data => setSong(data))
			.catch(() => navigate("/not-found")); // Redirect to /not-found on error
	}, [id, navigate]); // Added navigate to dependency array

	const { name, length, lyrics, genre, release_dt, image, artist_id, all_songs = [] } = song;

	return (
		<div className="song-detail" id={id}>
			<h1>{name}</h1>
			<p>{genre}</p>
			<p>{release_dt}</p>

			<div className="song-card">
				<figure className="image">
					<img src={image} alt={name} />
					<section>
						<p>Genre: {genre}</p>
						<p>Length: {length}</p>
						<p>Release Date: {release_dt}</p>
						<p>Lyrics:</p>
						<pre>{lyrics}</pre> {/* Use <pre> to preserve formatting */}
					</section>
				</figure>
				<section className="details">
					<h3 style={{ margin: "16px auto" }}> Artist </h3>
					<ul className="artist">
						{all_songs.map(s => (
							<li key={s.id}>
								<img
									width={"100px"}
									src={s.image}
									alt={s.name}
								/>
								<div className="s-member">
									<Link to={`/artists/${artist_id}`}>
										<p style={{ fontStyle: "italic" }}>{artist_id.name}</p>
									</Link>
								</div>
							</li>
						))}
					</ul>
				</section>
			</div>
		</div>
	);
}

export default SongDetail;
