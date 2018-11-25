const mediumToMarkdown = require('medium-to-markdown');
 
mediumToMarkdown.convertFromUrl("https://medium.com/@priyansh.jain0246/how-i-automated-the-boring-university-stuff-with-python-f2935b10d2ce").then(function (markdown) {
  console.log(markdown); //=> Markdown content of medium post
});