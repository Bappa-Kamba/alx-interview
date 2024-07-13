#!/usr/bin/node

'use_strict';
const request = require('request');

let movieID = process.argv[2];

function fetchMovieDetails(id, callback) {
    const SWAPI = `https://swapi-api.alx-tools.com/api/films/${id}`;

    request(SWAPI, { json: true }, (err, res, body) => {
        if (err) {
            return callback(err);
        }
        callback(null, body);
    });
}

function fetchCharacterDetails(url, callback) {
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

    console.log(`Title: ${data.title}`);
    console.log('Characters:');

    const characterURLs = data.characters;
    const characterNames = [];
    let completedRequests = 0;

    characterURLs.forEach(url => {
        fetchCharacterDetails(url, (error, character) => {
            if (error) {
                console.log(`Error fetching character details: ${error}`);
                return;
            }

            characterNames.push(character.name);
            completedRequests++;

            if (completedRequests === characterURLs.length) {
                characterNames.forEach(name => console.log(name));
            }
        });
    });
});

