<script>
function youtubeclick {
var y = //youtube username;
window.location.href = 'www.youtube.com/user/'+ y + '/videos';
var x = document.getElementsByClassName("yt-uix-sessionlink yt-uix-tile-link  spf-link  yt-ui-ellipsis yt-ui-ellipsis-2").href;
var videoid = x.substring(7);
window.history.go(-1);
}
</script>
