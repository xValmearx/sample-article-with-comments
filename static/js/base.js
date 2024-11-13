$(document).ready(function () {
    $('.like_button').click(function (event) {
        // Get request data
        let target = $(event.currentTarget);
        let article_id = target.data("id");
        let article_action = target.data("action");
        let aticle_like_url = target.data("like_url");

        // get icon and count elements
        let like_icon = target.find(".like_icon");
        let like_count = target.find('.like_count');
    });
});