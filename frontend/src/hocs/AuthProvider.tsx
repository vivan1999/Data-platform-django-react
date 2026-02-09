import React, { useContext, useState, useEffect, createContext } from "react";
import api from "../api";
import { Navigate } from "react-router-dom";

interface AuthContextType{
    isAuthenticated: boolean;
    isLoading :  boolean;
    userRole?: 'admin' | 'user';
    login: ()=> void;
    logout: ()=> void;
}

export const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider = ({children})=>{
    const [isAuthenticated,setAuthenticated] = useState(false)
    const [isLoading,setIsLoading] = useState(true)
    const [userRole, setUserRole] = useState<'admin'|'user'>()

    useEffect(()=>{
        async function checkTokenValidity (){
            const token = localStorage.getItem("access");
            const refresh = localStorage.getItem("refresh");
            try{
                if(token){
                    const response = await api.post("/auth/jwt/verify/",{"token":token})
                    if(response.status == 200){
                        setAuthenticated(true)
                        console.log("checked validity")
                    }
                }
            }catch(e){
                console.log("token validate error : ",e) 
                console.log("Access token invalid, trying refresh");
                }
            try{
                if(refresh){
                    const response = await api.post("/auth/jwt/refresh/",{"refresh":refresh})
                    if(response.status == 200){
                        console.log(response)
                        localStorage.setItem("access",response.data["access"])
                        setAuthenticated(true)
                        console.log("checked validity in refresh")
                    }
                }
            }catch(err){
                console.log("Refresh token invalid");
                setAuthenticated(false);
            } finally {
                setIsLoading(false);
            }
        }
        checkTokenValidity()
    },[])
   
    const login = ()=>{
        setAuthenticated(true)
    }
    const logout = () =>{
        localStorage.clear()
        setUserRole(undefined)
        setAuthenticated(false)
    }

    return <AuthContext.Provider value={{isAuthenticated, isLoading, userRole, login, logout}}>
        {children}
    </AuthContext.Provider>
} 