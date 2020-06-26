## Automation

This readme guides the website maintainer to auto-generate jsons suitable for tables in Database page.

1. ### Execute `python ./getRepoInfoOSF.py`

   This makes the API calls to OSF and collects all downloadable filepaths with download links; then stores it into a json in the `./output` folder

2. ### Execute `python ./makeJsonTableOSF.py`
   This takes the previously created json (full of paths and links) as the input and constructs the json for the download-tables in the Database page; then stores it in the `./output` folder.

### Important!

Any entry that does not follow the `realm > country > year > month` pattern must be removed manually from the first json before executing the step-2.

The path of the last json should be included in the `fetch` portion in Database page.
