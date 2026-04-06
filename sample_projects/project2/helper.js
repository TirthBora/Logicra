function helper() {
  // Similar to Python utils.helper()
  console.log('Helper function called');
  return 'helper result';
}

function processData(data) {
  return data.toUpperCase();
}

module.exports = { helper, processData };

