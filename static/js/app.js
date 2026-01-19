// Theme Management - Initialize immediately to prevent flash
(function() {
    // Load saved theme immediately
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', savedTheme);
})();

document.addEventListener('DOMContentLoaded', function() {
    // Update theme icon after DOM loads
    const savedTheme = localStorage.getItem('theme') || 'light';
    updateThemeIcon(savedTheme);
    
    // Theme toggle functionality
    const themeToggle = document.getElementById('theme-toggle');
    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            const currentTheme = document.documentElement.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            
            document.documentElement.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            updateThemeIcon(newTheme);
        });
    }
    
    // Flash message auto-hide
    const flashMessages = document.querySelectorAll('.flash-message');
    flashMessages.forEach(function(message) {
        // Auto-hide after 5 seconds
        setTimeout(function() {
            message.style.animation = 'slideOut 0.3s ease forwards';
            setTimeout(function() {
                message.remove();
            }, 300);
        }, 5000);
        
        // Close button functionality
        const closeBtn = message.querySelector('.flash-close');
        if (closeBtn) {
            closeBtn.addEventListener('click', function() {
                message.style.animation = 'slideOut 0.3s ease forwards';
                setTimeout(function() {
                    message.remove();
                }, 300);
            });
        }
    });
});

function updateThemeIcon(theme) {
    const themeToggle = document.getElementById('theme-toggle');
    if (themeToggle) {
        const icon = themeToggle.querySelector('i');
        if (theme === 'dark') {
            icon.className = 'fas fa-sun';
        } else {
            icon.className = 'fas fa-moon';
        }
    }
}

// Cart Management
function addToCart(dishId, quantity = 1) {
    fetch('/add-to-cart', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            dish_id: dishId,
            quantity: quantity
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            showMessage('Item added to cart!', 'success');
            updateCartCount();
        } else {
            showMessage(data.message, 'error');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        showMessage('An error occurred. Please try again.', 'error');
    });
}

function updateCartCount() {
    // This would typically update a cart count badge in the navbar
    // For now, we'll just log it
    console.log('Cart updated');
}

function showMessage(message, type) {
    // Create flash message element
    const flashContainer = document.querySelector('.flash-messages') || createFlashContainer();
    
    const messageElement = document.createElement('div');
    messageElement.className = `flash-message flash-${type}`;
    messageElement.innerHTML = `
        ${message}
        <button class="flash-close">&times;</button>
    `;
    
    flashContainer.appendChild(messageElement);
    
    // Add close functionality
    const closeBtn = messageElement.querySelector('.flash-close');
    closeBtn.addEventListener('click', function() {
        messageElement.style.animation = 'slideOut 0.3s ease forwards';
        setTimeout(function() {
            messageElement.remove();
        }, 300);
    });
    
    // Auto-hide after 5 seconds
    setTimeout(function() {
        if (messageElement.parentNode) {
            messageElement.style.animation = 'slideOut 0.3s ease forwards';
            setTimeout(function() {
                messageElement.remove();
            }, 300);
        }
    }, 5000);
}

function createFlashContainer() {
    const container = document.createElement('div');
    container.className = 'flash-messages';
    document.body.appendChild(container);
    return container;
}

// Form Validation
function validateForm(formId) {
    const form = document.getElementById(formId);
    if (!form) return true;
    
    const requiredFields = form.querySelectorAll('[required]');
    let isValid = true;
    
    requiredFields.forEach(function(field) {
        if (!field.value.trim()) {
            field.style.borderColor = '#e74c3c';
            isValid = false;
        } else {
            field.style.borderColor = '';
        }
    });
    
    return isValid;
}

// Image Preview for File Uploads
function setupImagePreview() {
    const imageInputs = document.querySelectorAll('input[type="file"][accept*="image"]');
    
    imageInputs.forEach(function(input) {
        input.addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    // Create or update preview image
                    let preview = input.parentNode.querySelector('.image-preview');
                    if (!preview) {
                        preview = document.createElement('img');
                        preview.className = 'image-preview';
                        preview.style.cssText = 'max-width: 200px; max-height: 200px; margin-top: 10px; border-radius: 5px;';
                        input.parentNode.appendChild(preview);
                    }
                    preview.src = e.target.result;
                };
                reader.readAsDataURL(file);
            }
        });
    });
}

// Initialize image preview on page load
document.addEventListener('DOMContentLoaded', setupImagePreview);

// Smooth scrolling for anchor links
document.addEventListener('DOMContentLoaded', function() {
    const anchorLinks = document.querySelectorAll('a[href^="#"]');
    
    anchorLinks.forEach(function(link) {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
});

// Search functionality with debouncing
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = function() {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Setup search with debouncing
document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.querySelector('.search-input');
    if (searchInput) {
        const debouncedSearch = debounce(function() {
            // Auto-submit search form after user stops typing
            const form = searchInput.closest('form');
            if (form) {
                form.submit();
            }
        }, 500);
        
        searchInput.addEventListener('input', debouncedSearch);
    }
});

// Confirmation dialogs
function confirmAction(message) {
    return confirm(message || 'Are you sure you want to perform this action?');
}

// Setup confirmation dialogs for delete actions
document.addEventListener('DOMContentLoaded', function() {
    const deleteButtons = document.querySelectorAll('[data-confirm]');
    
    deleteButtons.forEach(function(button) {
        button.addEventListener('click', function(e) {
            const message = this.getAttribute('data-confirm');
            if (!confirmAction(message)) {
                e.preventDefault();
            }
        });
    });
});

// Loading states for buttons
function setButtonLoading(button, loading = true) {
    if (loading) {
        button.disabled = true;
        button.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Loading...';
    } else {
        button.disabled = false;
        button.innerHTML = button.getAttribute('data-original-text') || 'Submit';
    }
}

// Setup loading states for forms
document.addEventListener('DOMContentLoaded', function() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(function(form) {
        form.addEventListener('submit', function() {
            const submitButton = form.querySelector('button[type="submit"]');
            if (submitButton) {
                submitButton.setAttribute('data-original-text', submitButton.innerHTML);
                setButtonLoading(submitButton, true);
            }
        });
    });
});

// Quantity controls for dish detail page
function increaseQuantity() {
    const input = document.getElementById('quantity');
    if (input) {
        const max = parseInt(input.getAttribute('max'));
        const current = parseInt(input.value);
        if (current < max) {
            input.value = current + 1;
        }
    }
}

function decreaseQuantity() {
    const input = document.getElementById('quantity');
    if (input) {
        const current = parseInt(input.value);
        if (current > 1) {
            input.value = current - 1;
        }
    }
}

// Tab functionality for dashboard
function showTab(tabName) {
    // Hide all tab contents
    const tabContents = document.querySelectorAll('.tab-content');
    tabContents.forEach(tab => tab.classList.remove('active'));
    
    // Remove active class from all tab buttons
    const tabBtns = document.querySelectorAll('.tab-btn');
    tabBtns.forEach(btn => btn.classList.remove('active'));
    
    // Show selected tab content
    const targetTab = document.getElementById(tabName + '-tab');
    if (targetTab) {
        targetTab.classList.add('active');
    }
    
    // Add active class to clicked button
    const clickedBtn = event ? event.target : document.querySelector(`[onclick="showTab('${tabName}')"]`);
    if (clickedBtn) {
        clickedBtn.classList.add('active');
    }
}

// Add slideOut animation to CSS
const style = document.createElement('style');
style.textContent = `
    @keyframes slideOut {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);