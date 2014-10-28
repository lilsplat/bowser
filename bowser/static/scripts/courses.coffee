var frm = $('#FORM-ID');
    frm.submit(function () {
        $.ajax({
            type: frm.attr('POST'),
            url: 'courses/newcourse',
            data: frm.serialize(),
            success: function (data) {
                $("#SOMEDIV").html(data);
            },
            error: function(data) {
                $("#MESSAGE-DIV").html("Something went wrong!");
            }
        });
        return false;
    });
