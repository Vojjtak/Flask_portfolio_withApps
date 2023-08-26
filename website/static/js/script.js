$(function() {
    $("#download").hide();

    $("#search-form").submit(function(event) {
        event.preventDefault();
        var url = $("#url-input").val();

        fetchTitleAndThumbnail(url)
            .then(function(response) {
                var title = response.title;
                var thumbnail = response.thumbnail;
                $("#title").text(title).show();
                $("#thumbnail").attr("src", thumbnail).show();
                $("#download").show();

                // Set the URL in the hidden input field
                $("#hidden_url").val(url);
            })
            .catch(function(error) {
                console.log("An error occurred:", error);
            });
    });

    $("#download-button").click(function(event) {
        event.preventDefault();
        var url = $("#url-input").val(); // Get the URL from the hidden input
        downloadVideo(url);
    });
});


function fetchTitleAndThumbnail(url) {
    return $.ajax({
        url: '/get_title',
        type: 'POST',
        data: {url: url}
    });
}

function downloadVideo(url) {
    $.ajax({
        url: '/download',
        type: 'POST',
        data: {url: url},
        success: function(response) {
            var video = response.video;
            console.log("Downloaded video:", video);
        },
        error: function(error) {
            console.log("Error downloading video:", error);
        }
    });
}

