import React from 'react'
import "./Login.css"

function Login() {
  return (
    <div className='form-container'>
        <h2 className='login-title'> Login </h2>
        <input type="text" name='text' className='username' placeholder='username'/>
        <input type="password" name="password" className="userpassword" placeholder="password" />
        <button className='loginBtn'>Login</button>
    </div>
  )
}

export default Login