import React from "react";
import SongCard from "./SongCard";

function SongContainer({ songs, onDeleteSong }) {
    return (
        <section>
            <ul className='cards'>
                {songs.map(song => (
                    <SongCard 
                        key={song.id} 
                        song={song} 
                        onDelete={onDeleteSong} 
                    />
                ))}
            </ul>
        </section>
    );
}

export default SongContainer;
