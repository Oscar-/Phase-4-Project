import ArtistCard from "./ArtistCard";

function ArtistContainer({ artists, onDeleteArtist }) {
    return (
        <section>
            <ul className='cards'>
                {artists.map(artist => (
                    <ArtistCard 
                        key={artist.id} 
                        artist={artist} 
                        onDeleteArtist={onDeleteArtist} 
                    />
                ))}
            </ul>
        </section>
    );
}

export default ArtistContainer;
