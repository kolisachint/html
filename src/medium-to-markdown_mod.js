const mediumToMarkdown = require('medium-to-markdown');
 
mediumToMarkdown.convertFromUrl("https://medium.com/@jeremysim_58438/the-worlds-gone-flat-evolutions-in-interface-design-cb7ddd295f54").then(function (markdown) {
  console.log(markdown); //=> Markdown content of medium post
});