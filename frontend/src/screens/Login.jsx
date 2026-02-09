import { useState, useEffect, useContext } from "react"
import api from "../api"
import { useNavigate } from "react-router-dom"
import { AuthContext } from "../hocs/AuthProvider"

export default function Login() {
    const navigate = useNavigate()
    const { login } = useContext(AuthContext)
    const [formData, setFormData] = useState(
        {
            email: "",
            password: ""
        }
    )
    useEffect(() => {
        api.get("auth/users/me/").then((response) => {
            console.log("from login page result:", response.data)
        })
    }, [])

    const { email, password } = formData
    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value })
    }
    const submit = async (e) => {
        e.preventDefault()
        console.log(formData)
        const response = await api.post("auth/jwt/create/", formData)
        console.log("login access creds", response.data)
        if (response.status == 200) {
            localStorage.setItem("access", response.data["access"])
            localStorage.setItem("refresh", response.data["refresh"])
            login() // from the auth context
            navigate("/")
        }
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
