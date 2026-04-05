async function scrapeUrl() {
    const urlInput = document.getElementById('urlInput');
    const scrapeBtn = document.getElementById('scrapeBtn');
    const btnText = document.getElementById('btnText');
    const btnIcon = document.getElementById('btnIcon');
    const btnLoader = document.getElementById('btnLoader');
    const errorMsg = document.getElementById('errorMsg');
    const resultsSection = document.getElementById('resultsSection');

    const url = urlInput.value.trim();

    // Basic validation
    if (!url) {
        showError('Please enter a valid URL.');
        return;
    }

    // Reset UI
    showError('');
    resultsSection.classList.add('hidden');
    setLoading(true);

    try {
        const response = await fetch('/scrape', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ url: url })
        });

        const data = await response.json();

        if (response.ok) {
            displayResults(data);
        } else {
            showError(data.error || 'Failed to scrape the website.');
        }

    } catch (error) {
        showError('An error occurred. Is the backend running?');
        console.error(error);
    } finally {
        setLoading(false);
    }
}

function displayResults(data) {
    document.getElementById('pageTitle').textContent = data.title;

    const pageUrlLink = document.getElementById('pageUrl');
    pageUrlLink.href = data.url;
    pageUrlLink.textContent = data.url;

    document.getElementById('pageText').textContent = data.text;
    document.getElementById('pageHtml').textContent = data.html;

    const gallery = document.getElementById('imageGallery');
    gallery.innerHTML = '';

    if (data.images && data.images.length > 0) {
        data.images.forEach(src => {
            const img = document.createElement('img');
            img.src = src;
            img.classList.add('image-item');
            img.onclick = () => window.open(src, '_blank');
            gallery.appendChild(img);
        });
    } else {
        gallery.innerHTML = '<p style="color:var(--text-muted)">No images found.</p>';
    }

    document.getElementById('resultsSection').classList.remove('hidden');
}

function showError(msg) {
    const errorEl = document.getElementById('errorMsg');
    errorEl.textContent = msg;
}

function setLoading(isLoading) {
    const scrapeBtn = document.getElementById('scrapeBtn');
    const btnText = document.getElementById('btnText');
    const btnIcon = document.getElementById('btnIcon');
    const btnLoader = document.getElementById('btnLoader');

    scrapeBtn.disabled = isLoading;

    if (isLoading) {
        btnText.style.display = 'none';
        btnIcon.style.display = 'none';
        btnLoader.style.display = 'block';
    } else {
        btnText.style.display = 'block';
        btnIcon.style.display = 'block';
        btnLoader.style.display = 'none';
    }
}

// Allow Enter key to submit
document.getElementById('urlInput').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        scrapeUrl();
    }
});
