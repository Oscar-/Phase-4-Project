import { redirect, useNavigate } from "react-router-dom";
import { useFormik } from "formik";
import * as yup from "yup";

function SongForm() {

	//1. create yup schema
	//2. use useFormik hook to set schema, initialValues, onSubmit
	//3. onSubmit POST request
	//4. hook up useFormik to JSX espeically the onSubmit, values, onChange, errors (opt)
	const navigate = useNavigate()
	
	//1. create schema for the values for form 
	const schema = yup.object().shape({
		name: yup.string().required("required"),
        length: yup.number().positive("must be greater than 0"),
        lyrics: yup.number().positive("must be greater than 0"),
		genre: yup.string(),
		release_dt: yup.string().required("required"),
		image: yup.string().required("required"),
	})

	//2. create use formik hook
	const formik = useFormik({
		//set initial values
		initialValues: {
			name: 'Could you be loved',
			length: '3:57',
			lyrics: 'Could you be loved and be love? Could you be loved and be love? Don\'t let them fool ya Or even try to school ya! Oh, no! We\'ve got a mind of our own So go to hell, if what you\'re thinking isn\'t right! Love would never leave us alone A-in the darkness, there must come out to light Could you be loved and be love? Could you be loved, woah, yeah And be loved? The road of life is rocky and you may stumble too So while you point your fingers someone else is judging you Love your brotherman! Could you be, could you be, could you be loved? Could you be, could you be loved? Could you be, could you be, could you be loved? Could you be, could you be loved?',
			genre: 'reggae',
			release_dt: '1980',
			image: 'https://upload.wikimedia.org/wikipedia/en/9/9f/CouldYouBeLoved.jpg'
		},
		//set schema
		validationSchema: schema,
		//3. create onSubmit callback
		//if your page is refreshing make sure you added onSubmit handler to JSX
		onSubmit: (values) => {
			console.log(formik.errors)
			//POST request
			fetch("http://127.0.0.1:5555/songs", {
				method: "POST",
				body: JSON.stringify(values),
				headers: {'content-type': 'application/json'}
			})
			.then(res => {
				if(res.ok){
					return res.json()
				} else {
					console.error("something went wrong with POST songs")
				}
			})
			.then(data => {
				console.log(`/songs/${data.id}`)
				//maybe update parent state and use inverse flow to pass up new production
				
				navigate(`/songs/${data.id}`)
			})

		}
	})
		


	return (
		<section>
			{/* 4. hook up formik submit, onchange, values, and errors */}
			<form onSubmit={formik.handleSubmit} className="form" >
				<label>Title </label>
				<input
					type="text"
					name="title"
					onChange={formik.handleChange}
					value={formik.values.title}
				/>
				{formik.errors.title && formik.touched.title ? (<h3 style={{ color: "red" }}>{formik.errors.title}</h3>) : "" }


				<label> Genre</label>
				<input
					type="text"
					name="genre"
					onChange={formik.handleChange}
					value={formik.values.genre}
				/>
				{formik.errors.genre && formik.touched.genre ? (<h3 style={{ color: "red" }}>{formik.errors.genre}</h3>) : "" }

				<label>Length</label>
				<input
					type="number"
					name="length"
					onChange={formik.handleChange}
					value={formik.values.length}
					
				/>
				{formik.errors.length && formik.touched.length ? (<h3 style={{ color: "red" }}>{formik.errors.length}</h3>) : "" }
				

				<label>Year</label>
				<input
					type="number"
					name="year"
					onChange={formik.handleChange}
					value={formik.values.year}
					
				/>
				{formik.errors.year && formik.touched.year ? (<h3 style={{ color: "red" }}>{formik.errors.year}</h3>) : "" }
				<label>Image</label>
				<input
					type="text"
					name="image"
					onChange={formik.handleChange}
					value={formik.values.image}
					
				/>
				
				<label>Language</label>
				<input
					type="text"
					name="language"
					onChange={formik.handleChange}
					value={formik.values.language}
					
				/>
				{formik.errors.language && formik.touched.language ? (<h3 style={{ color: "red" }}>{formik.errors.language}</h3>) : "" }

				<label>Director</label>
				<input
					type="text"
					name="director"
					onChange={formik.handleChange}
					value={formik.values.director}
					
				/>
				{formik.errors.director && formik.touched.director ? (<h3 style={{ color: "red" }}>{formik.errors.director}</h3>) : "" }

				<label>Description</label>
				<textarea
					type="text"
					rows="4"
					cols="50"
					name="description"
					onChange={formik.handleChange}
					value={formik.values.description}
					
				/>
				{formik.errors.description && formik.touched.description ? (<h3 style={{ color: "red" }}>{formik.errors.description}</h3>) : "" }
				
				<label>Composer</label>
				<input
					type="text"
					name="composer"
					onChange={formik.handleChange}
					value={formik.values.composer}
					
				/>
				{formik.errors.composer && formik.touched.composer ? (<h3 style={{ color: "red" }}>{formik.errors.composer}</h3>) : "" }

				<input className="button" type="submit" />
			</form>
		</section>
	);
}

export default SongForm;