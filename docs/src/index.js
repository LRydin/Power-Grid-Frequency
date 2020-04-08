const path = require("path");
const fs = require("fs");
var replace = require("replace");
const makeDocStruct = require("./docStruct");
const showdown = require("showdown");

const converter = new showdown.Converter({ tables: true });

const userInputPath = process.argv[2];
const rootDir = path.dirname(__dirname);
const inputFilePath = path.resolve(path.join(rootDir, userInputPath));

const sample_md = fs.readFileSync(inputFilePath, { encoding: "utf8" });

const outputHTMLChunk = converter.makeHtml(sample_md);

const docStructDOM = makeDocStruct(outputHTMLChunk);
const header = fs.readFileSync(path.resolve(__dirname, "../", "template", "header.txt"), { encoding: "utf8" });
const footer = fs.readFileSync(path.resolve(__dirname, "../", "template", "footer.txt"), { encoding: "utf8" });
const outputHTML = header + docStructDOM + footer;

fs.writeFileSync(path.resolve(__dirname, "../../", "index.html"), outputHTML);

replace({
  regex: ":x:",
  replacement: `<span class="cross">X</span>`,
  paths: [path.resolve(__dirname, "../../", "index.html")],
  recursive: true,
  silent: true,
});
