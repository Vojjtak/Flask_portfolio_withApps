$(function() {
    $("#download").hide();

    $("#search-form").submit(function(event) {
        event.preventDefault();

        var url = $("#url-input").val();

        $.ajax({
            url: '/get_title',
            type: 'POST',
            data: {url: url},
            success: function(response) {
                var title = response.title;
                var thumbnail = response.thumbnail;
                $("#title").text(title).show();
                $("#thumbnail").attr("src", thumbnail).show();

                $("#download").show();
            },
            error: function(error) {
                console.log("Error fetching title:", error);
            }

        });
    });
});