// Home page grid: search, filter, optional side-by-side with Huashu's sticker.
// Row: [slug, name, sci, family, agree, months, photo, sticker, english, chinese, observationId]
(function () {
  var D = window.BIRDS || [], T = window.T || {};
  var grid = document.getElementById("grid"), more = document.getElementById("more");
  var q = document.getElementById("q"), f = document.getElementById("f"), cmp = document.getElementById("cmp");
  var list = D, shown = 0, PAGE = 60;
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function fill(s, o) { return s.replace(/\{(\w)\}/g, function (_, k) { return o[k]; }); }
  try { cmp.checked = localStorage.getItem("cmp") === "1"; } catch (e) {}
  function report(r) {
    var p = { template: "wrong-photo.yml", title: "[photo] " + r[2] + " " + r[8], species: r[2] + " (" + r[9] + " / " + r[8] + ")",
      photo: "https://www.inaturalist.org/observations/" + r[10] };
    return T.repo + "/issues/new?" + Object.keys(p).map(function (k) { return k + "=" + encodeURIComponent(p[k]); }).join("&");
  }
  function card(r) {
    var href = "birds/" + r[0] + "/", c = cmp.checked && r[7];
    var imgs = '<a href="' + href + '"><img loading="lazy" src="' + esc(r[6]) + '" alt="' + esc(r[1]) + '">' + (c ? '<figcaption>' + esc(T.photo_cap) + '</figcaption>' : '') + '</a>';
    if (c) imgs += '<figure><img loading="lazy" src="' + esc(r[7]) + '" alt="' + esc(T.huashu_cap + " " + r[1]) + '"><figcaption>' + esc(T.huashu_cap) + '</figcaption></figure>';
    return '<article class="card' + (c ? ' cmp' : '') + '"><div class="imgs">' + imgs + '</div><div class="meta">' +
      '<a class="nm" href="' + href + '">' + esc(r[1]) + '</a><span class="sc">' + esc(r[2]) + '</span>' +
      '<div class="row"><span class="ev">' + esc(fill(T.evidence, { a: r[4], m: r[5] })) + '</span>' +
      '<a class="rp" href="' + esc(report(r)) + '" rel="noopener">' + esc(T.report) + '</a></div></div></article>';
  }
  function render(reset) {
    if (reset) { shown = 0; grid.innerHTML = ""; }
    var next = list.slice(shown, shown + PAGE);
    grid.insertAdjacentHTML("beforeend", next.map(card).join(""));
    shown += next.length;
    document.getElementById("count").textContent = list.length ? fill(T.count, { n: list.length.toLocaleString() }) : T.no_result;
    more.style.display = shown < list.length ? "block" : "none";
  }
  function apply() {
    var s = q.value.trim().toLowerCase(), v = f.value;
    list = D.filter(function (r) {
      return (!s || (r[1] + " " + r[2] + " " + r[3]).toLowerCase().indexOf(s) >= 0) && (v === "all" || r[4] >= 5);
    });
    render(true);
  }
  q.addEventListener("input", apply);
  f.addEventListener("change", apply);
  cmp.addEventListener("change", function () { try { localStorage.setItem("cmp", cmp.checked ? "1" : "0"); } catch (e) {} render(true); });
  more.addEventListener("click", function () { render(false); });
  apply();
})();
