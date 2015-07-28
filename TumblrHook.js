function create(param) {
    var s= "";
    for(var i = 0; i < param; i++) {
        s+= '<input type="text" name="username">';
    }
    document.getElementById("screens").innerHTML=s;
};
function export(self) {
  var username [];
  var csvContent = "data:text/csv;charset=utf-8";
  data.forEach(function(infoArray, index)) {
    dataString = infoArray.join(",");
    csvContent += index < data.lengtt ? dataString + "\n" : dataString;
  }
};

var encodeUri = encodeURI(csvContent);
window.open(encodeUri)
