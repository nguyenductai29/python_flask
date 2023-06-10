$(function() {
    window.onbeforeunload = function () {

    };
    window.onunload = function () {

    };

    openLoading();

    window.onload = setTimeout(() => {
        closeLoading();
    }, 1000);

    // ajax
    $.ajaxSetup({
        headers: {
            "X-CSRF-TOKEN": $('meta[name="csrf-token"]').attr("content"),
        },
    });
})

// open loading
function openLoading() {
    $('.divLoading').css('visibility', 'visible');
    $('#divSpinner').removeClass('hidden');
    $('#divModalArea').addClass('show');
}

// close loading
function closeLoading() {
    $('.divLoading').css('visibility', 'hidden');
    $('#divSpinner').addClass('hidden');
    // $('#main').removeClass('hidden');
    $('#divModalArea').removeClass('show');
}
