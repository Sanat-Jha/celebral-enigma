document.addEventListener('DOMContentLoaded', function() {
    const hamburgerBtn = document.querySelector('.hamburger-btn');
    const sidebar = document.querySelector('.sidebar');
    const body = document.body;

    // Create overlay element
    const overlay = document.createElement('div');
    overlay.className = 'sidebar-overlay';
    document.body.appendChild(overlay);

    function toggleSidebar() {
        sidebar.classList.toggle('collapsed');
        overlay.classList.toggle('active');
        body.classList.toggle('sidebar-open');
    }

    function closeSidebar() {
        sidebar.classList.remove('collapsed');
        overlay.classList.remove('active');
        body.classList.remove('sidebar-open');
    }

    if (hamburgerBtn && sidebar) {
        hamburgerBtn.addEventListener('click', toggleSidebar);
        
        // Close sidebar when clicking overlay
        overlay.addEventListener('click', closeSidebar);

        // Close on escape key
        document.addEventListener('keydown', function(event) {
            if (event.key === 'Escape') {
                closeSidebar();
            }
        });

        // Handle touch swipe to close
        let touchStartX = 0;
        sidebar.addEventListener('touchstart', function(e) {
            touchStartX = e.touches[0].clientX;
        });

        sidebar.addEventListener('touchmove', function(e) {
            if (!sidebar.classList.contains('collapsed')) return;
            
            const touchX = e.touches[0].clientX;
            const diff = touchStartX - touchX;

            if (diff > 50) { // Swipe left threshold
                closeSidebar();
            }
        });
    }
});