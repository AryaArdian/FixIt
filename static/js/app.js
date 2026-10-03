// Mobile menu
const btn = document.getElementById('menu-btn');
btn?.addEventListener('click', () => {
  const open = document.getElementById('menu').classList.toggle('hidden') === false;
  btn.setAttribute('aria-expanded', open);
  btn.textContent = open ? '✕' : '☰';
});

// Photo preview + file name
const photo = document.getElementById('photo');
const preview = document.getElementById('preview');
const dzText = document.getElementById('dz-text');
photo?.addEventListener('change', () => {
  const file = photo.files[0];
  if (!file) { preview.classList.add('hidden'); dzText.textContent = 'Tap to add a photo'; return; }
  preview.src = URL.createObjectURL(file);
  preview.classList.remove('hidden');
  dzText.textContent = file.name;
});

// Loading state while diagnosing
const form = document.getElementById('diag-form');
form?.addEventListener('submit', () => {
  const b = form.querySelector('button[type=submit]');
  b.disabled = true;
  b.textContent = 'Analyzing…';
});
