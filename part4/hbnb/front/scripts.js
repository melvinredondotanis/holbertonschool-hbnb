const API_CONFIG = {
    host: 'http://localhost',
    port: '5000',
    version: 'v1'
};
const apiUrl = `${API_CONFIG.host}:${API_CONFIG.port}/api/${API_CONFIG.version}`;


function setCookie(name, value, days) {
  const date = new Date();
  date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
  const expires = `expires=${date.toUTCString()}`;
  document.cookie = `${name}=${value}; ${expires}; path=/; domain=${window.location.hostname}`;
}

function getCookie(name) {
  const cookies = document.cookie.split(';');
  for (const cookie of cookies) {
    const [key, value] = cookie.trim().split('=');
    if (key === name) return value;
  }
  return null;
}

window.addEventListener('DOMContentLoaded', () => {
  if (window.location.pathname.includes('login.html') && getCookie('hbnb_token')) {
    window.location.href = 'index.html';
  }
});

window.addEventListener('load', () => {
  checkAuthentication()
});

function checkAuthentication() {
  const token = getCookie('hbnb_token');
  const loginLink = document.getElementById('login-link');
  const placesList = document.getElementById('places-list');

  if (loginLink) {
    if (!token) {
      loginLink.style.display = 'block';
    } else {
      loginLink.style.display = 'none';
    }
  }
  if (placesList) {
    fetchPlaces();
  }
}

function validateInput(password) {
  if (!password || password.length < 6) {
    throw new Error('Password too short');
  }
}

document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.getElementById('login-form');

  if (loginForm) {
    loginForm.addEventListener('submit', async (event) => {
      event.preventDefault();

      const email = loginForm.querySelector('[name="email"]').value;
      const password = loginForm.querySelector('[name="password"]').value;

      try {
        validateInput(password);
        const response = await fetch(`${apiUrl}/auth/login`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ email, password })
        });

        if (response.ok) {
          const data = await response.json();
          setCookie('hbnb_token', data.access_token, 1);
          window.location.href = 'index.html';
        } else {
          const error = await response.json();
          alert('Login failed: ' + (error.message || response.statusText));
        }
      } catch (error) {
        alert('Login failed: ' + error.message);
      }
    });
  }
});

async function fetchPlaces() {
  fetch(`${apiUrl}/places`)
    .then((response) => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then((data) => {
      displayPlaces(data);
    })
    .catch((error) => {
      console.error('Error: ', error);
    });
}

function displayPlaces(places) {
  const placesList = document.getElementById('places-list');
  placesList.innerHTML = '';

  places.forEach(place => {
    const placeCard = document.createElement('div');
    placeCard.classList.add('place-card');
    const placeInfo = `
      <div class="place-info">
          <h2>${place.title}</h2>
          <p>Price per night: $${place.price}</p>
      </div>
      <a href="place.html?id=${place.id}"><button class="details-button">View Details</button></a>
    `;
    placeCard.innerHTML = placeInfo;
    placesList.appendChild(placeCard);
  });
}
