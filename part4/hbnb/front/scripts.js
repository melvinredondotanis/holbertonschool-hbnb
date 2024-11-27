const host = 'localhost';
const port = '5000';


function getCookie(name)
{
  const cookies = document.cookie.split(';');
  for (let cookie of cookies)
  {
    const [cookie_name, cookie_value] = cookie.split('=');
    if (cookie_name.trim() === name)
      return cookie_value;
  }
  return null;
}


async function fetchPlaces(token)
{
  // Make a GET request to fetch places data
  // Include the token in the Authorization header
  // Handle the response and pass the data to displayPlaces function
}


function checkAuthentication()
{
  const token = getCookie('token');
  const loginLink = document.getElementById('login-link');

  if (!token)
  {
    loginLink.style.display = 'block';
  }
  else 
  {
    loginLink.style.display = 'none';
    fetchPlaces(token);
  }
}


function displayPlaces(places) {
  // Clear the current content of the places list
  // Iterate over the places data
  // For each place, create a div element and set its content
  // Append the created element to the places list
}


document.getElementById('price-filter').addEventListener('change', (event) => {
  // Get the selected price value
  // Iterate over the places and show/hide them based on the selected price
});


const login = 'http://' + host + ':' + port + '/api/v1/auth/login';
async function login_user(email, password) {
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
