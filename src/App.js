import {BrowserRouter as Router, Routes, Route} from "react-router-dom";
import Navbar from "./components/navbar/Navbar";
import ScrollToTop from "./utils/scrollToTop";
import Footer from "./components/footer/Footer";
import Home from "./pages/Home";
import './styles/main.css'
import FormValidation from "./components/formValidation/FormValidation";

function App() {
  return (
    <div className="App">
        <Router>
            <ScrollToTop />
            <Navbar />
            <Routes>
                <Route path="/" element={<Home />}/>
                {/*<Route path="/projects" element={<Projects />}/>*/}
                {/*<Route path="/project/:id" element={<Project/>}/>*/}
                {/*<Route path="/contacts" element={<Contacts />}/>*/}
                <Route path="/login" element={<FormValidation/>}/>
            </Routes>
            <Footer />
        </Router>
    </div>
  );
}

export default App;
