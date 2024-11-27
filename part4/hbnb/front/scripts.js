// Initialize the API URL
const host = 'localhost';
const port = '5000';


// API URL for the login endpoint
const login = 'http://' + host + ':' + port + '/api/v1/auth/login';
async function login_user(email, password)
{
  const login_data = {
    'email': email,
    'password': password
  };

  const response = await fetch(login, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(login_data)
  });

  return response;
}


document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.getElementById('login-form');

  if (loginForm)
  {
    loginForm.addEventListener('submit', async (event) => {
      event.preventDefault();
      
      const email = document.getElementById('email').value;
      const password = document.getElementById('password').value;
      
      if (!email || !password)
      {
        alert('Email and password are required');
        return;
      }

      const response = await login_user(email, password);
      if (response.ok)
      {
        const data = await response.json();
        document.cookie = `token=${data.access_token}; path=/`;
        window.location.href = 'index.html';
      }
      else
        alert('Login failed: ' + response.statusText);
    });
  }
});
