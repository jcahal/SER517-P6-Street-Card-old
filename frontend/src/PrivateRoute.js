 import React from 'react';
 import { Route, Redirect } from 'react-router-dom';

  export const PrivateRoute = ({ component: Component,...rest }) => (

  <Route {...rest} render={(props) => (
  	console.log("naren")
    localStorage.getItem('token') === true
      ? <Component 
      		{...props}
      	/>
      : <Redirect to='/login' />

  )} />


)