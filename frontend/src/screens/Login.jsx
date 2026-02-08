import { useState } from "react"

export default function Login() {
    const [formData, setFormData] = useState(
        {
            email: "",
            password: ""
        }
    )
    const { email, password } = formData
    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value })
    }
    const submit = (e) => {
        e.preventDefault()
    }
    return (
        <div style={{
            height: "80vh", display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center"
        }}>
            Login to DATA Platform
            <form onSubmit={(e) => submit(e)}
                style={{ height: "30vh", width: "40vw", display: "flex", flexDirection: "column", alignContent: "space-between", }}>
                <div style={{ display: "flex", flexDirection: "row", justifyContent: "space-between" }}>
                    <label>EMAIL</label>
                    <input style={{ width: "20vw" }} placeholder="Email" type="email" name="email" value={email} onChange={(e) => handleChange(e)}>
                    </input>
                </div>
                <div style={{ display: "flex", flexDirection: "row", justifyContent: "space-between" }}>
                    <label>PASSWORD</label>
                    <input style={{ width: "20vw" }} placeholder="Password" type="password" name="password" value={password} onChange={(e) => handleChange(e)}>
                    </input>
                </div>
                <button name="submit" type="submit"> Log In</button>
            </form>
        </div>
    )
}
