(() => {
  const root = document.documentElement;
  const toggle = document.querySelector('#theme-toggle');
  const syncTheme = () => {
    const dark = root.dataset.theme === 'dark';
    toggle.setAttribute('aria-pressed', String(dark));
    toggle.setAttribute('aria-label', `Switch to ${dark ? 'light' : 'dark'} theme`);
    toggle.title = `Switch to ${dark ? 'light' : 'dark'} theme`;
    document.querySelector('meta[name="theme-color"]').content = dark ? '#14151d' : '#faf9f6';
  };
  toggle.hidden = false;
  syncTheme();
  toggle.addEventListener('click', () => {
    root.dataset.theme = root.dataset.theme === 'dark' ? 'light' : 'dark';
    try { localStorage.setItem('kaiming-theme', root.dataset.theme); } catch {}
    syncTheme();
  });
  const revealTarget = () => {
    if (!location.hash) return;
    let id;
    try { id = decodeURIComponent(location.hash.slice(1)); } catch { return; }
    const target = document.getElementById(id);
    const closed = target?.closest('details:not([open])');
    if (closed) { closed.open = true; target.scrollIntoView(); }
  };
  revealTarget();
  window.addEventListener('hashchange', revealTarget);
  document.querySelectorAll('.copy-citation').forEach(button => {
    button.addEventListener('click', async () => {
      const pre = button.parentElement.querySelector('pre');
      try {
        if (!navigator.clipboard) throw new Error('Clipboard unavailable');
        await navigator.clipboard.writeText(pre.textContent);
        button.textContent = 'Copied';
        document.querySelector('#status-message').textContent = 'Citation copied to clipboard.';
        setTimeout(() => { button.textContent = 'Copy citation'; }, 1800);
      } catch {
        const range = document.createRange();
        range.selectNodeContents(pre);
        const selection = window.getSelection();
        selection.removeAllRanges(); selection.addRange(range);
        button.textContent = 'Selected — press Ctrl/Cmd+C';
        document.querySelector('#status-message').textContent = 'Citation selected. Press Control C or Command C to copy.';
      }
    });
  });
})();
