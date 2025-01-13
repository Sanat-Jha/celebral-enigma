document.addEventListener('DOMContentLoaded', function () {
    const hamburgerBtn = document.querySelector('.hamburger-btn');
    const sidebar = document.querySelector('.left-sidebar');
    const rightSidebar = document.querySelector('.right-sidebar');
    $(document).ready(function() {
        $('.hamburger-btn').click(function() {
            // Toggle the visibility of both sidebars
            $('.left-sidebar').toggleClass('collapsed');
        });
    });
    
    const postCards = document.querySelectorAll('.post-card');
    postCards.forEach((card, index) => {
        card.style.animationDelay = `${index * 0.2}s`;
        card.classList.remove('hidden');
    });
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
