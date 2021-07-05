if (screen.width >= 992) {
    document.getElementById("collapsible-nav").classList.add('show');
} else {
    document.getElementById("collapsible-nav").classList.remove('show');
}

document.getElementById("menu-btn").addEventListener("click", function() {
    var element = document.getElementById("collapsible-nav");
    if (element.classList) {
        element.classList.toggle("show");
    } else {
      // For IE9
      var classes = element.className.split(" ");
      var i = classes.indexOf("show");

      if (i >= 0) classes.splice(i, 1);
      else
        classes.push("show");
        element.className = classes.join(" ");
    }
});

document.getElementById("share").addEventListener("click", function() {
  const el = document.createElement('textarea');
  el.value = "Check out this amazing ❤ profile now! http://beastimran.com. BeastImran is really an amazing guy 🤩";
  el.setAttribute('readonly', '');
  el.style.position = 'absolute';
  el.style.left = '-9999px';
  document.body.appendChild(el);
  el.select();
  document.execCommand('copy');
  document.body.removeChild(el);
});