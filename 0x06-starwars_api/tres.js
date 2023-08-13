#!/usr/bin/node

const request = require('request');

function getStarWarsFilms() {
  return new Promise((resolve, reject) => {
    request('https://swapi-api.alx-tools.com/api/films', (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const data = JSON.parse(body);
        resolve(data.results);
      }
    });
  });
}

function getCharactersByFilm(film) {
  return new Promise((resolve, reject) => {
    const characterUrls = film.characters;
    const characterPromises = characterUrls.map(url => {
      return new Promise((resolve, reject) => {
        request(url, (error, response, body) => {
          if (error) {
            reject(error);
          } else {
            const characterData = JSON.parse(body);
            resolve(characterData.name);
          }
        });
      });
    });

    Promise.all(characterPromises)
      .then(characters => {
        resolve({ film: film.title, characters: characters });
      })
      .catch(error => {
        reject(error);
      });
  });
}

const filmId = process.argv[2];

if (!filmId) {
  console.log('Please provide a film ID as a command-line argument.');
  process.exit(1);
}

getStarWarsFilms()
  .then(films => {
    const film = films.find(film => film.episode_id === Number(filmId));
    if (!film) {
      throw new Error(`Film with ID ${filmId} not found.`);
    }
    return getCharactersByFilm(film);
  })
  .then(result => {
    console.log(`${result.characters.join('\n')}`);
  })
  .catch(error => {
    console.error('Error:', error);
  });
