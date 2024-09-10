import SongCard from "./SongCard";

function SongContainer({songs}) {

    return (
     <section>
         <ul className='cards'>
             {songs.map(song => <SongCard  key={song.id} song={song}  />)}
         </ul>
     </section>
    )
  }
  
export default SongContainer;