<script>
function instagramclick(){
	window.location.href = 'https://instagram.com/oauth/authorize/?client_id=8a612cd650344523808233c0468c80ed&redirect_uri=	http://www.hookedupsocialmedia.co.uk&response_type=token';
	var token = window.location.href.substring(43);

	if(token="s_denied&error_reason=user_denied&error_description=The+user+denied+your+request"){
	alert("That's fine, but we can't access your instagram without your permission.);
	}
	else {
		//save token to database
	}

}
</script>