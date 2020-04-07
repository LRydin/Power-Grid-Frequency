# Documentation generating workflow

This package generates the documentation website from a markdown file with only one command:

    npm run docgen markdown-file-path

The documentation webpage supports:

- LaTeX like symbols (using mathjax)
- Code highlighting (using highlight.js)

## Prerequisite

- Assumes that you have installed Node.JS in your machine

## Steps

- Navigate to the `/docs` folder and run `npm install`. This has to be done only once (i.e. only if you are running for the first time).

- If you're _.md_ file lives in the path: `"markdown-file-path"`, then run the command:

  > `npm run docgen "markdown-file-path"`

this should generate an `index.html` in the root directory.

### Example

    npm run docgen ../README.md

This command will generate the doc webpage from the README of this repo.

## Publish

- Create a branch `gh-pages`.
- Generate the doc.
- Push to `gh-pages`

The documentation website will automatically published in:

https://your-github-username.github.io/Power-Grid-Frequency/

See repository settings in github.
