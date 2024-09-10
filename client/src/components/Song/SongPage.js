import React from 'react'
import SongContainer from './SongCard'

function SongPage({ songs }) {
  return (
    <SongContainer songs={songs} />
  )
}

export default SongPage;