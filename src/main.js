/*
 * https://en.wikipedia.org/wiki/Gematria
 * https://en.wikipedia.org/wiki/Isopsephy
 * http://www.unicode.org/reports/tr44/#UnicodeData.txt
 * http://unicode.org/Public/UCD/latest/ucd/UnicodeData.txt
 */

import u from "./u.json";
import App from "./Gematria.svelte";

const app = new App({
  target: document.body,
  props: {
    u,
    table: [
      ["A", "ALPHA", "ALEF"],
      ["B", "BETA", "BET"],
      ["C", "GAMMA", "GIMEL"],
      ["D", "DELTA", "DALET"],
      ["E", "EPSILON", "HE"],
      ["F", "DIGAMMA", "STIGMA", "VAV"],
      ["G", "ZETA", "ZAYIN"],
      ["H", "ETA", "HET"],
      ["I", "THETA", "TET"],
      ["J", "IOTA", "YOD"],
      ["K", "KAPPA", "KAF"],
      ["L", "LAMDA", "LAMED"],
      ["M", "MU", "MEM"],
      ["N", "NU", "NUN"],
      ["O", "XI", "SAMEKH"],
      ["P", "OMICRON", "AYIN"],
      ["Q", "PI", "PE"],
      ["R", "KOPPA", "TSADI"],
      ["S", "RHO", "QOF"],
      ["T", "SIGMA", "RESH"],
      ["U", "TAU", "SHIN"],
      ["V", "UPSILON", "TAV"],
      ["W", "PHI", "FINAL KAF"],
      ["X", "CHI", "FINAL MEM"],
      ["Y", "PSI", "FINAL NUN"],
      ["Z", "OMEGA", "FINAL PE"],
      ["SAMPI", "FINAL TSADI"],
    ],
  },
});

export default app;
