import React from 'react';
import ReviewContainer from './ReviewContainer';

function ReviewPage({ reviews }) {
  return (
    <ReviewContainer reviews={reviews} />
  );
}

export default ReviewPage;