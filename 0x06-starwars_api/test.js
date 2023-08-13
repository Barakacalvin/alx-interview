#!/usr/bin/node
const request = require('request');

const filmId = process.argv[2];

if (!filmId) {
  console.log('Please provide a film ID as a command-line argument.');
  process.exit(1);
}

request.get(`https://swapi-api.alx-tools.com/api/films/${filmId}`, (error, response, body) => {
  if (error) {
    console.error('Error:', error.message);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Error:', `Request failed with status code ${response.statusCode}`);
    return;
  }

  const film = JSON.parse(body);
  const characterUrls = film.characters;
  const characterPromises = characterUrls.map(url => {
    return new Promise((resolve, reject) => {
      request.get(url, (error, response, body) => {
        if (error) {
          reject(new Error(`Error fetching character data: ${error.message}`));
          return;
        }

        if (response.statusCode !== 200) {
          reject(new Error(`Request failed with status code ${response.statusCode}`));
          return;
        }

        const character = JSON.parse(body);
        resolve(character.name);
      });
    });
  });

  Promise.all(characterPromises)
    .then(characters => {
      console.log(characters.join('\n'));
    })
    .catch(error => {
      console.error('Error:', error.message);
    });
});
