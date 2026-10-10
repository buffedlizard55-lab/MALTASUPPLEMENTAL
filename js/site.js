/* Malta Field Guide shared behavior: accessible mobile navigation and JSON fact cards. */
(() => {
  'use strict';

  function setupNavigation() {
    const toggle = document.querySelector('.nav-toggle');
    const nav = document.querySelector('.primary-nav');
    if (!toggle || !nav) return;

    const setOpen = (open) => {
      toggle.setAttribute('aria-expanded', String(open));
      toggle.setAttribute('aria-label', open ? 'Close main navigation' : 'Open main navigation');
      nav.classList.toggle('open', open);
    };

    toggle.setAttribute('aria-label', 'Open main navigation');
    toggle.addEventListener('click', () => {
      setOpen(toggle.getAttribute('aria-expanded') !== 'true');
    });
    nav.addEventListener('click', (event) => {
      if (event.target.closest('a')) setOpen(false);
    });
    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
        setOpen(false);
        toggle.focus();
      }
    });
    document.addEventListener('click', (event) => {
      if (toggle.getAttribute('aria-expanded') === 'true' &&
          !nav.contains(event.target) && !toggle.contains(event.target)) {
        setOpen(false);
      }
    });
  }

  function make(tag, className, text) {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (text !== undefined && text !== null) node.textContent = String(text);
    return node;
  }

  function safeHttpUrl(value) {
    try {
      const url = new URL(value, document.baseURI);
      return url.protocol === 'https:' || url.protocol === 'http:' ? url.href : null;
    } catch (_) {
      return null;
    }
  }

  function addFact(parent, label, value) {
    if (!value || String(value).trim() === '') return;
    const row = make('div', 'record-fact');
    const strong = make('strong', '', `${label}: `);
    row.append(strong, document.createTextNode(String(value)));
    parent.append(row);
  }

  function humanDate(iso) {
    if (!/^\d{4}-\d{2}-\d{2}$/.test(iso || '')) return iso || 'Date not recorded';
    const date = new Date(`${iso}T00:00:00Z`);
    return `Checked ${new Intl.DateTimeFormat('en-GB', { day: 'numeric', month: 'short', year: 'numeric', timeZone: 'UTC' }).format(date)}`;
  }

  function makeRecordCard(record) {
    const article = make('article', 'record-card');
    const safeId = String(record.id || '').replace(/[^a-zA-Z0-9_-]/g, '-');
    if (safeId) article.id = safeId;

    const header = make('header', 'record-card-head');
    const headingGroup = document.createElement('div');
    headingGroup.append(make('span', 'record-category', record.category || 'Guide listing'));
    headingGroup.append(make('h3', '', record.name || 'Untitled record'));
    header.append(headingGroup);

    const confidence = String(record.confidence || 'unverified').toLowerCase();
    const confidenceClass = confidence.replace(/[^a-z]+/g, '-').replace(/^-|-$/g, '') || 'unverified';
    header.append(make('span', `confidence-badge confidence-${confidenceClass}`, confidence));
    article.append(header);

    if (record.area) article.append(make('p', 'record-area', record.area));
    if (record['price range']) {
      const price = make('p', 'record-price');
      price.append(make('strong', '', 'Price / range: '));
      price.append(document.createTextNode(String(record['price range'])));
      article.append(price);
    }
    if (record.description) article.append(make('p', 'record-description', record.description));

    const facts = make('div', 'record-facts');
    addFact(facts, 'Address', record.address);
    addFact(facts, 'Hours / date', record.hours);
    if (facts.childElementCount) article.append(facts);

    const footer = make('footer', 'record-card-footer');
    footer.append(make('span', '', humanDate(record.date_checked)));
    footer.append(make('span', 'source-kind', record.source_type || 'source type not recorded'));
    article.append(footer);

    const sourceUrl = safeHttpUrl(record.source_url);
    if (sourceUrl) {
      const link = make('a', 'source-link', 'Open cited source ↗');
      link.href = sourceUrl;
      link.target = '_blank';
      link.rel = 'noopener noreferrer';
      article.append(link);
    }

    if (record.notes) {
      const details = make('details', 'record-notes');
      details.append(make('summary', '', 'Source note & caveats'));
      details.append(make('p', '', record.notes));
      article.append(details);
    }
    return article;
  }

  async function renderRecordList(container) {
    const source = container.dataset.recordSource;
    if (!source) return;
    container.setAttribute('aria-busy', 'true');

    try {
      const response = await fetch(new URL(source, document.baseURI), { credentials: 'same-origin' });
      if (!response.ok) throw new Error(`Source returned ${response.status}`);
      const records = await response.json();
      if (!Array.isArray(records)) throw new Error('The data file is not a JSON record array.');

      const requested = (container.dataset.recordFilter || '')
        .split(',').map((value) => value.trim()).filter(Boolean);
      const byId = new Map(records.map((record) => [String(record.id), record]));
      const selected = requested.length ? requested.map((id) => byId.get(id)).filter(Boolean) : records;
      const missing = requested.filter((id) => !byId.has(id));
      container.replaceChildren();

      if (!selected.length) {
        container.append(make('p', 'empty-state', 'No matching source records were found. Please check the source file and page filter.'));
      } else {
        selected.forEach((record) => container.append(makeRecordCard(record)));
      }
      if (missing.length) {
        const alert = make('p', 'load-error', `Source records not found: ${missing.join(', ')}. This page needs an integration review.`);
        alert.setAttribute('role', 'status');
        container.append(alert);
      }
    } catch (error) {
      container.replaceChildren();
      const message = make('p', 'load-error', `This source list could not be loaded (${error.message}). Open the guide through a web server or GitHub Pages rather than as a local file.`);
      message.setAttribute('role', 'status');
      container.append(message);
    } finally {
      container.removeAttribute('aria-busy');
    }
  }

  setupNavigation();
  document.querySelectorAll('[data-record-source]').forEach((container) => renderRecordList(container));
})();
