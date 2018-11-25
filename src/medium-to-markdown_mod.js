const mediumToMarkdown = require('medium-to-markdown');
 
mediumToMarkdown.convertFromUrl("https://medium.com/@Alikayaspor/how-to-use-your-kindle-more-effective-to-cultivate-a-reading-habit-a61f0fe45f1d").then(function (markdown) {
  console.log(markdown); //=> Markdown content of medium post
});