document.addEventListener("DOMContentLoaded", function () {
    const apiKey = 'YOUR_API_KEY';
    const searchButton = document.getElementById('search');
    const locationInput = document.getElementById('location');
    const weatherContainer = document.querySelector('.weather-container');

    searchButton.addEventListener('click', () => {
        const location = locationInput.value;
        const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${location}&appid=${apiKey}`;

        fetch(apiUrl)
            .then(response => response.json())
            .then(data => {
                // Extract and display weather data in the weather-container
                // You can customize this part based on the data you want to display
                const temperature = data.main.temp;
                const description = data.weather[0].description;

                weatherContainer.innerHTML = `
                    <h2>Weather in ${location}</h2>
                    <p>Temperature: ${temperature}°C</p>
                    <p>Description: ${description}</p>
                `;
            })
            .catch(error => {
                console.error('Error fetching data:', error);
                weatherContainer.innerHTML = '<p>Could not fetch weather data.</p>';
            });
    });
});
