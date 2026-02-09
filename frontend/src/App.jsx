import { BrowserRouter, Route, Routes } from "react-router-dom"
import Login from './screens/Login'
import Layout from './hocs/Layout'
import Homepage from './screens/Homepage'
import Signup from './screens/Signup'
import "./app.css"
import ResetPassword from "./screens/ResetPassword"
import ResetPasswordConfirm from "./screens/ResetPasswordConfirm"
import PrivateRoutes from "./hocs/PrivateRoutes"
import { AuthProvider } from "./hocs/AuthProvider"

function App() {

  return (
    <AuthProvider>
      <BrowserRouter>
        <Layout>
          <Routes>
            <Route element={<PrivateRoutes />}>
              <Route path="/" element={<Homepage />}>
              </Route>
            </Route>
            <Route path="/login" element={<Login />}>
            </Route>
            <Route path="/signup" element={<Signup />}>
            </Route>
            <Route path="/reset-password" element={<ResetPassword />}>
            </Route>
            <Route path="/password/reset/confirm/:uid/:token" element={<ResetPasswordConfirm />}>
            </Route>
          </Routes>
        </Layout>
      </BrowserRouter >
    </AuthProvider>
  )
}

export default App