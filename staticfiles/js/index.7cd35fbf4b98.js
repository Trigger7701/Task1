$ ('textarea.editor').ckeditor ();
$('#pubid').click(
	function() {
	var url = '/post/'
	var data = JSON.stringify({
        'id':0,
		'title':document.getElementById('title_id').value,
		'name':document.getElementById(	'name_id').value,
		'text':$( 'textarea.editor' ).val()
	})
    send(data,url)
}
)
$('#editid').click(
	function() {
	url = '/post/'
    var id=document.getElementById('title_id').dataset.id
    var title=document.getElementById('title_id').value
	var name=document.getElementById(	'name_id').value
	var	text=$( 'textarea.editor' ).val()
	var data = JSON.stringify({
        'id':id,
		'title':title,
		'name':name,
		'text':text
	})
    send(data,url)
}
)
function send(data,url) {
    $.ajax({url: url,
		headers:{
        'Content-Type':'application/json',
        'X-CSRFToken':csrftoken,
    },
    type: 'POST',
    data: data,
    success: function (data, status, xhr) {
        $('p').append('status: ' + status + ', data: ' + data.url);
        $(location).attr('href', data.url)
    },
    error: function (jqXhr, textStatus, errorMessage) {
            $('p').append('Error' + errorMessage);
    }
});

}
