import React from 'react';
import ReviewContainer from './ReviewContainer'; // Make sure this import matches the filename

function ReviewPage({ reviews }) {
  return (
    <ReviewContainer reviews={reviews} />
  );
}

export default ReviewPage;