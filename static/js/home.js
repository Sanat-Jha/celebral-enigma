document.addEventListener('DOMContentLoaded', function() {
    const hamburgerBtn = document.querySelector('.hamburger-btn');
    const sidebar = document.querySelector('.left-sidebar');
    const body = document.body;
    
    // Create and append overlay
    const overlay = document.createElement('div');
    overlay.className = 'sidebar-overlay';
    body.appendChild(overlay);
    
    // Create and append close button to sidebar
    const closeBtn = document.createElement('button');
    closeBtn.className = 'close-sidebar';
    closeBtn.innerHTML = '×';
    
    // Create header div for sidebar
    const sidebarHeader = document.createElement('div');
    sidebarHeader.className = 'sidebar-header';
    sidebarHeader.appendChild(closeBtn);
    
    // Insert header at the beginning of sidebar
    sidebar.insertBefore(sidebarHeader, sidebar.firstChild);
    
    // Toggle sidebar
    function toggleSidebar() {
        sidebar.classList.toggle('collapsed');
        body.classList.toggle('sidebar-open');
        overlay.classList.toggle('active');
    }
    
    // Close sidebar
    function closeSidebar() {
        sidebar.classList.remove('collapsed');
        body.classList.remove('sidebar-open');
        overlay.classList.remove('active');
    }
    
    // Event listeners
    hamburgerBtn.addEventListener('click', toggleSidebar);
    closeBtn.addEventListener('click', closeSidebar);
    overlay.addEventListener('click', closeSidebar);
    
    // Close sidebar on escape key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') closeSidebar();
    });
    
    // Handle touch events for swipe to close
    let touchStartX = 0;
    let touchEndX = 0;
    
    sidebar.addEventListener('touchstart', (e) => {
        touchStartX = e.changedTouches[0].screenX;
    }, false);
    
    sidebar.addEventListener('touchend', (e) => {
        touchEndX = e.changedTouches[0].screenX;
        handleSwipe();
    }, false);
    
    function handleSwipe() {
        const swipeThreshold = 100;
        if (touchStartX - touchEndX > swipeThreshold) {
            closeSidebar();
        }
    }
});

$('#subscribe-form').on('submit', function (e) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: 'newsubscribe',
        data: {
            name: $('#subscriber-name').val(),
            email: $('#subscriber-email').val(),
            csrfmiddlewaretoken: csrfToken,
        },
        success: function () {
            alert('Subscribed Successfully.');
            $('#subscriber-name').val('');
            $('#subscriber-email').val('');
        },
        error: function (xhr) {
            if (xhr.responseJSON && xhr.responseJSON.error) {
                alert(xhr.responseJSON.error === 'Already subscribed.' ? 'Already Subscribed.' : 'An error occurred.');
            } else {
                console.log('An error occurred.');
            }
        },
    });
});
