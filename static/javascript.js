function FlightSelection {
    var e = document.getElementById("ddlViewBy");
    var value = e.value;
    var text = e.options[e.selectedIndex].text;
    return text;
}

var e = document.getElementById("ddlViewBy");
function onChange() {
  var value = e.value;
  var text = e.options[e.selectedIndex].text;
  console.log(value, text);
}
e.onchange = onChange;
onChange();





