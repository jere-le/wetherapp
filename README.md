# Pyttis - Suomalainen Sääsovellus

Pyttis on yksinkertainen sääsovellus, joka näyttää ajantasaiset säätiedot mille tahansa kaupungille. Sovellus on toteutettu Python Flask -kehyksellä ja se käyttää OpenWeatherMap API:a säätietojen hakemiseen.

## Ominaisuudet

- Hae säätietoja kaupungin nimellä
- Näyttää lämpötilan Celsius-asteina
- Näyttää säätilan kuvauksen suomeksi
- Näyttää säätä vastaavan kuvakkeen

## Teknologiat

- Python 3
- Flask
- OpenWeatherMap API
- HTML
- dotenv (ympäristömuuttujien hallintaan)

## Asennus

1. Kloonaa tämä repositorio:
   ```
   git clone [repository-url]
   cd pyttis
   ```

2. Asenna tarvittavat riippuvuudet:
   ```
   pip install flask requests python-dotenv
   ```

3. Hanki API-avain OpenWeatherMap-palvelusta:
   - Rekisteröidy osoitteessa [OpenWeatherMap](https://openweathermap.org/)
   - Luo uusi API-avain
   
4. Luo `.env`-tiedosto projektin juurihakemistoon ja lisää API-avaimesi:
   ```
   OPENWEATHER_API_KEY=sinun_api_avaimesi_tähän
   ```

## Käyttö

1. Käynnistä sovellus:
   ```
   python app.py
   ```

2. Avaa selain ja siirry osoitteeseen:
   ```
   http://localhost:5000
   ```

3. Syötä haluamasi kaupungin nimi ja paina "Hae sää" -nappia.

## Kehitys

Sovellus käynnistyy kehitystilassa, jossa muutokset koodiin päivittyvät automaattisesti.

## Lisenssi

[Lisää lisenssi tähän]

---

# Pyttis - Finnish Weather Application

Pyttis is a simple weather application that displays current weather information for any city. The application is built with Python Flask framework and uses the OpenWeatherMap API to fetch weather data.

## Features

- Search for weather information by city name
- Displays temperature in Celsius
- Shows weather description in Finnish
- Displays a weather icon corresponding to the conditions

## Technologies

- Python 3
- Flask
- OpenWeatherMap API
- HTML
- dotenv (for environment variable management)

## Installation

1. Clone this repository:
   ```
   git clone [repository-url]
   cd pyttis
   ```

2. Install the required dependencies:
   ```
   pip install flask requests python-dotenv
   ```

3. Get an API key from OpenWeatherMap:
   - Register at [OpenWeatherMap](https://openweathermap.org/)
   - Create a new API key
   
4. Create a `.env` file in the project root directory and add your API key:
   ```
   OPENWEATHER_API_KEY=your_api_key_here
   ```

## Usage

1. Start the application:
   ```
   python app.py
   ```

2. Open a browser and navigate to:
   ```
   http://localhost:5000
   ```

3. Enter the name of the city you want to check and press the "Hae sää" (Get Weather) button.

## Development

The application runs in debug mode, which automatically updates when changes are made to the code.

## License

[Add license here]
