const tsne_data = require('./data.json');
const fs = require('fs');

let asia = [];
let northamerica = [];
let southamerica = [];
let europe = [];
let oceania = [];

for (let i = 0; i < tsne_data.length ; i++){
    if (tsne_data[i]['continent'] === 'asia'){
        asia.push(tsne_data[i]);
    } else if (tsne_data[i]['continent']  === 'northamerica') {
        northamerica.push(tsne_data[i])
    } else if (tsne_data[i]['continent']  === 'southamerica') {
        southamerica.push(tsne_data[i])
    }else if (tsne_data[i]['continent']  === 'europe') {
        europe.push(tsne_data[i])
    }else if (tsne_data[i]['continent']  === 'oceania') {
        oceania.push(tsne_data[i])
}};
fs.writeFileSync('asia.json', JSON.stringify(asia));
fs.writeFileSync('northamerica.json', JSON.stringify(northamerica));
fs.writeFileSync('southamerica.json', JSON.stringify(southamerica));
fs.writeFileSync('europe.json', JSON.stringify(europe));
fs.writeFileSync('oceania.json', JSON.stringify(oceania));