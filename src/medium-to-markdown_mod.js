const mediumToMarkdown = require('medium-to-markdown');
 
mediumToMarkdown.convertFromUrl("https://medium.com/swlh/what-i-learned-about-procrastination-while-scaling-my-startup-to-4-2-million-users-b07ba29309e").then(function (markdown) {
  console.log(markdown); //=> Markdown content of medium post
});