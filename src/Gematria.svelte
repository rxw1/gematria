<!--
-->

<script>
  export let table;
  export let u;

  function f(x) {
    return parseInt(Math.pow(10,
      Math.floor((x - 1) / 9)) * (((x - 1) % 9) + 1));
  }

  let examples = [
    { str: "Ἰησοῦς", val: 888 },
    { str: "Χριστός", val: 1460 }
  ];

  let input = "";
  let chars = [];

  let uppercase = false;
  let verbose = false;

  function toggleCase() {
    uppercase = !uppercase;
  }

  function toggleVerbose() {
    verbose = !verbose;
  }

  function loadExample(str) {
    input = str;
    handleInput();
  }

  function clearInput() {
    input = "";
    handleInput();
  }

  function handleInput() {
    if (!input.length) {
      uppercase = false;
    }

    chars = [];
    [...input.normalize("NFD")].map((chr, idx) => {
      let hex = chr.charCodeAt().toString(16).padStart(4, '0').toUpperCase();

      let name = u[hex];

      if (!name) {
        return
      }

      let r = /^(GREEK|HEBREW|LATIN) (CAPITAL|SMALL)? ?LETTER ?(FINAL)? ?([A-Z]*)$/

      let pos = table.map(st => {
        //if (st.indexOf(hex) > -1) {
        if (st.indexOf(name.match(r)[4]) > -1) {
          return table.indexOf(st) + 1
        }
      }).filter(Boolean)[0]

      let val = f(pos)

      chars[idx] = {chr, hex, pos, val, name}
    })
  }

  function pull(chars, key) {
    return key ?
      Object.keys(chars).map(hex => chars[hex][key]) :
      Object.values(chars);
  }

</script>

<main>
  <nav>
    <div on:click={() => clearInput()}>clear</div>
    <div on:click={toggleVerbose} class={verbose ? 'on' : 'off'}>verbose</div>
    <br />
    <div on:click={() => loadExample(examples[0].str)}>{examples[0].str}</div>
    <div on:click={() => loadExample(examples[1].str)}>{examples[1].str}</div>
    <!--
    {@html examples.map(x => {
      return `<div on:click={loadExample(${x.str})}>${x.str}</div>`
    }).join("")}
    -->
  </nav>

  <input bind:value={input} on:input={handleInput} placeholder={examples[0].str}>

  <div class="value">
    {pull(chars, 'val').reduce((a, b) => a + b, 0)}
  </div>

  <div class="container" on:click={toggleCase}>
    {@html pull(chars, null).map(hex => {
      return `<div class="item">
        <div>
          ${uppercase ? hex.chr.toUpperCase() : hex.chr}
        </div>
        <div>
          ${hex.val}
        </div>
      </div>`
      }).join(`<div class="item">+</div>`)}
  </div>

  {#if verbose && chars.length}
  <table>
    <thead>
      <tr>
        <th>idx</th>
        <th>chr</th>
        <th>pos</th>
        <th>val</th>
        <th>hex</th>
        <th>name</th>
      </tr>
    </thead>
    <tbody>
      {@html Object.keys(chars).map(k => `
        <tr>
          <td>${k}</td>
          <td>${chars[k].chr}</td>
          <td>${chars[k].pos}</td>
          <td>${chars[k].val}</td>
          <td>${chars[k].hex}</td>
          <td>${chars[k].name}</td>
        </tr>
      `).join("")}
    </tbody>
    <tfoot>
      <tr>
        <td></td>
        <td></td>
        <td></td>
        <td>
          {Object.keys(chars).map(k => chars[k].val).reduce((a, b) => a + b, 0)}
        </td>
        <td></td>
        <td></td>
      </tr>
    </tfoot>
  </table>
  {/if}
</main>

<style>
  main {
    text-align: center;
    padding: 1em;
    margin: 0 auto;
  }

  main > input,
  main > div,
  main > table {
    margin-top: 50px;
  }

  nav {
    position: fixed;
    right: 50px;
    color: #dca;
    font-size: 0.8em;
    user-select: none;
  }

  nav > div:active {
    color: #dac;

  }

  .on {
    color: #777;
  }

  .off {
    color: #dca;
  }

  input {
    border: none;
    border-bottom: 2px solid #772;
    text-align: center;
    color: #579;
  }

  ::placeholder {
    color: #abc;
  }

  *:focus {
    outline: none;
  }

  h1 {
    color: #ff3e00;
    text-transform: uppercase;
    font-size: 4em;
    font-weight: 100;
  }

  table {
    border-collapse:collapse;
    font-family: monospace;
    max-width: 640px;
    margin: auto;
    /*
    border-spacing: 16px 0;
    */
  }

  thead th {
    text-align: left;
    padding-bottom: 12px;
    border-bottom: 2px solid #333;
    padding-right: 4px;
  }

  .lalign {
    text-align: left;
  }

  .ralign {
    text-align: right;
  }

  /* Table */

  tbody {
    text-align: left;
    border-collapse: collapse;
  }

  tfoot td,
  tbody tr {
    padding-top: 12px;
    border-top: 2px solid #333;
  }

  :global(td:not(:last-child)) {
    padding-right: 2em;
  }

  :global(td:nth-child(2)),
  :global(td:nth-child(3)),
  :global(td:nth-child(4)),
  :global(th:nth-child(2)),
  :global(th:nth-child(3)),
  :global(th:nth-child(4)) {
    text-align: right;
  }

  tbody:before,
  tfoot:before {
    content:"@";
    display:block;
    line-height:12px;
    text-indent:-99999px;
}

  /* Big Sum */

  main > div.value {
    font-size: 4em;
  }

  /* Calculation Flexbox */

  :global(.container) {
    display: inline-flex;
    align-items: center;
  }

  :global(.item) {
    flex-grow: 1;
    padding: 6px;
  }

  :global(.item > div:first-child) {
    border-bottom: 3px solid #333;
  }

  :global(.item > div) {
    padding: 4px;
    vertical-align: bottom;
  }

  @media (min-width: 640px) {
    main {
      max-width: none;
    }
  }
</style>
