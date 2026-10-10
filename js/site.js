/* Shared interaction: accessible mobile navigation and local-only expense worksheet. */
(function () {
  "use strict";

  document.querySelectorAll(".nav-toggle").forEach(function (button) {
    var navId = button.getAttribute("aria-controls");
    var nav = navId ? document.getElementById(navId) : null;
    if (!nav) return;
    button.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      button.setAttribute("aria-expanded", open ? "true" : "false");
      button.textContent = open ? "Close menu" : "Menu";
    });
    nav.addEventListener("keydown", function (event) {
      if (event.key === "Escape") {
        nav.classList.remove("is-open");
        button.setAttribute("aria-expanded", "false");
        button.textContent = "Menu";
        button.focus();
      }
    });
  });

  var form = document.querySelector("[data-expense-form]");
  if (!form) return;

  var totalOutput = document.querySelector("[data-expense-total]");
  var possibleOutput = document.querySelector("[data-expense-possible]");
  var unknownOutput = document.querySelector("[data-expense-unknown]");
  var breakdown = document.querySelector("[data-expense-breakdown]");
  var currencySelect = form.querySelector("[data-expense-currency]");

  function readNumber(input, fallback) {
    var value = Number(input.value);
    if (!Number.isFinite(value) || value < 0) return fallback;
    return value;
  }

  function formatMoney(amount, currency) {
    try {
      return new Intl.NumberFormat(undefined, { style: "currency", currency: currency, maximumFractionDigits: 2 }).format(amount);
    } catch (error) {
      return currency + " " + amount.toFixed(2);
    }
  }

  function update() {
    var currency = currencySelect ? currencySelect.value : "EUR";
    var known = 0;
    var possible = 0;
    var unresolved = 0;
    var lineValues = [];

    form.querySelectorAll("[data-expense-line]").forEach(function (line) {
      var amountInput = line.querySelector("[data-amount]");
      var quantityInput = line.querySelector("[data-quantity]");
      var payerInput = line.querySelector("[data-payer]");
      var amount = amountInput ? readNumber(amountInput, 0) : 0;
      var quantity = quantityInput ? readNumber(quantityInput, 1) : 1;
      var payer = payerInput ? payerInput.value : "unknown";
      var value = amount * quantity;
      var label = line.getAttribute("data-label") || "Expense";
      possible += value;
      if (payer === "traveler") known += value;
      else if (payer === "unknown") unresolved += 1;
      lineValues.push({ label: label, amount: value, payer: payer });
    });

    if (totalOutput) totalOutput.textContent = formatMoney(known, currency);
    if (possibleOutput) possibleOutput.textContent = formatMoney(possible, currency);
    if (unknownOutput) unknownOutput.textContent = String(unresolved);
    if (breakdown) {
      breakdown.replaceChildren();
      lineValues.forEach(function (row) {
        var li = document.createElement("li");
        var label = document.createElement("span");
        var value = document.createElement("strong");
        var status = row.payer === "traveler" ? "Traveler pays" : (row.payer === "covered" ? "Covered" : "Unconfirmed");
        label.textContent = row.label + " · " + status;
        value.textContent = formatMoney(row.amount, currency);
        li.append(label, value);
        breakdown.append(li);
      });
    }
  }

  form.addEventListener("input", update);
  form.addEventListener("change", update);

  var resetButton = document.querySelector("[data-expense-reset]");
  if (resetButton) {
    resetButton.addEventListener("click", function () {
      form.reset();
      update();
    });
  }

  var downloadButton = document.querySelector("[data-expense-download]");
  if (downloadButton) {
    downloadButton.addEventListener("click", function () {
      var currency = currencySelect ? currencySelect.value : "EUR";
      var rows = [["category", "amount_per_unit", "quantity", "payer", "currency"]];
      form.querySelectorAll("[data-expense-line]").forEach(function (line) {
        var amountInput = line.querySelector("[data-amount]");
        var quantityInput = line.querySelector("[data-quantity]");
        var payerInput = line.querySelector("[data-payer]");
        rows.push([
          line.getAttribute("data-label") || "Expense",
          amountInput ? amountInput.value : "",
          quantityInput ? quantityInput.value : "1",
          payerInput ? payerInput.value : "unknown",
          currency
        ]);
      });
      var csv = rows.map(function (row) {
        return row.map(function (cell) { return '"' + String(cell).replace(/"/g, '""') + '"'; }).join(",");
      }).join("\r\n");
      var blob = new Blob([csv], { type: "text/csv;charset=utf-8" });
      var url = URL.createObjectURL(blob);
      var link = document.createElement("a");
      link.href = url;
      link.download = "malta-trip-expenses.csv";
      document.body.append(link);
      link.click();
      link.remove();
      URL.revokeObjectURL(url);
    });
  }

  update();
})();
