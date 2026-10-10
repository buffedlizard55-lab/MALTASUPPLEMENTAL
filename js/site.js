/* Shared Malta Trip Companion shell and data-driven topic renderer. */
(function () {
  "use strict";

  var body = document.body;
  var root = body && body.dataset.root ? body.dataset.root : ".";
  var links = [
    ["Overview", "index.html"],
    ["Getting around", "pages/transport.html"],
    ["Food & drink", "pages/food.html"],
    ["Activities & sights", "pages/activities.html"],
    ["Everyday life", "pages/everyday.html"],
    ["Radio sport", "pages/radio.html"],
    ["Expense planner", "pages/expenses.html"],
    ["Sources", "sources.html"]
  ];

  function addShell() {
    var header = document.getElementById("site-header");
    if (header) {
      var current = window.location.pathname.replace(/\/$/, "");
      var navHtml = links.map(function (item) {
        var href = root + "/" + item[1];
        var pathname = new URL(href, window.location.href).pathname.replace(/\/$/, "");
        var active = current === pathname || (item[1] === "index.html" && current === root);
        return '<a href="' + href + '"' + (active ? ' aria-current="page"' : "") + ">" + item[0] + "</a>";
      }).join("");
      header.className = "site-header";
      header.innerHTML =
        '<div class="header-inner">' +
          '<a class="brand" href="' + root + '/index.html" aria-label="Malta trip companion home">' +
            '<span class="brand-mark" aria-hidden="true">M</span>' +
            '<span>Malta Trip Companion<small>13–19 October 2026</small></span>' +
          '</a>' +
          '<button class="nav-toggle" type="button" aria-expanded="false" aria-controls="main-nav">Menu</button>' +
          '<nav class="main-nav" id="main-nav" aria-label="Main navigation">' + navHtml + '</nav>' +
        '</div>';

      var toggle = header.querySelector(".nav-toggle");
      var nav = header.querySelector(".main-nav");
      toggle.addEventListener("click", function () {
        var open = nav.classList.toggle("open");
        toggle.setAttribute("aria-expanded", open ? "true" : "false");
        toggle.textContent = open ? "Close menu" : "Menu";
      });
    }

    var footer = document.getElementById("site-footer");
    if (footer) {
      footer.className = "site-footer";
      footer.innerHTML =
        '<div class="footer-inner">' +
          '<p class="footer-note"><strong>Planning aid, not a live booking or dispatch service.</strong> ' +
          'Schedules, fares, hours, weather and event access can change. Re-check the linked operator or organizer before setting out.</p>' +
          '<p class="footer-note">Trip window: 13–19 October 2026 · Hotel: AX ODYCY, Qawra · ' +
          '<a href="' + root + '/sources.html">Research sources &amp; open questions</a></p>' +
        '</div>';
    }
  }

  function text(value) {
    if (value === null || value === undefined || value === "") return "Not published / not verified";
    if (Array.isArray(value)) return value.map(text).join("; ");
    if (typeof value === "object") return JSON.stringify(value);
    return String(value);
  }

  function humanize(value) {
    return String(value).replace(/_/g, " ").replace(/\b\w/g, function (c) { return c.toUpperCase(); });
  }

  function make(tag, className, value) {
    var el = document.createElement(tag);
    if (className) el.className = className;
    if (value !== undefined) el.textContent = value;
    return el;
  }

  function createRecordCard(record) {
    var required = ["id", "name", "category", "area", "address", "hours", "price range", "description", "source_url", "source_type", "date_checked", "confidence", "notes"];
    var missing = required.filter(function (key) { return !Object.prototype.hasOwnProperty.call(record, key); });
    var article = make("article", "card record-card");
    article.dataset.search = [record.name, record.category, record.area, record.description, JSON.stringify(record.details || "")].join(" ").toLowerCase();
    article.dataset.category = record.category || "Uncategorized";

    var meta = make("div", "record-meta");
    meta.appendChild(make("span", "card-kicker", text(record.category)));
    var confidenceClass = record.confidence === "verified" ? "verified" : (record.confidence === "partially verified" ? "partially-verified" : "unverified");
    meta.appendChild(make("span", "badge " + confidenceClass, text(record.confidence)));
    article.appendChild(meta);
    article.appendChild(make("h3", "", text(record.name)));
    article.appendChild(make("p", "record-description", text(record.description)));

    var fields = make("dl", "record-fields");
    [
      ["Area", record.area],
      ["Address", record.address],
      ["Hours", record.hours],
      ["Price range", record["price range"]]
    ].forEach(function (pair) {
      fields.appendChild(make("dt", "", pair[0]));
      fields.appendChild(make("dd", "", text(pair[1])));
    });
    article.appendChild(fields);

    if (record.details && typeof record.details === "object") {
      var detailEntries = Object.keys(record.details).filter(function (key) {
        return record.details[key] !== null && record.details[key] !== undefined && record.details[key] !== "";
      });
      if (detailEntries.length) {
        var extra = make("div", "record-extra");
        detailEntries.forEach(function (key) {
          var value = record.details[key];
          var p = make("p");
          p.appendChild(make("strong", "", humanize(key) + ": "));
          p.appendChild(document.createTextNode(text(value)));
          extra.appendChild(p);
        });
        article.appendChild(extra);
      }
    }

    var sources = [];
    if (record.source_url) sources.push({ label: "Primary source", url: record.source_url, type: record.source_type });
    if (Array.isArray(record.additional_sources)) {
      record.additional_sources.forEach(function (source) { sources.push(source); });
    }
    var sourceRow = make("div", "record-source");
    if (sources.length) {
      sources.forEach(function (source) {
        if (!source || !source.url) return;
        var link = make("a", "", source.label || "Source");
        link.href = source.url;
        link.target = "_blank";
        link.rel = "noopener noreferrer";
        sourceRow.appendChild(link);
        if (source.type) sourceRow.appendChild(make("span", "badge source-type", source.type));
      });
    } else {
      sourceRow.appendChild(make("span", "badge unverified", "No source URL recorded"));
    }
    sourceRow.appendChild(make("span", "small", "Checked: " + text(record.date_checked)));
    article.appendChild(sourceRow);

    if (record.notes) article.appendChild(make("p", "record-notes", "Notes: " + text(record.notes)));
    if (missing.length) {
      article.classList.add("data-error");
      article.appendChild(make("p", "callout danger", "Data schema incomplete: " + missing.join(", ")));
    }
    return article;
  }

  function renderDataset(container, dataset) {
    if (!dataset || !Array.isArray(dataset.records)) throw new Error("Expected a JSON object with a records array.");
    var heading = dataset.heading || "Verified trip information";
    var title = make("h2", "", heading);
    container.replaceChildren(title);

    var toolRow = make("div", "topic-tools");
    var searchLabel = make("label", "");
    searchLabel.appendChild(make("span", "visually-hidden", "Search records"));
    var search = document.createElement("input");
    search.type = "search";
    search.placeholder = "Search by name, area or detail";
    search.setAttribute("aria-label", "Search records by name, area or detail");
    searchLabel.appendChild(search);
    var filterLabel = make("label", "");
    filterLabel.appendChild(make("span", "visually-hidden", "Filter by category"));
    var filter = document.createElement("select");
    filter.setAttribute("aria-label", "Filter by category");
    var all = document.createElement("option");
    all.value = "";
    all.textContent = "All categories";
    filter.appendChild(all);
    Array.from(new Set(dataset.records.map(function (record) { return text(record.category); }))).sort().forEach(function (category) {
      var option = document.createElement("option");
      option.value = category;
      option.textContent = category;
      filter.appendChild(option);
    });
    filterLabel.appendChild(filter);
    toolRow.append(searchLabel, filterLabel);
    container.appendChild(toolRow);

    var status = make("p", "small muted", "");
    status.setAttribute("aria-live", "polite");
    container.appendChild(status);
    var grid = make("div", "record-grid");
    var cards = dataset.records.map(createRecordCard);
    cards.forEach(function (card) { grid.appendChild(card); });
    container.appendChild(grid);

    function applyFilters() {
      var query = search.value.trim().toLowerCase();
      var category = filter.value;
      var visible = 0;
      cards.forEach(function (card) {
        var match = (!query || card.dataset.search.indexOf(query) !== -1) && (!category || card.dataset.category === category);
        card.hidden = !match;
        if (match) visible += 1;
      });
      status.textContent = visible + (visible === 1 ? " item" : " items") + " shown";
      var oldEmpty = container.querySelector(".empty-state");
      if (!visible && !oldEmpty) container.appendChild(make("p", "empty-state", "No records match these filters."));
      if (visible && oldEmpty) oldEmpty.remove();
    }
    search.addEventListener("input", applyFilters);
    filter.addEventListener("change", applyFilters);
    applyFilters();
  }

  function loadTopicData() {
    var container = document.querySelector("[data-topic-data]");
    if (!container) return;
    var dataPath = container.getAttribute("data-topic-data");
    fetch(dataPath, { credentials: "same-origin" })
      .then(function (response) {
        if (!response.ok) throw new Error("HTTP " + response.status);
        return response.json();
      })
      .then(function (data) { renderDataset(container, data); })
      .catch(function (error) {
        console.error("Could not load topic data:", error);
        container.replaceChildren(make("p", "load-error", "Topic data could not be loaded. Please open this page through the GitHub Pages site or a local web server (not as a file:// URL), then try again."));
      });
  }

  document.addEventListener("DOMContentLoaded", function () {
    addShell();
    loadTopicData();
  });
})();
