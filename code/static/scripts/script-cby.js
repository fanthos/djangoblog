!function(r){e="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";(r.myatob=function(r){var o=String(r).replace(/=+$/,"");if(o.length%4==1)throw new Error("decrypt failed");for(var n,a,i=0,c=0,d="";a=o.charAt(c++);~a&&(n=i%4?64*n+a:a,i++%4)?d+=String.fromCharCode(255&n>>(-2*i&6)):0)a=e.indexOf(a);return d})}(this);
$(document).ready(
	function(){$(".enc-link").each(
		function(_, t){
			$(t).click(function(e){
				s=myatob;p=e.target;
				h=p.getAttribute("data-enchref");
				if(h=="")return;
				a=h.split("_");
				p.innerHTML=s(a[0]);p.href=s(a[1]);
				p.setAttribute("data-enchref","");
				return false})})});
