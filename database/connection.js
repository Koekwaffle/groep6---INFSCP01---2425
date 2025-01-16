const sqlite3 = require('sqlite3').verbose();
const { getDatabasePath } = require('../config/database');

const db = new sqlite3.Database(getDatabasePath());

module.exports = db;
