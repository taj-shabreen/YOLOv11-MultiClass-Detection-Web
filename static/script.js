const dropZone = document.getElementById('drop-zone');
const fileInput = document.getElementById('file-input');
const form = document.getElementById('upload-form');
const loader = document.getElementById('loader');

// Drop zone click opens file selector
dropZone.addEventListener('click', () => fileInput.click());

// Drag styling
dropZone.addEventListener('dragover', (e) => {
  e.preventDefault();
  dropZone.classList.add('dragover');
});

dropZone.addEventListener('dragleave', () => {
  dropZone.classList.remove('dragover');
});

// Drop upload
dropZone.addEventListener('drop', (e) => {
  e.preventDefault();
  dropZone.classList.remove('dragover');
  const file = e.dataTransfer.files[0];
  if (file) {
    uploadAndPreview(file);
  }
});

fileInput.addEventListener('change', () => {
  if (fileInput.files.length > 0) {
    uploadAndPreview(fileInput.files[0]);
  }
});

function uploadAndPreview(file) {
  loader.style.display = 'block';

  const formData = new FormData();
  formData.append('image', file);

  fetch('/', {
    method: 'POST',
    body: formData
  })
    .then(res => res.text())
    .then(html => {
      document.open();
      document.write(html);
      document.close();
    });
}
