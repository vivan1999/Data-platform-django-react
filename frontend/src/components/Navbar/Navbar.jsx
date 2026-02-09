import { useContext } from "react"
import { AuthContext } from "../../hocs/AuthProvider"
import { useNavigate, useLocation } from "react-router-dom"

export default function Navbar() {
    const { logout } = useContext(AuthContext)
    const location = useLocation()
    const navigate = useNavigate()

    const handleLogout = () => {
        logout()
        navigate("/login")
    }

    return (
        <div style={{ height: "100px", width: "100vw", backgroundColor: "black", color: "white" }}>
            Navbar
            <div>
                <button onClick={logout}>Logout</button>
            </div>
        </div>
    )
}
