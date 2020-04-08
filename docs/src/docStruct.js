/**
 *
 * @param {String} dom The DOM in string
 */
const makeDocStruct = (in_dom) => {
  let h1Count = 0;
  let h2Count = 0;
  let h3Count = 0;
  let h4Count = 0;

  const dom = Array.from(in_dom);
  for (let i = 0; i < dom.length; i++) {
    if (dom[i] === `<` && dom[i + 1] === `h` && dom[i + 2] === `1`) {
      h1Count++;
      h2Count = 0;
      h3Count = 0;
      h4Count = 0;

      dom.splice(i + 3, 0, ` data-headerNum="${h1Count}" `);
    } else if (dom[i] === `<` && dom[i + 1] === `h` && dom[i + 2] === `2`) {
      h2Count++;
      h3Count = 0;
      h4Count = 0;
      dom.splice(i + 3, 0, ` data-headerNum="${h1Count}.${h2Count}" `);
    } else if (dom[i] === `<` && dom[i + 1] === `h` && dom[i + 2] === `3`) {
      h3Count++;
      h4Count = 0;
      dom.splice(i + 3, 0, ` data-headerNum="${h1Count}.${h2Count}.${h3Count}" `);
    } else if (dom[i] === `<` && dom[i + 1] === `h` && dom[i + 2] === `4`) {
      h4Count++;
      dom.splice(i + 3, 0, ` data-headerNum="${h1Count}.${h2Count}.${h3Count}.${h4Count}" `);
    }
  }

  const retrievedDom = dom.join("");
  return retrievedDom;
};

module.exports = makeDocStruct;
