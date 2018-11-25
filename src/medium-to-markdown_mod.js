const mediumToMarkdown = require('medium-to-markdown');
 
mediumToMarkdown.convertFromUrl("https://medium.freecodecamp.org/python-collection-of-my-favorite-articles-8469b8455939").then(function (markdown) {
  console.log(markdown); //=> Markdown content of medium post
});