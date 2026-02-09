import { Navigate, Outlet, useLocation } from "react-router-dom";
import { useEffect, useState, useContext } from "react";
import api from "../api";
import { AuthContext } from "./AuthProvider";

export default function PrivateRoutes() {
    const { isAuthenticated, isLoading } = useContext(AuthContext)
    const location = useLocation()

    if (isLoading) {
        console.log("private routes : isauthenticated: ", isAuthenticated)
        return <div>Trying to log you in.....</div>
    }

    return isAuthenticated ? <Outlet /> : <Navigate to='/login' replace state={{ from: location }} />
}