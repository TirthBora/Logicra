class API {
  async connect() {
    console.log('API connected');
  }
  
  async getData() {
    return { data: 'sample data' };
  }
}

module.exports = new API();

