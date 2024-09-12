import { useFormik } from "formik";
import { useNavigate } from "react-router-dom";
import * as yup from "yup";

function ReviewForm() {
    const navigate = useNavigate();

    const schema = yup.object().shape({
        content: yup.string().required("Required"),
        rating: yup.number().positive("Must be positive").required("Required"),
        artist_id: yup.string().required("Required"),
        song_id: yup.string().required("Required"),
        user_id: yup.string().required("Required"),
        created_at: yup.string().required("Required"),
        updated_at: yup.string().required("Required"),
    });

    const formik = useFormik({
        initialValues: {
            content: "",
            rating: 0,
            artist_id: "",
            song_id: "",
            user_id: "",
            created_at: "",
            updated_at: "",
        },
        validationSchema: schema,
        onSubmit: (values) => {
            fetch("/review", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(values),
            })
            .then((res) => {
                console.log('Response Status:', res.status); // Log the status code

                return res.text().then((text) => {
                    console.log('Response Text:', text); // Log the response text

                    if (res.ok) {
                        const jsonResponse = JSON.parse(text); // Parse the text if the status is OK
                        navigate(`/reviews/${jsonResponse.id}`);
                    } else {
                        console.error("Error response:", text); // Log the error response
                    }
                });
            })
            .catch((error) => {
                console.error("Fetch error:", error); // Log any fetch errors
            });
        },
    });

    return (
        <section>
            <label htmlFor="rating">Rating</label>
                <input
                    type="number"
                    id="rating"
                    name="rating"
                    value={formik.values.rating}
                    onChange={formik.handleChange}
                    onBlur={formik.handleBlur}
                />
                {formik.touched.rating && formik.errors.rating ? (
                    <p style={{ color: "red" }}>{formik.errors.rating}</p>
                ) : null}

            <form onSubmit={formik.handleSubmit} className="form">
                <label htmlFor="content">Review</label>
                <input
                    type="text"
                    id="content"
                    name="content"
                    value={formik.values.content}
                    onChange={formik.handleChange}
                    onBlur={formik.handleBlur}
                />
                {formik.touched.content && formik.errors.content ? (
                    <p style={{ color: "red" }}>{formik.errors.content}</p>
                ) : null}

                <label htmlFor="artist">Artist</label>
                <input
                    type="text"
                    id="artist"
                    name="artist"
                    value={formik.values.artist_id}
                    onChange={formik.handleChange}
                    onBlur={formik.handleBlur}
                />
                {formik.touched.artist_id && formik.errors.artist_id ? (
                    <p style={{ color: "red" }}>{formik.errors.artist_id}</p>
                ) : null}

                <label htmlFor="song">Song</label>
                <input
                    type="text"
                    id="song_id"
                    name="song_id"
                    value={formik.values.song_id}
                    onChange={formik.handleChange}
                    onBlur={formik.handleBlur}
                />
                {formik.touched.song_id && formik.errors.song_id ? (
                    <p style={{ color: "red" }}>{formik.errors.song_id}</p>
                ) : null}

                <label htmlFor="User">User</label>
                <input
                    type="text"
                    id="user_id"
                    name="user_id"
                    value={formik.values.user_id}
                    onChange={formik.handleChange}
                    onBlur={formik.handleBlur}
                />
                {formik.touched.user_id && formik.errors.user_id ? (
                    <p style={{ color: "red" }}>{formik.errors.user_id}</p>
                ) : null}

                <label htmlFor="biography">Biography</label>
                <input
                    type="text"
                    id="biography"
                    name="biography"
                    value={formik.values.biography}
                    onChange={formik.handleChange}
                    onBlur={formik.handleBlur}
                />
                {formik.touched.biography && formik.errors.biography ? (
                    <p style={{ color: "red" }}>{formik.errors.biography}</p>
                ) : null}

                <label htmlFor="created">Created at</label>
                <input
                    type="text"
                    id="created_at"
                    name="created_at"
                    value={formik.values.created_at}
                    onChange={formik.handleChange}
                    onBlur={formik.handleBlur}
                />
                {formik.touched.created_at && formik.errors.created_at ? (
                    <p style={{ color: "red" }}>{formik.errors.created_at}</p>
                ) : null}

                <label htmlFor="updated">Updated at</label>
                <input
                    type="text"
                    id="updated_at"
                    name="updated_at"
                    value={formik.values.updated_at}
                    onChange={formik.handleChange}
                    onBlur={formik.handleBlur}
                />
                {formik.touched.updated_at && formik.errors.updated_at ? (
                    <p style={{ color: "red" }}>{formik.errors.updated_at}</p>
                ) : null}

                <button type="submit">Submit</button>
            </form>
        </section>
    );
}

export default ReviewForm;

