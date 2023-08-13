#!/usr/bin/node
const request = require('request');

if (process.argv.length === 3) {
  const filmId = process.argv[2];
  const filmUrl = `https://swapi-api.hbtn.io/api/films/${filmId}/`;
  const options = { json: true };

  request(filmUrl, options, (error, response, filmData) => {
    if (error) {
      console.error('Error:', error);
    } else if (response.statusCode !== 200) {
      console.error('Error:', response.statusCode, filmData.detail);
    } else {
      const characterPromises = filmData.characters.map(characterUrl => {
        return new Promise((resolve, reject) => {
          request(characterUrl, options, (error, response, characterData) => {
            if (error) {
              reject(error);
            } else if (response.statusCode !== 200) {
              reject(new Error(`Error fetching character data: ${response.statusCode} ${characterData.detail}`));
            } else {
              resolve(characterData.name);
            }
          });
        });
      });

      Promise.all(characterPromises)
        .then(characters => {
          console.log(characters.join('\n'));
        })
        .catch(error => {
          console.error('Error:', error);
        });
    }
  });
}

