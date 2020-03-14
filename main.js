const fs = require('fs');
const structure = require('./structure.json');

let rows = [];

function parse(structure, path) {
    if (Array.isArray(structure)) {
        const message = structure[0];

        if (typeof message.value === "object") {
            const values = message.value;
            const columns = Object.keys(values).map(value => [
                `${path}__${value}`,
                `${path.replace(/__/g, '.')}.value`,
                value
            ].join(','));
            rows.push(...columns);
        }
        else {
            const columns = [
                path,
                `${path.replace(/__/g, '.')}.value`,
                ''
            ];
            rows.push(columns.join(','));
        }
    }
    else if (typeof structure === "object") {
        for (const key in structure) {
            parse(structure[key], path ? `${path}__${key}` : key);
        }
    }
}

parse(structure, '');
fs.writeFileSync('./output.csv', 'name,path,property\n' + rows.join('\n'));