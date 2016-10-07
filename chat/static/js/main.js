$(function() {
    var messages = $('.messages');
    $.ajax({
        url: 'http://localhost:5000/messages',
        dataType: 'json',
    })
    .done(function(data) {
        for (var messageData in data) {
            if (!data.hasOwnProperty(messageData)) continue;

            var obj = data[messageData];
            for (var prop in obj) {
                if (!obj.hasOwnProperty(prop)) continue;
                messages.append('<li><strong>' + prop + '</strong> said ' + obj[prop] + '</li>');
            }
        }
    });
});
