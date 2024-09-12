import { useNavigate } from "react-router-dom";
import { useFormik } from "formik";
import * as yup from "yup";

function SongForm() {
    const navigate = useNavigate();

    // Create schema for form validation
    const schema = yup.object().shape({
        name: yup.string().required("Title is required"),
        length: yup.string().required("Length is required"),
        lyrics: yup.string().required("Lyrics are required"),
        genre: yup.string().required("Genre is required"),
        release_dt: yup.date().required("Release date is required").typeError('Release date must be a valid date'),
        image: yup.string().required("Image URL is required"),
    });

    // Create useFormik hook
    const formik = useFormik({
        initialValues: {
            name: '',
            length: '',
            lyrics: '',
            genre: '',
            release_dt: '',
            image: '',
        },
        validationSchema: schema,
        onSubmit: (values) => {
            console.log("Submitting song data:", values);  // Debug statement
            fetch("http://127.0.0.1:5555/song", {
                method: "POST",
                body: JSON.stringify(values),
                headers: { 'Content-Type': 'application/json' }
            })
            .then(res => {
                if (res.ok) {
                    return res.json();
                } else {
                    console.error("Something went wrong with POST request");
                    throw new Error("Failed to create song");
                }
            })
            .then(data => {
                navigate(`/song/${data.id}`);
            })
            .catch(error => {
                console.error(error.message);
            });
        }
    });

    return (
        <section>
            <form onSubmit={formik.handleSubmit} className="form">
                <label>Title</label>
                <input
                    type="text"
                    name="name"
                    onChange={formik.handleChange}
                    value={formik.values.name}
                />
                {formik.errors.name && formik.touched.name && (
                    <h3 style={{ color: "red" }}>{formik.errors.name}</h3>
                )}

                <label>Genre</label>
                <input
                    type="text"
                    name="genre"
                    onChange={formik.handleChange}
                    value={formik.values.genre}
                />
                {formik.errors.genre && formik.touched.genre && (
                    <h3 style={{ color: "red" }}>{formik.errors.genre}</h3>
                )}

                <label>Length</label>
                <input
                    type="text"
                    name="length"
                    onChange={formik.handleChange}
                    value={formik.values.length}
                />
                {formik.errors.length && formik.touched.length && (
                    <h3 style={{ color: "red" }}>{formik.errors.length}</h3>
                )}

                <label>Release Date</label>
                <input
                    type="date"  // Ensure correct date format
                    name="release_dt"
                    onChange={formik.handleChange}
                    value={formik.values.release_dt}
                />
                {formik.errors.release_dt && formik.touched.release_dt && (
                    <h3 style={{ color: "red" }}>{formik.errors.release_dt}</h3>
                )}

                <label>Image</label>
                <input
                    type="text"
                    name="image"
                    onChange={formik.handleChange}
                    value={formik.values.image}
                />
                {formik.errors.image && formik.touched.image && (
                    <h3 style={{ color: "red" }}>{formik.errors.image}</h3>
                )}

                <label>Lyrics</label>
                <textarea
                    rows="4"
                    cols="50"
                    name="lyrics"
                    onChange={formik.handleChange}
                    value={formik.values.lyrics}
                />
                {formik.errors.lyrics && formik.touched.lyrics && (
                    <h3 style={{ color: "red" }}>{formik.errors.lyrics}</h3>
                )}

                <input className="button" type="submit" />
            </form>
        </section>
    );
}

export default SongForm;
