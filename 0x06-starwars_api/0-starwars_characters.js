#!/usr/bin/node

'use_strict';
const request = require('request');

const movieID = process.argv[2];

function fetchMovieDetails (id, callback) {
  const SWAPI = `https://swapi-api.alx-tools.com/api/films/${id}`;

  request(SWAPI, { json: true }, (err, res, body) => {
    if (err) {
      return callback(err);
    }
    callback(null, body);
  });
}

function fetchCharacterDetails (url, callback) {
  request(url, { json: true }, (err, res, body) => {
    if (err) return callback(err);
    callback(null, body);
  });
}

fetchMovieDetails(movieID, (err, data) => {
  if (err) {
    console.error('Error fetching movie details:', err);
    return;
  }

  const characterURLs = data.characters;
  const characterNames = [];
  let index = 0;

  function fetchNextCharacter () {
    if (index < characterURLs.length) {
      fetchCharacterDetails(characterURLs[index], (error, character) => {
        if (error) {
          console.log(`Error fetching character details: ${error}`);
          return;
        }

        characterNames.push(character.name);
        console.log(character.name);

        index++;
        fetchNextCharacter(); // Fetch next character recursively
      });
    }
  }

  fetchNextCharacter();
});
