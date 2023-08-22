$(document).ready(function() {
    // interaction update
    $('#command').keyup(function(e) {
        if (e.key === 'Enter') {
            let cmd = $('#command').val();
            $('#console').append('<div class="user-input"><img src="static/user.png" alt="avatar"><span>' + cmd + '</span></div>');
            $.ajax({
                url: '/command',
                type: 'POST',
                contentType: 'application/json',
                data: JSON.stringify({command: cmd}),
                dataType: 'json',
                success: function(data) {
                    $('#console').append('<div class="response"><img src="static/noa.webp" alt="avatar"><span>' + data.response + '</span></div>');
                    $('#command').val('');
                }
            });
        }
    });

    // load conversation
    $('#load-conversation').click(function() {
        $.ajax({
            url: '/load_conversation',
            type: 'GET',
            dataType: 'json',
            success: function(data) {
                $('#console').empty(); // 清空现有对话
                data.conversation.forEach(function(item) {
                    $('#console').append('<div class="' + item.type + '"><img src="static/avatar.png" alt="avatar"><span>' + item.message + '</span></div>');
                });
            }
        });
    });

});