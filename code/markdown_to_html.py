#!/usr/bin/env python

import argparse
import sys
import inspect
import jinja2
import markdown

TEMPLATE = """<!DOCTYPE html>
<html>
<head>
    <link href="http://netdna.bootstrapcdn.com/twitter-bootstrap/2.3.0/css/bootstrap-combined.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Roboto:100,100i,300,300i,400,400i,500,500i,700,700i,900,900i" rel="stylesheet"><style>
        body {
            font-family:  'Roboto', sans-serif;
            font-size: 18px;
            font-weight: 400;
            line-height: 2.2;
        }
        h3::first-letter { 
            font-size: 100%;
        }
        span { 
            font-size: 300%;
            font-weight: 600;
            line-height: 1;
        }
        blockquote {
          background: #f9f9f9;
          border-left: 10px solid #ccc;
          margin: 1.5em 10px;
          padding: 0.5em 10px;
          quotes: "\201C""\201D""\2018""\2019";
        }
        blockquote p {
          line-height: 2.2;
          font-size: 18px;
          font-weight: 400;
        }
    </style>
</head>
<body>
<div class="container">
{{content}}
</div>
</body>
</html>
"""


def parse_args(args=None):
    d = 'Make a complete, styled HTML document from a Markdown file.'
    parser = argparse.ArgumentParser(description=d)
    parser.add_argument('mdfile', type=argparse.FileType('r'), nargs='?',
                        default=sys.stdin,
                        help='File to convert. Defaults to stdin.')
    parser.add_argument('-o', '--out', type=argparse.FileType('w'),
                        default=sys.stdout,
                        help='Output file name. Defaults to stdout.')
    return parser.parse_args(args)


def main(args=None):
    args = parse_args(args)
    md = args.mdfile.read()
    extensionlist = ['extra', 'smarty']
    html = markdown.markdown(md, extensions=extensionlist)
    doc = jinja2.Template(TEMPLATE).render(content=html)
    args.out.write(doc)


if __name__ == '__main__':
    sys.exit(main())
