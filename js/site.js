/* MALTASUPPLEMENTAL — site.js
   1) Mobile nav toggle
   2) Budget calculator on costs.html (pure client-side, no external calls)
*/
(function () {
  "use strict";

  // ---------- mobile nav ----------
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.querySelector(".main-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.textContent = open ? "Close menu" : "Menu";
    });
  }

  // ---------- budget calculator ----------
  var calc = document.getElementById("budget-calc");
  if (!calc) return;

  var EURUSD = 1.145; // labelled estimate, close of 22 Sep 2026 (TradingEconomics via MALTA dossier)

  var ids = {
    nights: "c_nights",
    airfareCovered: "c_airfare",
    hotelCovered: "c_hotel",
    foodPerDay: "c_food",
    transport: "c_transport",
    transfers: "c_transfers",
    activities: "c_activities",
    sim: "c_sim",
    ecoTax: "c_eco",
    buffer: "c_buffer",
    taxRate: "c_taxrate"
  };

  function num(id, fallback) {
    var el = document.getElementById(id);
    if (!el) return fallback;
    var v = parseFloat(el.value);
    return isNaN(v) ? fallback : v;
  }

  function render() {
    var nights = num(ids.nights, 7);
    var days = nights + 1;

    var airfare = num(ids.airfareCovered, 0);      // $ you pay (0 if covered)
    var hotel = num(ids.hotelCovered, 0);          // $ you pay (0 if covered)
    var food = num(ids.foodPerDay, 30) * days;     // $
    var transport = num(ids.transport, 35);        // $
    var transfers = num(ids.transfers, 60);        // $
    var activities = num(ids.activities, 80);      // $
    var sim = num(ids.sim, 15);                    // $
    var ecoTax = num(ids.ecoTax, 11);              // $ (€1.50/night x1.145 x7)
    var buffer = num(ids.buffer, 150);             // $

    var total = airfare + hotel + food + transport + transfers + activities + sim + ecoTax + buffer;

    // Tax: only on the FMV of the prize you receive (airfare + hotel + ticket you did NOT pay)
    var fmv = (airfare === 0 ? 1100 : airfare) + (hotel === 0 ? 900 : hotel) + 100; // ticket est $100
    var taxRate = num(ids.taxRate, 30) / 100;      // combined federal + California estimate
    var tax = fmv * taxRate;

    var out = total + (airfare === 0 && hotel === 0 ? tax : 0);

    var el = document.getElementById("calc-out");
    if (!el) return;

    el.innerHTML =
      '<div style="display:flex;justify-content:space-between;flex-wrap:wrap;gap:10px;align-items:baseline">' +
      '<span>Your estimated out-of-pocket: <span class="big">$' + Math.round(out).toLocaleString() + "</span></span>" +
      '<span class="muted" style="color:#9fb0c3">EUR/USD ' + EURUSD + " (est.)</span></div>" +
      "<ul>" +
      "<li>Flights (you pay): $" + Math.round(airfare).toLocaleString() + "</li>" +
      "<li>Hotel (you pay): $" + Math.round(hotel).toLocaleString() + "</li>" +
      "<li>Food $" + num(ids.foodPerDay, 30) + "/day × " + days + " days: $" + Math.round(food).toLocaleString() + "</li>" +
      "<li>Local transport: $" + Math.round(transport).toLocaleString() + "</li>" +
      "<li>Airport transfers: $" + Math.round(transfers).toLocaleString() + "</li>" +
      "<li>Activities / extra entry fees: $" + Math.round(activities).toLocaleString() + "</li>" +
      "<li>Local SIM / eSIM: $" + Math.round(sim).toLocaleString() + "</li>" +
      "<li>Eco-tax (hotel pass-through): $" + Math.round(ecoTax).toLocaleString() + "</li>" +
      "<li>Buffer / incidentals: $" + Math.round(buffer).toLocaleString() + "</li>" +
      (airfare === 0 && hotel === 0
        ? "<li>Est. US tax on prize FMV (~$" + Math.round(fmv).toLocaleString() + " × " + num(ids.taxRate, 30) + "%): $" + Math.round(tax).toLocaleString() + "</li>"
        : "") +
      "</ul>" +
      '<p class="small" style="color:#8fa1b5;margin:10px 0 0">Estimate only — not tax advice. "0" in flights/hotel = covered by the prize. The calculator runs entirely in your browser.</p>';
  }

  Object.keys(ids).forEach(function (k) {
    var el = document.getElementById(ids[k]);
    if (el) el.addEventListener("input", render);
  });

  render();
})();
