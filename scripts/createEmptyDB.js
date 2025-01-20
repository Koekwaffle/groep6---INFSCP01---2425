const sqlite3 = require('sqlite3').verbose();
const fs = require('fs');
const path = require('path');

// Path to your original database
const sourceDB = path.join(__dirname, '..', 'ILY_TEST.db');
// Path for the new empty database
const newDB = path.join(__dirname, '..', 'ILY_TEST.db');

// Make sure we don't overwrite an existing empty database
if (fs.existsSync(newDB)) {
    fs.unlinkSync(newDB);
}

// Connect to the source database
const source = new sqlite3.Database(sourceDB);
const destination = new sqlite3.Database(newDB);

source.serialize(() => {
    // Get the schema from the original database
    source.all("SELECT sql FROM sqlite_master WHERE sql IS NOT NULL AND type='table'", [], (err, tables) => {
        if (err) {
            console.error('Error reading schema:', err);
            return;
        }

        destination.serialize(() => {
            // Create each table in the new database
            tables.forEach(table => {
                if (table.sql && !table.sql.includes('sqlite_')) {
                    destination.run(table.sql, [], err => {
                        if (err) {
                            console.error('Error creating table:', err);
                        }
                    });
                }
            });

            console.log('Empty database created successfully!');
            destination.close();
        });
    });
});

source.close();
