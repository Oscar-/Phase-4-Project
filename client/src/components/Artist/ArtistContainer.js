import ArtistCard from "./ArtistCard";

function ArtistContainer({ artists }) {
    return (
      <section>
           <ul className='cards'>
               {artists.map(artist => <ArtistCard  key={artist.id} artist={artist}  />)}
           </ul>
       </section>
    )
  }

export default ArtistContainer;