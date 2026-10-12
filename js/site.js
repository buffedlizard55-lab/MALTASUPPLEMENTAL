/* MALTASUPPLEMENTAL — accessible, dependency-free shared navigation and JSON page renderer. */
(function () {
  "use strict";

  var NAV = [
    ["index.html", "Overview"],
    ["event.html", "Event desk"],
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
    var skip = make("a", "skip-link", "Skip to main content");
    skip.href = "#main-content";
    document.body.prepend(skip);
    var main = document.querySelector("main");
    if (main) main.id = "main-content";
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
      document.addEventListener("keydown", function (event) {
        if (event.key === "Escape" && toggle.getAttribute("aria-expanded") === "true") {
          toggle.click();
          toggle.focus();
        }
      });
    }

    var footer = document.querySelector("[data-site-footer]");
    if (footer) {
      var inner = make("div", "footer-inner");
      var left = document.createElement("div");
      left.appendChild(make("p", "", "Malta trip guide · Critical refresh: 12 October 2026 · Individual source dates vary"));
      left.appendChild(make("p", "", "Check source pages and live operator information again before travel; schedules, opening hours and prices can change."));
      var right = document.createElement("div");
      var sourceLink = make("a", "", "Master source log");
      sourceLink.href = "sources.html#source-reader";
      right.appendChild(sourceLink);
      right.appendChild(document.createTextNode(" · "));
      var questionLink = make("a", "", "Open questions");
      questionLink.href = "sources.html#question-reader";
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
    article.id = record.id;
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
      var notes = make("details", "record-notes");
      notes.appendChild(make("summary", "", "Evidence & caveats"));
      var noteText = make("p");
      notes.appendChild(noteText);
      appendLinkedText(noteText, record.notes);
      article.appendChild(notes);
    }
    if (record.source_url) {
      var source = make("a", "record-source", "Open source ↗");
      source.href = record.source_url;
      source.target = "_blank";
      source.rel = "noopener noreferrer";
      source.setAttribute("aria-label", "Open source for " + record.name + " in a new tab");
      article.appendChild(source);
      var permalink = make("a", "record-source", "Link to this entry");
      permalink.href = "#" + record.id;
      article.appendChild(permalink);
    } else {
      article.appendChild(make("p", "record-source data-warning", "No direct source URL is available; this record must not be treated as verified."));
    }
    article.appendChild(make("div", "record-source-meta", record.source_type + " · checked " + record.date_checked));
    return article;
  }

  function revealTarget(target) {
    if (!target) return;
    // Canonical deep links may point into a collapsed evidence disclosure.
    for (var parent = target.parentElement; parent; parent = parent.parentElement) {
      if (parent.tagName === "DETAILS") parent.open = true;
    }
    target.scrollIntoView();
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

      function filterControl(labelText, values, attribute) {
        var label = make("label", "", labelText);
        var control = make("select");
        control.setAttribute(attribute, "");
        var all = make("option", "", "All " + labelText.toLowerCase());
        all.value = "";
        control.appendChild(all);
        values.forEach(function (value) {
          var option = make("option", "", value);
          option.value = value;
          control.appendChild(option);
        });
        label.appendChild(control);
        if (tools) tools.insertBefore(label, count);
        return control;
      }
      var area = filterControl("Areas", Array.from(new Set(records.map(function (r) { return r.area; }))).sort(), "data-area-filter");
      var confidence = filterControl("Confidence", ["verified", "partially verified", "unverified"], "data-confidence-filter");
      var reset = make("button", "filter-reset", "Reset filters");
      reset.type = "button";
      if (tools) tools.appendChild(reset);
      reset.addEventListener("click", function () {
        if (search) search.value = "";
        if (select) select.value = "";
        area.value = "";
        confidence.value = "";
        paint();
      });
      var jumps = make("div", "quick-links category-jumps");
      jumps.setAttribute("aria-label", "Jump to a category");
      if (tools) tools.after(jumps);

      function paint() {
        var query = search ? search.value.trim().toLowerCase() : "";
        var category = select ? select.value : "";
        var filtered = records.filter(function (r) {
          var matchesCategory = !category || r.category === category;
          var haystack = [r.name, r.category, r.area, r.address, r.description, r.hours, r["price range"], r.notes].join(" ").toLowerCase();
          return matchesCategory && (!area.value || r.area === area.value) && (!confidence.value || r.confidence === confidence.value) && (!query || haystack.indexOf(query) !== -1);
        });
        host.replaceChildren();
        jumps.replaceChildren();
        if (!filtered.length) {
          host.appendChild(make("p", "empty-state", "No entries match those filters. Clear the search or choose another category."));
        } else {
          var categories = Array.from(new Set(filtered.map(function (r) { return r.category; })));
          categories.forEach(function (name) {
            var group = make("section", "category-section");
            var sectionId = "category-" + name.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
            group.id = sectionId;
            var jump = make("a", "", name);
            jump.href = "#" + sectionId;
            jumps.appendChild(jump);
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
      area.addEventListener("change", paint);
      confidence.addEventListener("change", paint);
      paint();
      function followHash() {
        var id;
        try { id = decodeURIComponent(window.location.hash.slice(1)); } catch (_error) { return; }
        if (records.some(function (r) { return r.id === id; }) && !document.getElementById(id)) {
          if (search) search.value = "";
          if (select) select.value = "";
          area.value = "";
          confidence.value = "";
          paint();
        }
        var target = document.getElementById(id);
        revealTarget(target);
      }
      followHash();
      window.addEventListener("hashchange", followHash);
    }).catch(function (error) {
      host.replaceChildren(make("p", "callout callout-danger", "Topic data could not be loaded. Please use the source links in the project repository or reload the page. " + error.message));
    });
  }

  function renderDocuments() {
    document.querySelectorAll("[data-document]").forEach(function (host) {
      fetch(host.dataset.document).then(function (response) {
        if (!response.ok) throw new Error("HTTP " + response.status);
        return response.text();
      }).then(function (text) {
        host.replaceChildren();
        var body = make("div", "document-text");
        appendLinkedText(body, text);
        host.appendChild(body);
      }).catch(function () {
        host.textContent = "Document could not load. Use the GitHub or raw-document links above.";
      });
    });
  }

  var topicRequests = new Map();
  function loadTopic(topic) {
    if (!topicRequests.has(topic)) topicRequests.set(topic, fetch("data/" + topic + ".json").then(function (response) {
      if (!response.ok) throw new Error("HTTP " + response.status);
      return response.json();
    }));
    return topicRequests.get(topic);
  }

  function summaryCard(record, topicPage, label, field) {
    var card = make("article", "card");
    card.dataset.recordRef = record.id;
    card.append(make("span", "card-tag", label), make("h3", "", record.name), make("p", "", record[field || "description"]));
    var source = make("a", "", "Evidence & details →");
    source.href = topicPage + "#" + record.id;
    card.append(source, make("p", "small", "Checked " + record.date_checked + " · " + record.confidence));
    return card;
  }

  function renderOverview() {
    var host = document.querySelector("[data-overview]");
    if (!host) return;
    var specs = [
      ["activities", "ax-odycy-base-hotel", "activities.html", "Your base"],
      ["activities", "twc-finals-2026", "event.html", "Before the event"],
      ["transport", "mode-comparison-summary", "getting-around.html", "Choose a mode"],
      ["food", "espresso-odycy", "restaurants.html", "At the hotel"],
      ["everyday", "malta-electricity", "everyday.html", "Pack first"],
      ["radio", "radio-research-status", "radio.html", "Receiver, not stream"]
    ];
    specs.forEach(function (spec) {
      var slot = make("div", "summary-slot");
      slot.textContent = "Loading " + spec[3].toLowerCase() + "…";
      host.appendChild(slot);
      loadTopic(spec[0]).then(function (data) {
        var record = data.records.find(function (r) { return r.id === spec[1]; });
        if (!record) throw new Error("Record missing");
        slot.replaceWith(summaryCard(record, spec[2], spec[3]));
      }).catch(function () {
        slot.className = "card callout-danger";
        slot.replaceChildren(make("h3", "", spec[3]), make("p", "", "Summary unavailable; open the topic guide or try again."));
        var link = make("a", "", "Open guide →");
        link.href = spec[2];
        slot.appendChild(link);
      });
    });
  }

  function renderRecordLists() {
    document.querySelectorAll("[data-record-list]").forEach(function (host) {
      var ids = host.dataset.ids.split(/\s+/).filter(Boolean);
      loadTopic(host.dataset.recordList).then(function (data) {
        var records = ids.map(function (id) {
          var record = data.records.find(function (r) { return r.id === id; });
          if (!record) throw new Error("Record missing: " + id);
          return record;
        });
        host.replaceChildren();
        records.forEach(function (record) { host.appendChild(createRecord(record)); });
        var target;
        try { target = document.getElementById(decodeURIComponent(window.location.hash.slice(1))); } catch (_error) { return; }
        revealTarget(target);
      }).catch(function () {
        host.replaceChildren(make("p", "callout callout-danger", "These entries could not be loaded. Reload or use the topic guide and source data."));
      });
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    renderShell();
    renderTopic();
    renderDocuments();
    renderOverview();
    renderRecordLists();
  });
})();
