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
                $("#download").fadeIn(500);

                $("#hidden_url").val(url);
            })
            .catch(function(error) {
                console.log("An error occurred:", error);
            });
    });

    $(document).ready(function() {
        $("#image_name").click(function() {
            $.ajax({
                type: "POST",
                url: "/get_img_path",
                success: function(response) {
                    var name = response.image_name;
                    $("#img_result").attr("src", "/static/temp/" +  name).show();

                },
                error: function() {
                    $("#imagePathResult").text("Error getting image path.");
                }
            });
        });
    });

    $("#download-button").click(function(event) {
        event.preventDefault();
        var url = $("#url-input").val();
        downloadVideo(url);
    });
});


function fetchImgPath(image_path) {
    return $.ajax({
        url: '/get_title',
        type: 'POST',
        data: {url: url}
    });
}

function fetchTitleAndThumbnail(url) {
    return $.ajax({
        url: '/get_title',
        type: 'POST',
        data: {url: url}
    });
}

function showImage(image) {
    return $.ajax({
    image : '/choose_image',
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

  function email_sent_message() {
           var formData = {

            nameinput: $("input[name=nameinput]").val(),
            emailinput: $("input[name=emailinput]").val(),
            messageinput: $("textarea[name=messageinput]").val()
            };

            $.ajax({
                url: "/contact_sent",
                type: 'POST',
                data: formData,  // Send the form data
                success: function(response) {
                    var sent = response.sent;
                    $("#sent").text(sent).fadeIn(500);
                },
                error: function(error) {
                    console.log("Error sending email:", error);
                }
            });
        }

$(document).ready(function() {
    $("#sendEmailButton").click(function() {
        email_sent_message();
    });
});

$(document).ready(function() {
    $(".dropdown").hover(
        function() {
            $(".dropdown-content").finish().slideDown("slow");
        },
        function() {
            $(".dropdown-content").finish().slideUp("slow");
        }
    );
});

