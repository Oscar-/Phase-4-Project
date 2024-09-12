import React from 'react';
import SongContainer from './SongContainer'; 

function SongPage({ songs }) {
  return (
    <SongContainer songs={songs} />
  );
}

export default SongPage;
