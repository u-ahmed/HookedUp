<?php
//going to need to be run after js somehow, maybe reloaded page? Loop this *3 for different ids.

$videoId=//get it from database;
// url where feed is located
$url="http://gdata.youtube.com/feeds/api/videos/{$videoId}/comments";
// get the feed
$comments=simplexml_load_file($url);
// parse the feed using a loop
foreach($comments->entry as $comment)
{
 echo '<fieldset>'.$comment->content.'</fieldset>';
}

?>