/* MALTASUPPLEMENTAL — accessible, dependency-free shared navigation and JSON page renderer. */
(function () {
  "use strict";

  var NAV = [
    ["index.html", "Overview"],
    ["getting-around.html", "Transport"],
    ["restaurants.html", "Food & cafés"],
    ["activities.html", "Activities & sights"],
    ["everyday.html", "Everyday guide"],
    ["radio.html", "Sports radio"],
    ["costs.html", "Expense planner"],
    ["sources.html", "Sources & status"]
  ];

  function make(tag, className, text) {
    var el = document.createElement(tag);
    if (className) el.className = className;
    if (text !== undefined && text !== null) el.textContent = text;
    return el;
  }

  function renderShell() {
    var current = window.location.pathname.split("/").pop() || "index.html";
    var header = document.querySelector("[data-site-header]");
    if (header) {
      var wrap = make("div", "header-inner");
      var brand = document.createElement("a");
      brand.className = "brand";
      brand.href = "index.html";
      var mark = make("span", "brand-mark", "MT");
      mark.setAttribute("aria-hidden", "true");
      brand.appendChild(mark);
      var brandText = make("span", "", "MALTA TRIP GUIDE");
      brandText.appendChild(make("small", "", "Qawra · 13–19 October 2026"));
      brand.appendChild(brandText);
      wrap.appendChild(brand);

      var toggle = make("button", "nav-toggle", "Menu");
      toggle.type = "button";
      toggle.setAttribute("aria-expanded", "false");
      toggle.setAttribute("aria-controls", "main-navigation");
      wrap.appendChild(toggle);

      var nav = make("nav", "main-nav");
      nav.id = "main-navigation";
      nav.setAttribute("aria-label", "Main navigation");
      NAV.forEach(function (entry) {
        var link = make("a", "", entry[1]);
        link.href = entry[0];
        if (entry[0] === current) link.setAttribute("aria-current", "page");
        nav.appendChild(link);
      });
      wrap.appendChild(nav);
      header.replaceChildren(wrap);
      toggle.addEventListener("click", function () {
        var expanded = toggle.getAttribute("aria-expanded") !== "true";
        toggle.setAttribute("aria-expanded", String(expanded));
        toggle.textContent = expanded ? "Close menu" : "Menu";
        nav.classList.toggle("open", expanded);
      });
    }

    var footer = document.querySelector("[data-site-footer]");
    if (footer) {
      var inner = make("div", "footer-inner");
      var left = document.createElement("div");
      left.appendChild(make("p", "", "Malta trip guide · Research snapshot: 10 October 2026"));
      left.appendChild(make("p", "", "Check source pages and live operator information again before travel; schedules, opening hours and prices can change."));
      var right = document.createElement("div");
      var sourceLink = make("a", "", "Master source log");
      sourceLink.href = "docs/SOURCES.md";
      right.appendChild(sourceLink);
      right.appendChild(document.createTextNode(" · "));
      var questionLink = make("a", "", "Open questions");
      questionLink.href = "docs/OPEN_QUESTIONS.md";
      right.appendChild(questionLink);
      inner.append(left, right);
      footer.replaceChildren(inner);
    }
  }

  function detail(dl, label, value) {
    var wrapper = make("div", "record-detail");
    wrapper.append(make("dt", "", label), make("dd", "", value || "Not published"));
    dl.appendChild(wrapper);
  }

  function appendLinkedText(container, text) {
    var value = String(text || "");
    var urlPattern = /https?:\/\/[^\s<>]+/g;
    var lastIndex = 0;
    var match;
    while ((match = urlPattern.exec(value)) !== null) {
      var rawUrl = match[0];
      var trailing = "";
      while (/[),.;!?]$/.test(rawUrl)) {
        trailing = rawUrl.slice(-1) + trailing;
        rawUrl = rawUrl.slice(0, -1);
      }
      if (match.index > lastIndex) container.appendChild(document.createTextNode(value.slice(lastIndex, match.index)));
      try {
        var parsed = new URL(rawUrl);
        if (parsed.protocol === "http:" || parsed.protocol === "https:") {
          var link = make("a", "", rawUrl);
          link.href = parsed.href;
          link.target = "_blank";
          link.rel = "noopener noreferrer";
          container.appendChild(link);
        } else {
          container.appendChild(document.createTextNode(rawUrl));
        }
      } catch (_error) {
        container.appendChild(document.createTextNode(rawUrl));
      }
      if (trailing) container.appendChild(document.createTextNode(trailing));
      lastIndex = match.index + match[0].length;
    }
    if (lastIndex < value.length) container.appendChild(document.createTextNode(value.slice(lastIndex)));
  }

  function createRecord(record) {
    var article = make("article", "record-card");
    article.dataset.category = record.category;
    var meta = make("div", "record-meta");
    meta.appendChild(make("span", "pill", record.category));
    var confidenceClass = record.confidence === "verified" ? "verified" : (record.confidence === "partially verified" ? "partial" : "unverified");
    meta.appendChild(make("span", "pill " + confidenceClass, record.confidence));
    meta.appendChild(make("span", "small", record.area));
    article.append(meta, make("h3", "", record.name), make("p", "", record.description));

    var dl = make("dl", "record-details");
    detail(dl, "Address / area", record.address && record.address !== "Not published" ? record.address : record.area + " — address not published");
    detail(dl, "Hours / schedule", record.hours);
    detail(dl, "Price", record["price range"]);
    article.appendChild(dl);

    if (record.notes) {
      var notes = make("div", "record-notes");
      notes.appendChild(document.createTextNode("Notes: "));
      appendLinkedText(notes, record.notes);
      article.appendChild(notes);
    }
    if (record.source_url) {
      var source = make("a", "record-source", "Open source ↗");
      source.href = record.source_url;
      source.target = "_blank";
      source.rel = "noopener noreferrer";
      source.setAttribute("aria-label", "Open source for " + record.name + " in a new tab");
      article.appendChild(source);
    } else {
      article.appendChild(make("p", "record-source data-warning", "No direct source URL is available; this record must not be treated as verified."));
    }
    article.appendChild(make("div", "record-source-meta", record.source_type + " · checked " + record.date_checked));
    return article;
  }

  function renderTopic() {
    var host = document.querySelector("[data-topic-data]");
    if (!host) return;
    var sourcePath = host.getAttribute("data-topic-data");
    var loading = make("p", "muted", "Loading source-backed entries…");
    host.replaceChildren(loading);
    fetch(sourcePath).then(function (response) {
      if (!response.ok) throw new Error("Unable to load topic data (" + response.status + ")");
      return response.json();
    }).then(function (data) {
      var title = document.querySelector("[data-topic-title]");
      var intro = document.querySelector("[data-topic-intro]");
      if (title) title.textContent = data.title || data.topic;
      if (intro) intro.textContent = data.intro || "Source-backed entries are listed below.";

      var records = Array.isArray(data.records) ? data.records : [];
      var tools = document.querySelector("[data-topic-tools]");
      var search = tools && tools.querySelector("input[type=search]");
      var select = tools && tools.querySelector("select");
      var count = tools && tools.querySelector("[data-result-count]");
      if (select) {
        Array.from(new Set(records.map(function (r) { return r.category; }))).sort().forEach(function (category) {
          var option = document.createElement("option");
          option.value = category;
          option.textContent = category;
          select.appendChild(option);
        });
      }

      function paint() {
        var query = search ? search.value.trim().toLowerCase() : "";
        var category = select ? select.value : "";
        var filtered = records.filter(function (r) {
          var matchesCategory = !category || r.category === category;
          var haystack = [r.name, r.category, r.area, r.address, r.description, r.hours, r["price range"], r.notes].join(" ").toLowerCase();
          return matchesCategory && (!query || haystack.indexOf(query) !== -1);
        });
        host.replaceChildren();
        if (!filtered.length) {
          host.appendChild(make("p", "empty-state", "No entries match those filters. Clear the search or choose another category."));
        } else {
          var categories = Array.from(new Set(filtered.map(function (r) { return r.category; })));
          categories.forEach(function (name) {
            var group = make("section", "category-section");
            var sectionId = "category-" + name.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
            group.id = sectionId;
            var heading = make("div", "category-heading");
            heading.append(make("h2", "", name), make("span", "category-count", filtered.filter(function (r) { return r.category === name; }).length + " entries"));
            var grid = make("div", "grid");
            filtered.filter(function (r) { return r.category === name; }).forEach(function (record) { grid.appendChild(createRecord(record)); });
            group.append(heading, grid);
            host.appendChild(group);
          });
        }
        if (count) count.textContent = "Showing " + filtered.length + " of " + records.length + " entries";
      }
      if (search) search.addEventListener("input", paint);
      if (select) select.addEventListener("change", paint);
      paint();
    }).catch(function (error) {
      host.replaceChildren(make("p", "callout callout-danger", "Topic data could not be loaded. Please use the source links in the project repository or reload the page. " + error.message));
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    renderShell();
    renderTopic();
  });
})();
