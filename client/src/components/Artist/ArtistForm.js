import { useFormik } from "formik";
import { useNavigate } from "react-router-dom";
import * as yup from "yup";

function ArtistForm() {
    const navigate = useNavigate();

    const schema = yup.object().shape({
        name: yup.string().required("Required"),
        age: yup.number().positive("Must be positive").required("Required"),
        gender: yup.string().required("Required"),
        birth_date: yup.string().required("Required"),
        birth_place: yup.string().required("Required"),
        biography: yup.string().required("Required"),
        image: yup.string().required("Required"),
    });

    const formik = useFormik({
        initialValues: {
            name: "",
            age: "",
            gender: "",
            birth_date: "",
            birth_place: "",
            biography: "",
            image: "",
        },
        validationSchema: schema,
        onSubmit: (values) => {
            fetch("/artist", {
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
                        navigate(`/artists/${jsonResponse.id}`);
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
            <form onSubmit={formik.handleSubmit} className="form">
                <label htmlFor="name">Full Name</label>
                <input
                    type="text"
                    id="name"
                    name="name"
                    value={formik.values.name}
                    onChange={formik.handleChange}
                    onBlur={formik.handleBlur}
                />
                {formik.touched.name && formik.errors.name ? (
                    <p style={{ color: "red" }}>{formik.errors.name}</p>
                ) : null}

                <label htmlFor="age">Age</label>
                <input
                    type="number"
                    id="age"
                    name="age"
                    value={formik.values.age}
                    onChange={formik.handleChange}
                    onBlur={formik.handleBlur}
                />
                {formik.touched.age && formik.errors.age ? (
                    <p style={{ color: "red" }}>{formik.errors.age}</p>
                ) : null}

                <label htmlFor="gender">Gender</label>
                <input
                    type="text"
                    id="gender"
                    name="gender"
                    value={formik.values.gender}
                    onChange={formik.handleChange}
                    onBlur={formik.handleBlur}
                />
                {formik.touched.gender && formik.errors.gender ? (
                    <p style={{ color: "red" }}>{formik.errors.gender}</p>
                ) : null}

                <label htmlFor="birth_date">Birth Date</label>
                <input
                    type="text"
                    id="birth_date"
                    name="birth_date"
                    value={formik.values.birth_date}
                    onChange={formik.handleChange}
                    onBlur={formik.handleBlur}
                />
                {formik.touched.birth_date && formik.errors.birth_date ? (
                    <p style={{ color: "red" }}>{formik.errors.birth_date}</p>
                ) : null}

                <label htmlFor="birth_place">Birth Place</label>
                <input
                    type="text"
                    id="birth_place"
                    name="birth_place"
                    value={formik.values.birth_place}
                    onChange={formik.handleChange}
                    onBlur={formik.handleBlur}
                />
                {formik.touched.birth_place && formik.errors.birth_place ? (
                    <p style={{ color: "red" }}>{formik.errors.birth_place}</p>
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

                <label htmlFor="image">Image URL</label>
                <input
                    type="text"
                    id="image"
                    name="image"
                    value={formik.values.image}
                    onChange={formik.handleChange}
                    onBlur={formik.handleBlur}
                />
                {formik.touched.image && formik.errors.image ? (
                    <p style={{ color: "red" }}>{formik.errors.image}</p>
                ) : null}

                <button type="submit">Submit</button>
            </form>
        </section>
    );
}

export default ArtistForm;

