function isIE(){var n=navigator.userAgent.toLowerCase();return(n.indexOf('msie')!=-1)?parseInt(n.split('msie')[1]):false}
{h=document.getElementsByTagName("head")[0];
g=function(t){n=document.createElement("script");n.src=t;h.appendChild(n)}
c=function(t){n=document.createElement("link");n.rel="stylesheet";n.src=t;h.appendChild(n)}
g("//cdn.jsdelivr.net/html5shiv/3.7.2/html5shiv-printshiv.min.js");g("//cdn.jsdelivr.net/respond/1.4.2/respond.min.js");
t=isIE();if(t<8)c("scripts/bootstrap-ie7.css"),c("scripts/fix-ie7.css");
if(t<7)c("scripts/fix-ie6.css");
window.attachEvent("onload",function(){a=document.createElement("div");b=document.getElementsByTagName("body")[0];
a.innerHTML='<div class="alert alert-danger"><span class="glyphicon glyphicon-warning-sign glyphicons-lg"></span><div>PAGE MAY NOT DISPLAY CORRECTLY IN OLD BROWSERS!<br />Please upgrade your web browser.<br /><a href="http://windows.microsoft.com/internet-explorer/download-ie">Internet Explorer</a> | <a href="https://www.mozilla.org/firefox/">Firefox</a> | <a href="https://www.google.com/chrome/browser">Google Chrome</a> | <a href="http://www.opera.com/">Opera</a></div></div>';
b.insertBefore(a,b.firstChild)})}