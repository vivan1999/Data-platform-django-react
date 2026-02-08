import Navbar from "../Navbar/Navbar";

export default function Header(props) {
    return (
        <div>
            <Navbar />
            {
                props.children
            }
        </div>
    )
}
