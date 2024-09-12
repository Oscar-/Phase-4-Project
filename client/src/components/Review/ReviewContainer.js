import ReviewCard from "./ReviewCard";

function ReviewContainer({ review }) {
    return (
      <section>
           <ul className='cards'>
               {reviews.map(review => <ReviewCard  key={review.id} review={review}  />)}
           </ul>
       </section>
    )
  }

export default ReviewContainer;