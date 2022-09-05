const exp = require('constants');
const fs = require('fs');
const path = require("path");
const FILE_NAME = 'titled_data.csv'
const csvPath = path.join(__dirname, FILE_NAME);
const csv = fs.readFileSync(csvPath, "utf-8")

const rows = csv.split('\n')
if(rows[rows.length -1] === ''){
    console.log("empty has been found");
    rows.pop();
}
console.log(rows);

let results = []
let columnTitle = []
for (const i in rows){
    const row = rows[i]
    const row_d = row.replace('\r','')
    const data = row_d.split(",")
    if (i == '0') {
        columnTitle = data
    } else {
        let row_data = {}
        for (const index in columnTitle) {
            const title = columnTitle[index]
            row_data[title] = data[index]
        }
        results.push(row_data)
    }
}

const result = JSON.stringify(results);
fs.writeFileSync('data.json',result);
module.exports = results;