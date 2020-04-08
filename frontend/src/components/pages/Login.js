import React from 'react';
import { Link } from "react-router-dom";

import Header from './../layout/Header'

function Login() {
  return (
    <div className="Login-bg">
      <Header/>
      <div class="container-fluid h-100">
        <div class="row justify-content-center align-items-center h-100">
            <div class="col col-sm-6 col-md-6 col-lg-4 col-xl-3">
                <form action="">
                    <div class="form-group">
                      <input 
                        id="input-email" 
                        class="text-white bg-transparent rounded-0 form-control border border-white border-left-0 border-top-0 border-right-0" 
                        placeholder="Email" 
                        type="email"/>
                    </div>
                    <div class="form-group">
                      <input 
                        id="input-password" 
                        class="text-white bg-transparent rounded-0 form-control border border-white border-left-0 border-top-0 border-right-0" 
                        placeholder="Password"  
                        type="password"/>
                    </div>
                    <div class="form-group">
                      <Link to={{ pathname: "/dash-alerts"}}>
                        <button 
                          class="bg-transparent btn btn-outline-light btn-block rounded-pill border-primary">
                          Login
                        </button>
                      </Link>
                    </div>
                </form>
            </div>
        </div>
      </div>
    </div>

  )
}

export default Login;