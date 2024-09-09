import { useFormik } from "formik";
import { redirect } from "react-router-dom";
import * as yup from "yup";

function ArtistForm() {

	const schema = yup.object().shape({
		name: yup.string().required("required"),
		age: yup.number().positive("must be positive"),
        gender: yup.string().required("required"),
        birth_date: yup.string().required("required"),
        birth_place: yup.string().required("required"),
        biography: yup.string().required("required"),
		image: yup.string().required("required"),
	});

	const formik = useFormik({
		initialValues: {
			name: "",
			age: 0,
			gender: "",
            birth_date: "",
            birth_place: "",
            biography: "",
            image: "",
		},
		validationSchema: schema,
		onSubmit: (values) => {

			console.log(values);
			fetch("/artists", {
				method: "POST",
				headers: {
					"content-type": "application/json",
				},
				body: JSON.stringify(values),
			}).then((res) => {
				if (res.ok) {
					res.json().then((artist) => {
						console.log(artist);
						redirect(`/artists/${artist.id}`);
					});
				} else {
					res.json().then(err => console.log("oops"))
				}
			});
		},
	});
	return (
		<section>
			<form onSubmit={formik.handleSubmit} className="form">
				<label>Full Name </label>

				<input
					type="text"
					name="name"
					value={formik.values.name}
					onChange={formik.handleChange}
					onBlur={formik.handleBlur}
				/>
				{formik.touched.name && formik.errors.name ? (
					<h3 style={{ color: "red" }}>{formik.errors.name}</h3>
				) : (
					""
				)}
				<label>Age </label>

				<input
					type="text"
					name="age"
					value={formik.values.image}
					onChange={formik.handleChange}
					onBlur={formik.handleBlur}
				/>
                {formik.touched.age && formik.errors.age ? (
					<h3 style={{ color: "red" }}>{formik.errors.age}</h3>
				) : (
					""
				)}
		
				<label>Gender </label>

				<input
					type="text"
					name="gender"
					value={formik.values.age}
					onChange={formik.handleChange}
					onBlur={formik.handleBlur}
				/>
				{formik.touched.gender && formik.errors.gender ? (
					<h3 style={{ color: "red" }}>{formik.errors.gender}</h3>
				) : (
					""
				)}
				<label>Birthday </label>
				<input
					type="text"
					name="Birthday"
					value={formik.values.birth_date}
					onChange={formik.handleChange}
					onBlur={formik.handleBlur}
				/>
                {formik.touched.birth_date && formik.errors.birth_date ? (
					<h3 style={{ color: "red" }}>{formik.errors.birth_date}</h3>
				) : (
					""
				)}
                <label>Birth place </label>
				<input
					type="text"
					name="Birth place"
					value={formik.values.birth_place}
					onChange={formik.handleChange}
					onBlur={formik.handleBlur}
				/>
                {formik.touched.birth_place && formik.errors.birth_place ? (
					<h3 style={{ color: "red" }}>{formik.errors.birth_place}</h3>
				) : (
					""
				)}
                <label>Biography </label>
				<input
					type="text"
					name="Biography"
					value={formik.values.biography}
					onChange={formik.handleChange}
					onBlur={formik.handleBlur}
				/>
                {formik.touched.biography && formik.errors.biography ? (
					<h3 style={{ color: "red" }}>{formik.errors.biography}</h3>
				) : (
					""
				)}
                <label>Image</label>
				<input
					type="text"
					name="Image"
					value={formik.values.image}
					onChange={formik.handleChange}
					onBlur={formik.handleBlur}
				/>
                {formik.touched.image && formik.errors.image ? (
					<h3 style={{ color: "red" }}>{formik.errors.image}</h3>
				) : (
					""
				)}
				<input className="button" type="submit" />
			</form>
		</section>
	);
}

export default ArtistForm;