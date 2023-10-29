document.addEventListener('DOMContentLoaded', function() {
    // Load existing posts on page load
    loadPosts();

    // Handle new post submission
    document.getElementById('newPostForm').addEventListener('submit', function(event) {
        event.preventDefault();

        var formData = new FormData(this);

        fetch('/add_post_ajax/', {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Clear form fields
                document.getElementById('id_title').value = '';
                document.getElementById('id_content').value = '';
                document.getElementById('id_judul_buku').value = '';

                // Load updated posts
                loadPosts();
            } else {
                alert('Failed to add post. Please try again.');
            }
        });
    });
});

function loadPosts() {
    var forumPosts = document.getElementById('forumPosts');
    forumPosts.innerHTML = ''; // Clear existing posts

    fetch('/get_posts_json/')
        .then(response => response.json())
        .then(data => {
            data.forEach(post => {
                var postCard = `
                    <div class="col-md-4">
                        <div class="card post-card">
                            <div class="card-body">
                                <h5 class="card-title">${post.title}</h5>
                                <p class="card-text">${post.content}</p>
                                <p class="card-text">${post.judul_buku}</p>
                            </div>
                        </div>
                    </div>
                `;
                forumPosts.innerHTML += postCard;
            });
        });
}

// Function to get CSRF token from cookie
function getCookie(name) {
    var value = '; ' + document.cookie;
    var parts = value.split('; ' + name + '=');
    if (parts.length == 2) return parts.pop().split(';').shift();
}
