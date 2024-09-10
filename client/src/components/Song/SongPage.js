import React from 'react';
import SongContainer from './SongContainer'; // Make sure this import matches the filename

function SongPage({ songs }) {
  return (
    <SongContainer songs={songs} />
  );
}

export default SongPage;
