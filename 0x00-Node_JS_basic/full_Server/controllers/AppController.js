// Controller for homepage

class AppController {
  static getHomepage(request, response) {
    return response.end('Hello Holberton School!');
  }
}

module.exports = AppController;
