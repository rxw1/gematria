<script>

  import { fade, fly } from 'svelte/transition';
  import { cubicIn, quadIn, circIn, expoIn, quartIn, quintIn, sineIn, elasticIn, elasticOut } from 'svelte/easing';
  import { flip } from 'svelte/animate';


  export let table;
  export let u;

	let a = [];

  function f(x) {
    return parseInt(Math.pow(10,
      Math.floor((x - 1) / 9)) * (((x - 1) % 9) + 1));
  }

  let links = [
    { url: "https://en.wikipedia.org/wiki/Gematria", name: "Gematria" },
    { url: "https://en.wikipedia.org/wiki/Isopsephy", name: "Isopsephy" }
  ]

  let examples = [
    { str: "נרון קסר", val: 666 }, // Nero Caesar. The Greek version of Nero's name (Neron Kaisar) transliterates into Hebrew as נרון קסר (NRON QSR)

    // { str: "Louisa", val: 500 },

    { str: "סוד", val: 70 }, // secret
    { str: "יין", val: 70 }, // wine

    { str: "René", val: 150 },
    { str: "asdf", val: 111 },

    { str: "Jesus", val: 515 },
    { str: "IHSOYS", val: 977 },
    { str: "Χριστός", val: 1460 },
    { str: "Ἰησοῦς", val: 888 },
  ];

  let input = "";
  let chars = [];

	let sum = 0;
	let dsum1= null;
	let dsum2 = null;
	let dsum3 = null;

  let menu = false;
  let verbose = false;
  let uppercase = false;

  function toggleMenu() {
    menu = !menu;
  }

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

	//function dsum(arr, n) {
	//	arr = [].concat(arr)
	//	let l = arr.length
	//	let last = arr[l - 1]
	//	if (l >= n) {
	//		console.log(arr)
	//		return arr
	//	}
	//		return arr.concat(dsum(last.toString().split("").reduce((a, b) => parseInt(a) + parseInt(b), 0)))




	//	//if ([].concat(arr[arr.length -1].length) >= 1) {
	//	//	console.log(arr)
	//	//	return arr
	//	//} else {
	//	//	let r = dsum([...arr, arr[arr.length -1].reduce((a, b) => parseInt(a) + parseInt(b), 0)])
	//	//	console.log(r)
	//	//}
	//}

	function dsum(str) {
		return str.toString().split("").reduce((a, b) => parseInt(a) + parseInt(b), 0).toString();
	}

  function handleInput() {
    if (!input.length) {
      uppercase = false;
    }

		sum = 0;
		dsum1= null;
		dsum2 = null;
		dsum3 = null;
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

			chars = chars.filter(Boolean);

			sum = pull(chars, 'val').reduce((a, b) => parseInt(a) + parseInt(b), 0).toString()
			dsum1 = sum && sum.length > 1 ? dsum(sum) : null;
			dsum2 = dsum1 && dsum1.length > 1 ? dsum(dsum1) : null;
			dsum3 = dsum2 && dsum2.length > 1 ? dsum(dsum2) : null;

			// if (sum[0] && sum[0].length > 1) {
			// 	let ns = sum.push(getSum(sum[0].split("").map(x => +x)))
			// 	console.log(ns);
			// }

			// if (sum[1] && sum[1].length > 1) {
			// 	sum.push(getSum(sum[1].split("").map(x => +x)))
			// }

			//console.log(sum);

    })
  }

  function pull(chars, key) {
    let r = key ?
      Object.keys(chars).map(hex => chars[hex][key]) :
      Object.values(chars).filter(Boolean);

		return r;
  }

  function exampleList() {
    examples.map(example => {
      return `<div on:click={() => loadExample(${example.str})}>${example.str}</div>`
    }).join(" ")
  }

	function isPrime(n) {
		if (n<2) return false;
		for (let i = 2; i <= Math.sqrt(n); i++) 
			if (n % i == 0) return false;
		return true;
	}


	const factors = number => Array
		.from(Array(number + 1), (_, i) => i)
		.filter(i => number % i === 0)

	//const sumVal = (a, b) => parseInt(a) + parseInt(b)

</script>

<main>
  <div class="menu">
    <nav>
      {#if menu}
        <div>
          {#each examples as example}
            <div on:click={() => loadExample(example.str)}>{example.str}</div>
          {/each}
        </div>
        <div>
          {#each links as link}
            <a href={link.url} target="_blank">{link.name}</a>
          {/each}
        </div>
        <div>
          <div on:click={() => clearInput()}>clear</div>
          <div on:click={toggleVerbose} class={verbose ? 'on' : 'off'}>verbose</div>
        </div>
      {/if}
      <div class="toggleMenu" on:click={toggleMenu}>menu</div>
    </nav>
  </div>

  <div class="input">
    <input bind:value={input} on:input={handleInput}
    placeholder={examples[Math.floor(Math.random() * examples.length)].str}>
  </div>

  <div class="value">{sum}</div>

	{#if (dsum1)}
		<div class="value2"> {dsum1} </div>
		{#if (dsum2)}
			<div class="value3"> {dsum2} </div>
			{#if (dsum3)}
				<div class="value4"> {dsum3} </div>
			{/if}
		{/if}
	{/if}

  <div class="value3">
		{isPrime(+sum) ? 'prime' : factors(+sum).filter(x =>
			x != +sum && x != 1).join(", ")}
	</div>



<!--
  <div class="value3">
    {pull(chars, 'val').reduce(sumVal, 0).toString().split("").reduce(sumVal, 0).toString().split("").reduce(sumVal, 0)}
  </div>
-->


  <div class="container" on:click={toggleCase}>

		<!--
		{#each chars.map((e, i) => [e, null]) as char}
		<div in:fade="{{ duration: 400, easing: circIn }}" class="item">
		-->

    {#each chars as char, i}
			<div class="item">
				<div>
					{uppercase ? char.chr.toUpperCase() : char.chr}
				</div>
				<div>
					{char.val}
				</div>
			</div>
			{#if (i < chars.length - 1)}
				<div class="item">+</div>
			{/if}
    {/each}
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

<style type="text/scss">

  $mainPadding: 1em;

  main {
    text-align: center;
    padding: $mainPadding;
    margin: 0 auto;
  }

  main > input,
  main > div,
  main > table {
    margin-top: 80px;
  }

  nav {
    position: fixed;
    min-width: 80px;
    right: 60px;
    color: #dca;
    font-size: 0.8em;
    user-select: none;
    border: 1px solid #333;
    padding: 1em;
    position: fixed;
    bottom: 20px;
    right: 20px;
    background-color: #fec;
    box-shadow: -2px -2px 2px 1px rgba(0, 0, 0, 0.1);
  }


  nav .toggleMenu {
    margin: 0;
    padding: 0;
  }

  nav > div > div:hover {
    color: #333;
  }

  nav > div > div:active {
    color: #dac;
  }

  nav > div:not(:first-child) {
    margin-top: 6px;
  }

  nav > div > a {
    display: block;
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

  input:focus::placeholder {
    color: transparent;
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
    min-width: 640px;
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

  main > div.value2 {
		margin-top: 0;
    font-size: 2em;
  }

  main > div.value3 {
		margin-top: 0;
    font-size: 1em;
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

  :global(.item:after) {
		/* content: 'xxx' */
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

  @media (max-width: 400px) {

    $mainPadding: 60px;

    :global(.container) {
      flex-wrap: wrap;
    }
    :global(.item) {
      flex-grow: 1;
      padding: 2px;
    }

    main {
      padding: 0;
      margin: 0;
    }
    nav {
      border: 2px solid #333;
      padding: 1em;
      position: fixed;
      bottom: 20px;
      right: 20px;
      background-color: #fec;
      box-shadow: -2px -2px 2px 1px rgba(0, 0, 0, 0.2);
    }
    main > input,
    main > div,
    main > table {
      margin-top: $mainPadding;
    }

  }
</style>
