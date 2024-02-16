#!/usr/bin/node

const request = require('request');

function makeRequest (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (!error && response.statusCode === 200) {
        resolve(JSON.parse(body));
      }
    });
  });
}
async function printChars (movieId) {
  try {
    const film = await makeRequest(`https://swapi-api.alx-tools.com/api/films/${movieId}/`);
    const chars = film.characters;

    for (const charUrl of chars) {
      const char = await makeRequest(charUrl);
      console.log(char.name);
    }
  } catch (error) {
    console.error(error);
  }
}

const filmId = process.argv[2];
if (filmId) {
  printChars(filmId);
}
