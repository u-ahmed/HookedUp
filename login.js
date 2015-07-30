<script>
function loadCSVDoc(username, password)
{
var xmlhttp;
if (window.XMLHttpRequest)
  {// code for IE7+, Firefox, Chrome, Opera, Safari
  xmlhttp=new XMLHttpRequest();
  }
else
  {// code for IE6, IE5
  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
xmlhttp.onreadystatechange=function()
  {
  if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
    document.getElementById("myDiv").innerHTML=xmlhttp.responseText;
    }
  }
xmlhttp.open("GET","database.txt",true);
xmlhttp.send();

// number of rows in csv file
    var norows = xmlhttp.match(/^(.*)$/mg);


for (i = 0; i < norows; i++) {
var rows = getLines()
var keys = Object.keys(data[0]);
if (username == data[i][keys[0]]) {
	if (password == data[i][keys[1]] {
	//save other usernames, tokens, etc as cookies
	}
}

}
}
</script>

// call loadCSVDoc with the username and password