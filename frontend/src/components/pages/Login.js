import React from 'react';
// import { Link } from "react-router-dom";
import useForm from 'react-hook-form/dist/react-hook-form.ie11';
import Header from './../layout/Header';
// import { Redirect } from 'react-router';

function Login() {
  const { handleSubmit, register, errors } = useForm();
  const onSubmit = e => {
    window.location.href = "/dash-alerts";
  } 
  
  return (
    <div className="Login-bg">
      <Header/>
      <div class="container-fluid h-100">
        <div class="row justify-content-center align-items-center h-100">
            <div class="col col-sm-6 col-md-6 col-lg-4 col-xl-3">
                <form onSubmit={handleSubmit(onSubmit)}>
                    <div class="form-group">
                      <input 
                        name="email"
                        ref={register({
                          required: 'Required',
                          validate: value => value === 'admin@cirrustransit.com' || 'Invalid Email'
                        })}
                        id="input-email" 
                        class="text-white bg-transparent rounded-0 form-control border border-white border-left-0 border-top-0 border-right-0" 
                        placeholder="Email" 
                        type="Email"
                      />
                         <p style={{color: "red"}}>{errors.email && errors.email.message}</p>
                    </div>
                    <div class="form-group">    
                      <input 
                        name="password"
                        ref={
                          register({
                            validate: value => value === 'admin' || 'Invalid Password' 
                          })
                        }
                        id="input-password" 
                        class="text-white bg-transparent rounded-0 form-control border border-white border-left-0 border-top-0 border-right-0" 
                        placeholder="Password"  
                        type="password"
                      />
                       <p style={{color: "red"}}>{errors.password && errors.password.message}</p>
                    </div>
                    <div class="form-group">
                      {/* <Link to={{
                        pathname: "/dash-alerts"
                      }} */}
                      >
                        <button 
                          type="submit"
                          class="bg-transparent btn btn-outline-light btn-block rounded-pill border-primary"
                        >
                            Login
                        </button>
                      {/* </Link> */}
                    </div>
                </form>
            </div>
        </div>
      </div>
    </div>

  )
}

export default Login;