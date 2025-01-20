const path = require('path');

const config = {
    production: path.join(__dirname, '..', 'ILY.db'),
    test: path.join(__dirname, '..', 'ILY_TEST.db')
};

module.exports = {
    getDatabasePath: () => {
        return process.env.NODE_ENV === 'test' ? config.test : config.production;
    }
};
