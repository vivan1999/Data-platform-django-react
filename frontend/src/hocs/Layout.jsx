import Footer from "../components/Footer/Footer";
import Header from "../components/Header/Header";

export default function Layout(props) {
    return (
        <>
            <Header>
                <div style={{ color: "red", backgroundColor: "gold", textAlign: "center" }}>
                    hello this is a child of header sent as a prop.children
                </div>
            </Header>
            {props.children}
            <Footer />
        </>
    )
}
