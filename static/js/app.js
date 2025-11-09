// AJAX functionality for real-time fruit price updates
document.addEventListener('DOMContentLoaded', function() {
    const searchButtons = document.querySelectorAll('.search-btn');
    const messageContainer = document.getElementById('message-container');
    
    searchButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            
            const fruitId = this.dataset.fruitId;
            const fruitName = this.dataset.fruitName;
            const fruitCard = this.closest('.fruit-card');
            
            // Disable button and show loading state
            this.disabled = true;
            this.innerHTML = '<span class="spinner-border spinner-border-sm"></span> Searching...';
            
            // Add searching animation to card
            fruitCard.classList.add('searching');
            
            // Get CSRF token
            const csrfToken = getCookie('csrftoken');
            
            // Make AJAX request
            fetch(`/search/${fruitId}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Update price with animation
                    const priceElement = fruitCard.querySelector('.price-value');
                    priceElement.textContent = `₹${data.new_price}`;
                    priceElement.classList.add('price-updated');
                    
                    // Update search count badge
                    const badge = fruitCard.querySelector('.badge');
                    badge.textContent = `${data.search_count}/5`;
                    
                    // Update badge color based on search count
                    if (data.search_count >= 5) {
                        badge.classList.remove('bg-info');
                        badge.classList.add('bg-danger');
                    }
                    
                    // Show success message
                    showMessage(data.message, 'success');
                    
                    // Reload page to update history (or use AJAX to update history section)
                    setTimeout(() => {
                        location.reload();
                    }, 1500);
                    
                } else {
                    showMessage('Error updating price. Please try again.', 'danger');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                showMessage('Network error. Please try again.', 'danger');
            })
            .finally(() => {
                // Remove animation and re-enable button
                setTimeout(() => {
                    fruitCard.classList.remove('searching');
                    this.disabled = false;
                    this.innerHTML = 'Search';
                }, 500);
            });
        });
    });
    
    // Function to show messages
    function showMessage(message, type) {
        const alertDiv = document.createElement('div');
        alertDiv.className = `alert alert-${type} alert-dismissible fade show`;
        alertDiv.role = 'alert';
        alertDiv.innerHTML = `
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        `;
        
        messageContainer.innerHTML = '';
        messageContainer.appendChild(alertDiv);
        
        // Auto-dismiss after 5 seconds
        setTimeout(() => {
            alertDiv.classList.remove('show');
            setTimeout(() => alertDiv.remove(), 150);
        }, 5000);
    }
    
    // Function to get CSRF token from cookies
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    
    // Add click animation to fruit cards
    const fruitCards = document.querySelectorAll('.fruit-card');
    fruitCards.forEach(card => {
        card.addEventListener('click', function(e) {
            // Only trigger if clicking on the card itself, not the button
            if (!e.target.classList.contains('search-btn') && !e.target.closest('.search-btn')) {
                const button = this.querySelector('.search-btn');
                if (button && !button.disabled) {
                    button.click();
                }
            }
        });
    });
});
