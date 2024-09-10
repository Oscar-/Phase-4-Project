import { useParams, Link, useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";

function SongDetail() {
	const [song, setSongs] = useState({
		discography: []
	});

	// 4a. fetch current production based on params
	// params.id
	const params = useParams()
	
	// 4c. if response is not ok, navigate to /not-found
	useEffect(() => {
		fetch(`http://127.0.0.1:5555/songs/${params.id}`)
		.then(res => {
			if(res.ok){
				return res.json()
			}
		})
		.then(data => setSongs(data))
	}, [])

	// 4b. destructure the values and display them on page
	const { id, name, length, lyrics, genre, release_dt, image } = song;
	
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
						<br>Lyrics: {lyrics}</br>
					</section>
				</figure>
				<section className="details">
					
					<h3 style={{ margin: "16px auto" }}>Cast: </h3>
					<ul className="crew">
						{song.roles.map((crew) => (
							<li>
								<img
									width={"100px"}
									src={crew.actor.image}
									alt={crew.actor.name}
								/>

								<div className="crew-member">
									<Link to={`/actors/${crew.actor.id}`}>
										<p style={{ "font-style": "italic" }}>{crew.actor.name}</p>
									</Link>
									<p>{crew.role_name}</p>
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