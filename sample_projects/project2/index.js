const helper = require('./helper');
const api = require('./api');

class App {
  constructor() {
    this.api = api;
  }
  
  async run() {
    helper.helper();  // Similar to utils.helper()
    await this.api.connect();
    console.log('App running...');
  }
}

module.exports = App;

