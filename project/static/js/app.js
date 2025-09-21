document.addEventListener('DOMContentLoaded', () => {
  // Student form handler
  const uploadForm = document.getElementById('uploadForm');
  if (uploadForm) {
    const spinner = document.getElementById('uploadSpinner');
    const resultEl = document.getElementById('result');
    const scoreBar = document.getElementById('scoreBar');
    const verdictEl = document.getElementById('verdict');
    const matchedBadges = document.getElementById('matchedBadges');
    const missingBadges = document.getElementById('missingBadges');
    const feedbackEl = document.getElementById('feedback');

    uploadForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const formData = new FormData(uploadForm);
      try {
        spinner && spinner.classList.remove('d-none');
        resultEl && resultEl.classList.add('d-none');

        const response = await fetch('/api/evaluate', {
          method: 'POST',
          body: formData,
        });
        const data = await response.json();

        const score = Math.max(0, Math.min(100, Number(data.score || 0)));
        if (scoreBar) {
          scoreBar.style.width = `${score}%`;
          scoreBar.classList.remove('bg-success', 'bg-warning', 'bg-danger');
          if (score >= 80) scoreBar.classList.add('bg-success');
          else if (score >= 50) scoreBar.classList.add('bg-warning');
          else scoreBar.classList.add('bg-danger');
        }
        if (verdictEl) verdictEl.textContent = data.verdict || '';
        if (matchedBadges) {
          const matched = Array.isArray(data.matched) ? data.matched : [];
          matchedBadges.innerHTML = matched
            .slice(0, 50)
            .map(k => `<span class="badge bg-success">${k}</span>`) 
            .join(' ');
        }
        if (missingBadges) {
          const missing = Array.isArray(data.missing) ? data.missing : [];
          missingBadges.innerHTML = missing
            .slice(0, 50)
            .map(k => `<span class="badge bg-danger">${k}</span>`) 
            .join(' ');
        }
        if (feedbackEl) feedbackEl.textContent = data.feedback || '';

        resultEl && resultEl.classList.remove('d-none');
      } catch (err) {
        alert('Failed to evaluate files. Please try again.');
      } finally {
        spinner && spinner.classList.add('d-none');
      }
    });
  }

  // Admin login handler
  const adminLogin = document.getElementById('adminLogin');
  if (adminLogin) {
    const spinner = document.getElementById('loginSpinner');
    const statusEl = document.getElementById('loginStatus');

    adminLogin.addEventListener('submit', async (e) => {
      e.preventDefault();
      const username = document.getElementById('username').value.trim();
      const password = document.getElementById('password').value;
      try {
        spinner && spinner.classList.remove('d-none');
        statusEl && (statusEl.innerHTML = '');
        const resp = await fetch('/api/admin-login', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ username, password }),
        });
        const data = await resp.json();
        if (data.status === 'success' && data.redirect) {
          window.location.href = data.redirect;
        } else {
          statusEl && (statusEl.innerHTML = '<div class="text-danger">Invalid credentials</div>');
        }
      } catch (err) {
        statusEl && (statusEl.innerHTML = '<div class="text-danger">Login failed. Try again.</div>');
      } finally {
        spinner && spinner.classList.add('d-none');
      }
    });
  }
});
