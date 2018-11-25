const mediumToMarkdown = require('medium-to-markdown');
 
mediumToMarkdown.convertFromUrl('https://medium.com/@williamkoehrsen/five-minutes-to-your-own-website-fd0b43cbd886')
.then(function (markdown) {
  console.log(markdown); //=> Markdown content of medium post
});